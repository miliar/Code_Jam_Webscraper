#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cctype>
#include <cassert>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>

#define D(x) cerr << #x << " = " << x << endl
#define REP(i,a,n) for(int i=(a); i<(int)(n); i++)
#define FOREACH(it,v) for(typeof((v).begin()) it=(v).begin(); it!=(v).end(); ++it)
#define ALL(v) (v).begin(), (v).end()

typedef long long int64;

const int INF = (int)(1e9);
const int64 INFLL = (int64)(1e18);
const double EPS = 1e-13;
const int SIZE = 100;
const int FILA = 0;
const int COLUMNA = 1;
int matrix[SIZE][SIZE];
int n,m;
using namespace std;

bool verify(int index, int orientation){
    
    if(orientation == FILA){
        for(int i=0;i<m;i++)
          if(matrix[index][i] != 1)
            return false;
    }else if(orientation == COLUMNA){
        for(int i=0;i<n ;i++)
          if(matrix[i][index] != 1)
            return false;
    }
    
    return true;
}

int main() {
  ios_base::sync_with_stdio(false);
  freopen("b.in","r", stdin);
  freopen("b.out","w", stdout);
  int t;
  cin >> t;
  for(int k=1;k<=t;k++){
   
    cin >> n >> m;
    
    for(int i=0;i<n;i++)
      for(int j=0;j<m;j++)
        cin >> matrix[i][j];
    bool paila = false;
    for(int i=0; i<n; i++){
        for(int j=0; j<m;j++){
            if(matrix[i][j] == 1){
                bool fila = verify(i,FILA); // verificar fila
                bool columna = verify(j,COLUMNA);
                //cout << i <<" "<<j <<" " <<!(fila || columna)<< endl; 
                if(!(fila || columna)){
                    paila = true;
                    i = n;
                    j = m;
                }
                  
            }
            
        }
    }
    if(paila)
      cout << "Case #"<<k<<": NO"<<endl;
    else
      cout << "Case #"<<k<<": YES"<<endl;
  }
  return 0;
}
