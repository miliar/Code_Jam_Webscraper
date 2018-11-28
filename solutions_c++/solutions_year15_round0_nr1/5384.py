#include<iostream>
#include<string>
#include<stdlib.h>
#include<math.h>
#include<sstream>
using namespace std;
int main()
{
	freopen("A-large.txt","r",stdin);
	
 int cases,f,cn=0,sol=0;
 string x;
 cin>>cases;
 for(int i=0; i<cases; i++)
 {
	cin>>f>>x;
	for(int t=0; t<x.length(); t++)
	{
		int res=0;
		if(t>cn)
		{
			sol+=t-cn;
			res=t-cn;
		}
         cn+=(int)x[t]-'0'+res;
	}
	 cout<<"Case #"<<i+1<<": "<<sol<<endl;
	  sol=0,cn=0;
 }
}