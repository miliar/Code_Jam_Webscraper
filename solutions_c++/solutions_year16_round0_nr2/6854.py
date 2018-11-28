//----------shivam_wadhwa----------//
#include <bits/stdc++.h>
#define ll long long int
#define sc1(x) scanf("%d",&x)
#define sc2(x,y) scanf("%d%d",&x,&y)
#define pint(c) printf("%d",c)
#define pll(c) printf("%lld",c)
#define ps() printf(" ")
#define pn() printf("\n")

#define vi vector<int>
#define vii vector<pair<int,int> >
#define mp make_pair
#define pb push_back
#define MAX 10000000
#define MOD 1000000007
using namespace std;
int main()
{
	int t=1;
	sc1(t);
	int k=1;
	while(k<=t)
	{
		string s;
		cin>>s;
		int A[s.length()];
		for(int i=0;i<s.length();++i)
		{
			A[i]=(s[i]=='+'?1:0);
		}
		int len=s.length();
		int i=len-1;
		int count=0;
		int flag=0;
		for(int i=len-1;i>=0;--i)
		{
			while(A[i]==1 && i>=0)
				i--;
			for(int j=0;j<=i;++j)
			{
				A[j]=!A[j];
				flag=1;
			}
			if(flag)
			{
				count++;
				flag=0;
			}
				
		}
		cout<<"Case #"<<k<<": "<<count<<"\n";
		k++;
	}
	return 0;
}
