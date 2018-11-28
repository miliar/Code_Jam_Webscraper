#include<iostream>
#include<cstdlib>
#include<cstdio>//old c library
#include<cmath>//ceil,floor,round,M_PI,,trig,pow(ambigous)
#include<cstring>
#include<iomanip>//set precisions
#include <algorithm>//using swap
#include<fstream>//used to manipulate files.
//#include <boost/multiprecision/cpp_int.hpp>//algerbric operations on string
//namespace mp=boost::multiprecision;
using namespace std;
int main()
{
	freopen("test.in","r",stdin);
	freopen("test.txt","w",stdout);
	int te,smax;
	cin>>te;
	char s[1002];
	int t,n,m,i;
	for(int x=1;x<=te;x++)
	{
		t=n=m=i=0;
		cin>>smax>>s;
		while(s[i]!='\0')
		{
			if(i==0 && s[i]=='0')
			{
			m=m+1;
			t=t+1;
			}
			else if(i==0 && s[i]!='0')
			{
				t=t+(s[i]-48);
			}
			if(i>0 && s[i]!='0')
			{
				if(i>t)
				{
					n=i-t;
					m+=n;
					t=t+(s[i]-48)+n;
					}
				else
				{
					t=t+(s[i]-48);
					}
				}
			i++;
			}
		cout<<"Case #"<<x<<": "<<m<<endl;
		}
	return 0;
}
