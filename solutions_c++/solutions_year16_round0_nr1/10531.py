#include<iostream>
#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<string>
#include<sstream>
using namespace std;
int check_all(vector<long int> v)
{
	for(int i=0;i<=9;i++)
	{
		if (find(v.begin(), v.end(),i)==v.end())
		{
			return 0;
		}
	}
	return 1;
}
vector<long int> insert(vector<long int> v,char c)
{
		int a=(int)c - 48;
		if (find(v.begin(), v.end(),a)==v.end())
		{
			v.push_back(a);
		}
		return v;
}
int main()
{ 
	freopen("A-large.in","rt",stdin);
	freopen("rajat_large.out","wt",stdout);
	int n;
	cin>>n;
	for(int j=0;j<n;j++)
	{
		long int numb;
		vector<long int> ar;
		cin>>numb;
		if(numb==0)
		{
			cout<<"Case #"<<j+1<<": "<<"INSOMNIA\n";
			continue;
		}
		int mul=1;
		long int number;
		while(check_all(ar)!=1)
		{	
			number=numb*mul++;
			char num[200];
			string num2;
			num2=to_string(number);
			strcpy(num,num2.c_str());
			for(int i=0;i<strlen(num);i++)
			{
				ar=insert(ar,num[i]);
			}
		}
		cout<<"Case #"<<j+1<<": "<<number<<"\n";
	}
	return 0;
}
