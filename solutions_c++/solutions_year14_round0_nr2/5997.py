// codejam2014.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#pragma warning(disable:4996)
#include<iostream>
#include <iomanip>
using namespace std;
//int a[4][4];
//int b[4][4];
//int type(int f,int s)
//{
//	int sum=0;
//	int temp=0;
//	for(int i=0;i<4;i++)
//		for(int j=0;j<4;j++)
//		{
//			if(a[f][i]==b[s][j])
//			{
//				if(sum==0)
//				   temp=a[f][i];
//				sum++;
//			}
//		}
//	if(sum==0)
//		return 0;
//	else if(sum==1)
//		return temp;
//	else
//		return -1;
//}
int _tmain(int argc, _TCHAR* argv[])
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	/*int t,f,s;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		cin>>f;
		cout<<"Case #"<<i<<": ";
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				cin>>a[j][k];
		cin>>s;
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				cin>>b[j][k];
		if(type(f-1,s-1)>0)
			cout<<type(f-1,s-1)<<endl;
		else if(type(f,s)==0)
			cout<<"Volunteer cheated!"<<endl;
		else
			cout<<"Bad magician!"<<endl;
	}*/



	int t;
	double c,f,x;
	cin>>t;
	double currate,pretotal;
	for(int i=1;i<=t;i++)
	{
		
		cout<<"Case #"<<i<<": ";
		cin>>c>>f>>x;
		currate=2;
		pretotal=0;
		double sum=0;
		/*while(pretotal>0)
		{
			
			if(pretotal>c&&pretotal/(currate+f)<(pretotal-c)/currate)
			{
				sum+=pretotal/currate;
				currate+=f;
				pretotal-=c;
			}
			else
			{
				sum+=pretotal/currate;
				pretotal-=c;
			}
			
		}*/
		if(x<c)
			cout<<fixed<<setprecision(7)<<x/currate<<endl;
		else
		{
			while(pretotal<x)
			{
				if(c+pretotal<x)
				{
				sum+=c/currate;
				pretotal+=c;
				}
				else
				{
                sum+=(x-pretotal)/currate;
				pretotal=x;
				}
				if(x>pretotal&&(x-pretotal)/currate>(x-pretotal+c)/(currate+f))
				{
					pretotal-=c;
					currate+=f;
				}
			}
			cout<<fixed<<setprecision(7)<<sum<<endl;
		}
		
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}

