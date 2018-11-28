/*
	Manish Kumar
	c0dezer0
	www.fb.com/kur.manish
*/
#include <bits/stdc++.h>
#define mod 1000000007
 
using namespace std;

int main()
{
    //ios_base::sync_with_stdio(false);cin.tie(0);
	
	int t,smax,i,j,k,l,a,b,c;
	cin>>t;
	for(j=1;j<=t;j++)
	{
		cin>>smax;
		string s ;
		cin>>s;
		a=0;
		c=0;
		for(i=0;i<=smax;i++)
		{
			if(int(s[i])&&i>a)
			{
				c+= i-a;
				a+= i-a;
				//cout<<i<<" "<<a<<"\n";
			}
			a+= int(s[i]-'0');
			
		}
		//cout<<c<<"\n";
		cout<<"Case #"<<j<<": "<<c<<"\n";
	}
	
	
    return 0;

}
