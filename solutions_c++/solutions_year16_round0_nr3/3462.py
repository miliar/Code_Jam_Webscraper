/*
 * jamcoin.cpp
 *
 *  Created on: Apr 9, 2016
 *      Author: natali
 */
#include<iostream>
#include<string>
#include<vector>
#include<math.h>
#include<stdio.h>
#include<fstream>

using namespace std;

vector<string>  binaries;
vector<long long> divisors;

char a[14];

void get_numbers(int n)
{
	if(n==-1)
	{
		binaries.push_back('1'+(string)a+'1');
		return;
	}
	a[n]='0';
	get_numbers(n-1);
	a[n]='1';
	get_numbers(n-1);

}

long long construct(string strNumber, long long base)
{
	long long ans=0;
	for(int i=0; i<strNumber.size(); i++)
	{
		ans*=base;
		if(strNumber[i]=='1') ans+=1;
	}
	return ans;
}

long long get_divider(long long number)
{
	long long m=sqrt(double(number));
	//cout<<"sqrt"<<m<<endl;
	for(long long i=2; i<=m; i++)
	{
		if(number%i==0) return i;
	}
	return 1;
}

int main()
{
	//cout<<binaries.size()<<endl;
	freopen("C-small-attempt1.in", "r", stdin);
	freopen ("out.txt", "w", stdout);
	int t,n,r;
	cin>>t>>n>>r;
	//cout<<n<<" "<<r<<endl;
	cout<<"Case #1:\n";
	int count=0;
	long long numb;
	long long d;
	get_numbers(n-3);
	bool ch;
	//cout<<get_divider(60063);
	for(int i=0; i<16384; i++)
	{
		if(count==r) break;
		ch=true;
		for(long long j=2; j<11; j++)
		{
			numb=construct(binaries[i],j);
			//cout<<"numb "<<numb<<endl;
			d=get_divider(numb);
			if(d==1)
			{
				//cout<<numb<<" "<<j<<endl;
				ch=false;
				break;
			}
			divisors.push_back(d);
		}
		if(ch)
		{
			cout<<binaries[i]<<" ";
			for(int j=0; j<9; j++)
			{
				cout<<divisors[j]<<" ";
			}
			cout<<endl;
			count++;
		}
		divisors.clear();
	}
	return 0;
}





