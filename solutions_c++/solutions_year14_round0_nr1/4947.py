#include<vector>
#include<cstring>
#include<algorithm>
#include<stdio.h>
#include<climits>
#include<set>
#include<cmath>
#include<bitset>
#include<map>
#include<iostream>
#include<queue>
#define test(t) while(t--)
#define s(n) scanf("%d",&n)
#define sl(n) scanf("%llu",&n)
 
#define p(n) printf("%llu\n",n)
#define rep(i,a,n) for(i=a;i<=n;i++)
#define vi vector<int>
#define vii vector< vector<int> >
#define vpii vector< pair<int,int> >
#define mii map<int,int>
#define pb push_back
#define inf 1000000000LL
#define mp make_pair
#define MOD 1000000009LL
#define ll long long
#define gc getchar_unlocked
using namespace std;
int main()
{
	
	int t1[5],t2[5],i,j,k;
	int t,n1,n2,num;
	s(t);
	for(k=1;k<=t;++k)
	{
		s(n1);
		for(i=1;i<=4;++i)
		{
			for(j=1;j<=4;++j)
			{
				s(num);
				if(i==n1)
				t1[j]=num;
			}
		}
		s(n2);
		for(i=1;i<=4;++i)
		{
			for(j=1;j<=4;++j)
			{
				s(num);
				if(i==n2)
				t2[j]=num;
			}
		}
		int same;int ct;
		ct=0;
		for(i=1;i<=4;++i)
		{
			for(j=1;j<=4;++j)
			{
				if(t1[i]==t2[j])
				{
					ct++;
					same=t1[i];
				}
			}
		}
		if(ct>=2)
		cout<<"Case #"<<k<<": "<<"Bad magician!"<<endl;
		else if(ct==0)
		cout<<"Case #"<<k<<": "<<"Volunteer cheated!"<<endl;
		else
		cout<<"Case #"<<k<<": "<<same<<endl;
	}
}
