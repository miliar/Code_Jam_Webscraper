#include <bits/stdc++.h>
using namespace std;
int main()
{
	freopen( "input.txt","r",stdin );
    freopen( "output.txt","w",stdout );
    long long a,b,c,d=0,e,f,g,h,i,j,k=1,l=0,m[10],n;
    string s;
    cin>>a;
    for (i=0;i<a; i++) {
    	cin>>s;
    	l=0;
    	n=s.length();
    	for (j=1;j<n; j++)
    			if (s[j]!=s[j-1]) l++;
    	if (s[n-1]=='-') l++;
    	cout<<"Case #"<<i+1<<": "<<l<<"\n";
    }

return 0;
}