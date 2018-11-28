/*This program is made on Vibhore's Machine.*/
#include<iostream>
#include<stdio.h>
#include<fstream>
#include<cstdio>
using namespace std;
int main()
{
  freopen("/home/archit/Documents/COdejam/Qualification/OMINUS/D-small-attempt0.in", "r", stdin);
  freopen("7", "w", stdout);

	int t,n,i,j,k,sum,ans,x,r,c;
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
		cin>>x>>r>>c;
		int max=r;
		if(max<c)
		max=c;
		if(x>max)
		{
		cout<<"Case #"<<(i+1)<<": RICHARD"<<endl;
		}
		else if((r*c)%x!=0)
		cout<<"Case #"<<(i+1)<<": RICHARD"<<endl;
		else if((r==1&&(c==3||c==4))||((c==1)&&(r==3||r==4)))
		{if(max==x)
		cout<<"Case #"<<(i+1)<<": RICHARD"<<endl;
		else
		cout<<"Case #"<<(i+1)<<": GABRIEL"<<endl;}
		else if((r==4&&c==2)||(r==2&&c==4))
		{if(x==4)
		cout<<"Case #"<<(i+1)<<": RICHARD"<<endl;
		else
		cout<<"Case #"<<(i+1)<<": GABRIEL"<<endl;}
		else
		cout<<"Case #"<<(i+1)<<": GABRIEL"<<endl;
	}
	return 0;
}

