//Case #1: 0

#include <bits/stdc++.h>
using namespace std;
int main()
{
	string s;
    int test,n,add=0,peo=0,i,j;
    cin>>test;
    for(j=1;j<=test;++j)
    {
           cin>>n;
           cin>>s;
           add=0;
           peo=0;
           int l=s.length();
           for(i=0;i<l;++i)
           {
           	     int corr=s[i]-'0';
           	     if(i==0)
           	     {
           	     	peo=peo+corr;
           	     	continue;
           	     }
           	     if(i<=peo)
           	     {
           	     	peo=peo+corr;
           	     }
           	     else
           	     {
           	     	add=add+(i-peo);
           	     	peo=peo+corr+(i-peo);
           	     }

           }
           cout<<peo<<endl;
           cout<<"Case #"<<j<<": "<<add<<endl;
    }
    return 0;


}