#include <bits/stdc++.h>
using namespace std;
int mul(int a,int b)
{
	if(a==1)return b;
	if(b==1)return a;
	if(a==-1)return -b;
	if(b==-1)return -a;
	if(a==b)return -1;
	if(a<0)return -mul(-a,b);
	if(b<0)return -mul(a,-b);
	if((3+b-a)%3==1)return (9-a-b);
	return -(9-a-b);
}
int power(int a,long long b)
{
	if(b>3)return power(a,b%4);
	if(b==0)return 1;
	if(b==1)return a;
	if(b==2)return mul(a,a);
	return mul(a,mul(a,a));
}
/*
 * -4 -3 -2 -1 0 1 2 3 4
 * -k -j -i -1   1 i j k
 */
int main()
{
	int cas;
	cin>>cas;
	for(int t=1;t<=cas;t++)
	{
		long long l,x;
		cin>>l>>x;
		string s;
		cin>>s;
		for(int i=0;i<l;i++)s[i]=s[i]-'g';
		if(l*x<3)
		{
			cout<<"Case #"<<t<<": NO"<<endl;
			continue;
		}
		int cur;cur=s[0];
		for(int i=1;i<l;i++)cur=mul(cur,s[i]);
		if(power(cur,x)!=-1)
		{
			cout<<"Case #"<<t<<": NO"<<endl;
			continue;
		}
		if(x>=8)
		{
			s=s+s+s+s+s+s+s+s;
			int cc=s[0],i=1,first,last;
			while(cc!=2&&i<8*l)
				cc=mul(cc,s[i++]);
			if(cc!=2)
			{
				cout<<"Case #"<<t<<": NO"<<endl;
				continue;
			}
			first=i-1;
			cc=s[8*l-1];i=8*l-2;
			while(cc!=4&&i>=0)
				cc=mul(s[i--],cc);
			if(cc!=4)
			{
				cout<<"Case #"<<t<<": NO"<<endl;
				continue;
			}
			last=(x-8)*l+i+1;
			if(first<last)
			{
				cout<<"Case #"<<t<<": YES"<<endl;
				continue;
			}
			cout<<"Case #"<<t<<": NO"<<endl;
		}
		else
		{
			string temp="";
			for(int i=0;i<x;i++)
				temp=temp+s;
			s=temp;
			int cc=s[0],i=1,first,last;
			while(cc!=2&&i<x*l)
				cc=mul(cc,s[i++]);
			if(cc!=2)
			{
				cout<<"Case #"<<t<<": NO"<<endl;
				continue;
			}
			first=i-1;
			cc=s[x*l-1];i=x*l-2;
			while(cc!=4&&i>=0)
				cc=mul(s[i--],cc);
			if(cc!=4)
			{
				cout<<"Case #"<<t<<": NO"<<endl;
				continue;
			}
			last=i+1;
			if(first<last)
			{
				cout<<"Case #"<<t<<": YES"<<endl;
				continue;
			}
			cout<<"Case #"<<t<<": NO"<<endl;
		}
	}
	return 0;
}
