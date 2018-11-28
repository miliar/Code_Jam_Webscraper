#include <iostream>
#include <assert.h>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <map>
#include <queue>
#include <string>

using namespace std; 
 
int f[2000],g[2000];
 
int main()
{
 //freopen("input.txt","r",stdin);
 // freopen("output.txt","w",stdout);  

  int t,nm1=0;
  cin >> t;
  while(t > 0)
  {
	  t--;nm1++; 
	  string ans;
	  int x,n,m;
	  cin >> x >> n >> m;
	  if(n > m ) swap(n,m);
	  if(x == 1) ans = "GABRIEL";
	  if(x == 2)
	  {
		  if(n*m % 2 == 0)  ans = "GABRIEL";
		  else  ans = "RICHARD";
	  }
	  if(x == 3)
	  {
		  if(n == 1 && m == 1) ans = "RICHARD";
		  if(n == 1 && m == 2) ans = "RICHARD";
		  if(n == 1 && m == 3) ans = "RICHARD";
		  if(n == 1 && m == 4) ans = "RICHARD";
		  if(n == 2 && m == 2) ans = "RICHARD";
		  if(n == 2 && m == 3) ans = "GABRIEL";
		  if(n == 2 && m == 4) ans = "RICHARD";
		  if(n == 3 && m == 3) ans = "GABRIEL";
		  if(n == 3 && m == 4) ans = "GABRIEL";
		  if(n == 4 && m == 4) ans = "RICHARD"; 
	  }
	  if(x == 4)
	  {
		  if(n == 1 && m == 1) ans = "RICHARD";
		  if(n == 1 && m == 2) ans = "RICHARD";
		  if(n == 1 && m == 3) ans = "RICHARD";
		  if(n == 1 && m == 4) ans = "RICHARD";
		  if(n == 2 && m == 2) ans = "RICHARD";
		  if(n == 2 && m == 3) ans = "RICHARD";
		  if(n == 2 && m == 4) ans = "RICHARD";
		  if(n == 3 && m == 3) ans = "RICHARD";
		  if(n == 3 && m == 4) ans = "GABRIEL";
		  if(n == 4 && m == 4) ans = "GABRIEL"; 
	  }


	  cout << "Case #" << nm1 << ": " << ans << endl; 
  }
}