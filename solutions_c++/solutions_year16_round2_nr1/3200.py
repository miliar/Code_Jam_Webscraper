#include <iostream>
#include<bits/stdc++.h>
#include<algorithm>
#include<cmath>
#include<limits.h>
#define r(i,n) for(int i=0;i<n;i++)
using namespace std;
int main()
{
	freopen("C://Users//Abhishek//Desktop//Algorithm Coursera//Round 1BV//A-small-attempt0.in","r",stdin);
	freopen("C://Users//Abhishek//Desktop//Algorithm Coursera//abhishek.txt","w",stdout);
	int t;
	cin>>t;
	for(int j=1;j<=t;j++)
	{
		string s;
		cin>>s;
		int n=s.length();
		int a[26]={0};
		int i,zero=0,one=0,two=0,three=0,four=0,five=0,six=0,seven=0,eight=0,nine=0;
		for(i=0;i<n;i++)
			a[(int)s[i]-65]++;
		if(a[25]>0)
		{
			zero=a[25];
			a[4]-=zero;
			a[17]-=zero;
			a[14]-=zero;
		}
		if(a[22]>0)
		{
			two=a[22];
			a[19]-=two;
			a[14]-=two;
		}
		if(a[20]>0)
		{
			four=a[20];
			a[5]-=four;
			a[14]-=four;
			a[17]-=four;
		}
		if(a[23]>0)
		{
			six=a[23];
			a[18]-=six;
			a[8]-=six;
		}
		if(a[6]>0)
		{
			eight=a[6];
			a[4]-=eight;
			a[8]-=eight;
			a[7]-=eight;
			a[19]-=eight;
		}
		if(a[14]>0)
		{
			one=a[14];
			a[13]-=one;
			a[4]-=one;
		}
		if(a[19]>0)
		{
			three=a[19];
			a[7]-=three;
			a[17]-=three;
			a[4]-=2*(three);
		}
		if(a[5]>0)
		{
			five=a[5];
			a[8]-=five;
			a[21]-=five;
			a[4]-=five;
		}
		if(a[18]>0)
		{
			seven=a[18];
			a[4]-=2*(seven);
			a[21]-=seven;;
			a[13]-=seven;
		}
		if(a[13]>0)
			nine=a[13]/2;
		cout<<"Case #"<<j<<": ";
		for(i=0;i<zero;i++)
			cout<<"0";
		for(i=0;i<one;i++)
			cout<<"1";
		for(i=0;i<two;i++)
			cout<<"2";
		for(i=0;i<three;i++)
			cout<<"3";
		for(i=0;i<four;i++)
			cout<<"4";
		for(i=0;i<five;i++)
			cout<<"5";
		for(i=0;i<six;i++)
			cout<<"6";
		for(i=0;i<seven;i++)
			cout<<"7";
		for(i=0;i<eight;i++)
			cout<<"8";
		for(i=0;i<nine;i++)
			cout<<"9";
		cout<<endl;
	}
	
}

