#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
int t;
    cin>>t;
    for(int in=1;in<=t;in++)
    {
    	int c[17]={0},a[4][4]={0},r,nu,c2=0;
    	cin>>r;
    	for(int i=0;i<4;i++)for(int j=0;j<4;j++)cin>>a[i][j];
    	for(int j=0;j<4;j++)
    	{
    		c[a[r-1][j]]++;
    	}
    	cin>>r;
    	for(int i=0;i<4;i++)for(int j=0;j<4;j++)cin>>a[i][j];
    	for(int j=0;j<4;j++)
    	{
    		c[a[r-1][j]]++;
    	}
    	for(int j=1;j<=16;j++)
    	{
    		if(c[j]==2){c2++;nu=j;}
    	}
    	//cout<<c2<<endl;
    	if(c2>1)cout<<"Case #"<<in<<": "<<"Bad magician!"<<endl;
    	else if(c2==1)cout<<"Case #"<<in<<": "<<nu<<endl;
    	else cout<<"Case #"<<in<<": "<<"Volunteer cheated!"<<endl;
   	}
}