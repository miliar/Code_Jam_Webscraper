#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <map>

using namespace std;
long long t,pp,i,j,a,b,s,f,x,k,l,m,n;
char c[111][111];
vector <long long> p,q;
int main() {
  cin >>t;
  while (t --){
  	cin >> n>>m>>k;
    s = 0;
    x = m*n - k;
    if (m ==1 || n ==1){
      if (k == m*n)s = 5;
      else s = 4; 
    }
    else{
      if (k > m*n - 4) s = 5;
      if (k == m*n - 5 || k == m*n - 7) s = 5;
      if (m ==2 || n == 2){
        if (k %2 ==1) s = 5;
      }
    }
    if (k == m*n - 1) s = 3;
    printf ("Case #%lld:\n",++pp);
    
    if (s == 5)cout << "Impossible"<<endl;
    else {
      for (i = 0; i < n; i ++)
        for (j = 0; j < m ; j ++)
          c[i][j] = '*';
      k = m*n - k;
      if (k <= m*2&&k>1){
        if (k%2 == 1){
          k -= 3;
        	c[2][0] = '.';
        	c[2][1] = '.';
        	c[2][2] = '.';
        }
      	for (i = 0; i < k/2; i ++){
          	c[0][i] = '.';
          	c[1][i] = '.'; 
        }
      }else if (k !=1){
        a = k / m;
      	b = k % m;
      	for (i = 0; i < a; i ++){
          for (j = 0; j <m; j ++)
            c[i][j] = '.'; 
        }
      	if (b == 1){
          if (a == 2) {
            b += 2; 
            c[0][m-1] = '*';
            c[1][m-1] = '*';
          }
          else {
            b ++;
            c[a-1][m-1] = '*';
          }
        }
      	for (i = 0; i < b; i ++)
          c[a][i] = '.';
          
      }
      if (n == 1 || m == 1){
     	 for (i = 0; i < n; i ++){
        	for (j = 0; j < m ; j ++){
              c[i][j] ='*';
              if (x > 0) c[i][j] = '.';
              x --;
            }
         }
      }
      c[0][0] = 'c';
      for (i = 0; i < n; i ++){
        for (j = 0; j < m ; j ++)
          cout <<c[i][j];
      	cout << endl;
      }
      
    }
  }
  
  return 0;
}
