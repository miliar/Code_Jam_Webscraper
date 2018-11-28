#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

using namespace std;

struct day{
  int e, r, n;
  vector< int > v;
};


int next_day( day d, int enow, int i ){
  int e,r,n,v;
  int enow2,euse;
  int max = 0;
  int maxj;
  e = d.e;
  r = d.r;
  n = d.n;

  if ( i == n-1 ){
    return enow * d.v[i]; 
  } else {
    for ( euse = 0; euse <= enow; ++euse ){
      maxj = euse * d.v[i];
      enow2 = enow - euse + d.r; 
      if ( enow2 > d.e ) enow2 = d.e;
      maxj += next_day( d, enow2, i+1  );
      if ( maxj > max ) max = maxj;
    }
    return max;
  }

}

int max_day( day d ){
  int e,r,n,v;
  int enow,euse;
  int i;
  int max = 0;
  e = d.e;
  r = d.r;
  n = d.n;
  enow = e;
  
/*
  for ( i = 0; i < n; i++ ){
    euse = 2;
    enow -= euse;
    max += euse*d.v[i];
    enow += r;
    if ( enow > e ) enow = e;
  }
*/

  return max;
}

int main(){

  using namespace std;
  fstream fin("g1.dat",ios::in);
  int i,j,k;
  int t, ti;
  fin >> t;
  int e,r,n,v;

  vector< day > days(t);

  //cout << n_cases << endl;
  for ( ti = 0; ti < t; ++ti ){
    fin >> e >> r >> n;
    days[ti].e = e;
    days[ti].r = r;
    days[ti].n = n;
    //cout << ti << " " << e << " " << r << " " << n << " " << endl;
    for ( int i = 0; i < n; ++i ){
      fin >> v;
      days[ti].v.push_back(v);
    }
  }
  fin.close();


  for ( ti = 0; ti < t; ++ti ){
    std::cout << next_day(days[ti],days[ti].e,0) << " ";
    cout << endl;
  }


  
  fstream fout("o1.dat",ios::out);
  for ( ti = 0; ti < t; ++ti ){
    std::cout << next_day(days[ti],days[ti].e,0) << " ";
    cout << endl;
    fout << "Case #" << (ti+1) << ": " << next_day(days[ti],days[ti].e,0) << endl;
  }
/*
  for ( i_case = 0; i_case < num_cases; ++i_case ){
    int rs = k_in_n(boards[i_case],'R');
    int bs = k_in_n(boards[i_case],'B');
    if ( rs > 0 )
      cout << i_case << " R " << rs << endl;
    if ( bs > 0 )
      cout << i_case << " B " << bs << endl;
    if ((rs>0)&&(bs>0)){
      fout << "Case #" << (i_case+1) << ": Both" << endl;
    } else if (rs>0){
      fout << "Case #" << (i_case+1) << ": Red" << endl;
    } else if (bs>0){
      fout << "Case #" << (i_case+1) << ": Blue" << endl;
    } else {
      fout << "Case #" << (i_case+1) << ": Neither" << endl;
    }
  }
*/
  return 0;
}



