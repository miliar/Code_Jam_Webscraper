#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

struct board{
  std::vector< std::vector< int > > b;
  int n;
  int m;
};

int equal_boards( board b1, board b2 ){
  int equal_b = 1;
  int n = b1.n;
  int m = b1.m;
  int i,j;
  if ( b2.n != n )
    equal_b = 0;  
  if ( b2.m != m )
    equal_b = 0;  
  for ( i = 0; i < n; ++i ){
    for ( j = 0; j < m; ++j ){
      if ( b1.b[i][j] != b2.b[i][j] )
        equal_b = 0;
    }
  }
  return equal_b;
}

int is_possible( board b ){
  int n = b.n;
  int m = b.m;
  int i,j;
  int imax,jmax;
  int possible;
  int max = 0;
  
  for ( i = 0; i < n; ++i ){
    for ( j = 0; j < m; ++j ){
      if ( b.b[i][j] > max ){
        max = b.b[i][j];
        imax = i;
        jmax = j;
      }
    }
  } 

  

  board b2;
  b2.n = n; 
  b2.m = m;
  b2.b.resize(n);
  for ( i = 0; i < n; ++i)
    b2.b[i].resize(m);  
  for ( i = 0; i < n; ++i ){
    for ( j = 0; j < m; ++j ){
      b2.b[i][j] = max;
    }
  }

  int h;
  // vertical shave:
  for ( i = 0; i < imax; ++i ){
    h = b.b[i][jmax];
    for ( j = 0; j < m; ++j ){
      b2.b[i][j] = h;
    }
  }
  for ( i = imax+1; i < n; ++i ){
    h = b.b[i][jmax];
    for ( j = 0; j < m; ++j ){
      b2.b[i][j] = h;
    }
  }

  // horizontal shave:
  for ( j = 0; j < jmax; ++j ){
    h = b.b[imax][j];
    for ( i = 0; i < n; ++i ){
      if ( b2.b[i][j] > h ){        
        b2.b[i][j] = h;
      }
    }
  }
  for ( j = jmax+1; j < m; ++j ){
    h = b.b[imax][j];
    for ( i = 0; i < n; ++i ){
      if ( b2.b[i][j] > h ){        
        b2.b[i][j] = h;
      }
    }
  }
    
  
  std::cout << std::endl;
  for ( i = 0; i < n; ++i ){
    for ( j = 0; j < m; ++j ){
      std::cout << b2.b[i][j] << " ";
    }
    std::cout << std::endl;
  }

  possible = equal_boards( b, b2 );
  return possible;
}

int main(){

  using namespace std;
  fstream fin("g1.dat",ios::in);
  int i,j,k;
  int t, ti;
  fin >> t;

  vector< board > bs(t); 

  //cout << n_cases << endl;
  for ( ti= 0; ti< t; ++ti ){
    int n,m;
    fin >> n;
    fin >> m;
    bs[ti].n = n; bs[ti].m = m;
    bs[ti].b.resize(n);
    for ( i = 0; i < n; ++i)
      bs[ti].b[i].resize(m);
    
    for ( i = 0; i < n; ++i)
      for ( j = 0; j < m; ++j)
        fin >> bs[ti].b[i][j];
  }
  fin.close();

  
  for ( ti= 0; ti< t; ++ti ){
    for ( i = 0; i < bs[ti].n; ++i){
      for ( j = 0; j < bs[ti].m; ++j)
        cout << bs[ti].b[i][j] << " ";
      cout << endl;
    }
  }


  
  fstream fout("o1.dat",ios::out);
  for ( ti = 0; ti < t; ++ti ){
    if ( is_possible( bs[ti] ) == 1 ){
      fout << "Case #" << (ti+1) << ": YES" << endl;
    } else {
      fout << "Case #" << (ti+1) << ": NO" << endl;
    }
  }

  return 0;
}



