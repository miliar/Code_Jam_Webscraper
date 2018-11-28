#include <bits/stdc++.h>
using namespace std;
 
int main()
{
	long int t,x,n,c,flag,m,r,y,s,j;
	int v[10];
 
	cin>>t;
 
	for(x=1;x<=t;x++)
	{
 
		for(y=0;y<=9;y++)
		v[y]=-1;
 
		flag=1;
 
		cin>>n;
		j=n;
		c=1;
		while(flag == 1 && n !=0)
		{
		m=j;
		while(m!=0)
		{
			r=m%10;
			if(v[r] == -1)
			v[r]=v[r]+2;
 
			m=m/10;
		}
		for(y=0;y<10;y++)
		{
			s=s+v[y];
		}
			if(s == 10){
			cout<<"Case #"<<x<<": "<<j<<endl;
			flag=0;
			}
 
			s=0;
 
			j=n*(c++);
		}
 
		if(n == 0)
		cout<<"Case #"<<x<<": "<<"INSOMNIA\n";
 
 
	}
	return 0;
}