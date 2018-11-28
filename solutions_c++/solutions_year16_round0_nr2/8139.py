//Author:Hena Firdaus
#include <bits/stdc++.h>
using namespace std;
#define mp make_pair
typedef pair<int,int> ii;
#define fr(i,a,b) for(i=a;i<b;i++)
int A[105];
int main()
{
	int t,i,f;
	string str;
	freopen("in3.txt","r",stdin);
	freopen("out3.txt","w",stdout);
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		cin>>str;
		int len=str.length();
		
		int c1=0,c2=0;
		for(int i=0;i<len;i++)
		{
			if(str[i]=='+')
				{c1++;A[i]=1;}
			else
				{c2++;A[i]=0;}
		}
      if(c1==len)
      	{cout<<"Case #"<<k<<": 0"<<endl;
         continue;}
      else
      	if(c2==len)
      {cout<<"Case #"<<k<<": 1"<<endl;
      	continue;}
	if(str[0]=='+')
		f=1;
	else
		f=0;
	int count=0;
	for(int i=1;i<len;)
	{
		if(A[i]!=A[i-1])
		{
			if(f)//Positive-negative
			{
				while(!A[i] && i<len)
				{
					A[i]=1;
					i++;
					
				}
				count+=2;
			}
			else//Negative-positive
			{
				while(A[i] && i<len)
				{
					A[i]=1;
					i++;
					
					f=1;
				}
				count+=1;
			}
			
		}
		else
			i++;


	}
	cout<<"Case #"<<k<<": "<<count<<endl;
	}
	return 0;
}
