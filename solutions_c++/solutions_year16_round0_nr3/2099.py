// QualRound.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include "vector"
#include "string"
#include "algorithm"
#include "string.h"
#include "stdio.h"
#include "iostream"
using namespace std;

string toBinary(long long t)
{
	string ret;
	while(t)
	{
		if(t&1) ret.push_back('1');
		else ret.push_back('0');
		t>>=1;
	}
	reverse(ret.begin(),ret.end());
	return ret;
}

int main()
{
	long long g=(1LL<<31)+1;
	int factors[5]={2,3,5,7,11};
	long long MOD = 2*3*5*7*11;
	while(g%3) g+=2;
	int J=500;
	cout<<"Case #1:"<<endl;
	while(J){
		g+=6;
		string ans=toBinary(g);
		int v[11]={};
		long long c[11]={};
		int valid=1;
		for(int i=3;i<=10;i++) {
			long long t=1,cur=0;
			for(int j=ans.size()-1;j>=0;j--)
			{
				if(ans[j]=='1')
					cur+=t;
				t=t*i%MOD;
			}
			c[i]=cur;
			for(int j=0;j<5;j++)
			{
				if(cur%factors[j]==0) v[i]=factors[j];
			}
			if(v[i]==0){valid=0; break;}
		}
		if(valid) 
		{
			cout<<ans<<" "<<3;
			for(int i=3;i<=10;i++)
			{
				cout<<" "<<v[i];
			}
			cout<<endl;
			J--;
		}
	}
	return 0;
}

