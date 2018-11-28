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
 
 
int main()
{
 //freopen("input.txt","r",stdin);
 //  freopen("output.txt","w",stdout); 
 int t,nm=0;
 cin >> t;
 while(t > 0)
 {
	 t--;nm++;
	 int n,ans=0,c=0;
	 cin >> n;
	 string s;
	 cin >> s;
	 int x=0,y=s.length()-1;
	 while(s[y] == '0')
	 { 
		 x++;y--;
	 }
	 if(x > 0) s.erase(y+1,x);
	 for(int i(0);i<s.size();i++)
	 {
		 if(ans < i){ c += i -ans;ans = i;}
		 ans += (int)s[i] - 48;
	 }
	 cout << "Case #" << nm << ": " << c << endl;
 }
}
