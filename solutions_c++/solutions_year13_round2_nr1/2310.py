#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

struct game{
  int a;
  int n;
  vector< int > m;
};

int eval_game( game g ){
  int i,i2;
  int ops = 0;
  int size = g.a;
  int n = g.n;
  int mleft = n;
  int nsmaller = 0;

  vector< int > mi = g.m;
  sort(mi.begin(),mi.end());
  //reverse(mi.begin(),mi.end());

  // 1 special case:
  if ( mi[0] >= 1 && size == 1 )
    return n;

  vector < int > cumul(n+1);
  cumul[0] = g.a;
  for ( i = 0; i < n; ++i ){
    cumul[i+1] = cumul[i] + mi[i];
  }

  
/*
  cout << size << " : ";
  for ( i = 0; i < n; ++i ){
    cout << mi[i] << " ";
  }
  cout << endl;
  for ( i = 0; i <= n; ++i ){
    cout << cumul[i] << " ";
  }
  cout << endl;

*/
  vector< int > added(n,0);
  for ( i = 0; i < n; ++i ){
    double cumulold = cumul[i];
    while ( mi[i] >= cumul[i] ){    
      cumul[i] = 2*cumul[i] - 1;
      added[i]++;
      //cout << "hey";
    }
    // correct the rest:
    for ( i2 = i+1; i2 < n; ++i2 ){
      cumul[i2] += ( cumul[i] - cumulold );
    }
  }

/*
  for ( i = 0; i < n; ++i ){
    cout << added[i] << " ";
  }
  cout << endl;
*/

  int tadded = 0;
  for ( i = 0; i < n; i++ ){
    tadded += added[i];
  }
  int cadded = 0;
  for ( i = 0; i < n; i++ ){
    int nextadd = added[i];
    int nleft = n - i;
    if ( nextadd < nleft ){
      cadded += nextadd;
      ops += nextadd;
    } else {
      ops += nleft;
      break;
    }
  }
  
  return ops;
}

int main(){

  using namespace std;
  fstream fin("g1.dat",ios::in);
  int i,j,k;
  int t, ti;
  fin >> t;
  int a,n,mi;

  vector< game > g(t);

  //cout << n_cases << endl;
  for ( ti = 0; ti < t; ++ti ){
    fin >> a >> n;
    g[ti].a = a;
    g[ti].n = n;
    //cout << ti << " " << e << " " << r << " " << n << " " << endl;
    for ( int i = 0; i < n; ++i ){
      fin >> mi;
      g[ti].m.push_back(mi);
    }
  }
  fin.close();


/*
  for ( ti = 0; ti < t; ++ti ){
    //std::cout << g[ti].a << " ";
    //for ( int i = 0; i < g[ti].m.size(); ++i ){
    //  cout << g[ti].m[i] << " ";
    //}
    i = eval_game(g[ti]);
    cout << " ops " << i << endl;
  }
*/

  
  fstream fout("o1.dat",ios::out);
  for ( ti = 0; ti < t; ++ti ){
    std::cout << eval_game(g[ti]) << " ";
    //cout << endl;
    //fout << "Case #" << (ti+1) << ": " << next_day(days[ti],days[ti].e,0) << endl;
    fout << "Case #" << (ti+1) << ": " << eval_game(g[ti]) << endl;
  }

  return 0;
}



