#include<iostream>
#include<cstdio>
#include<vector>
#include<cstring>
#include<algorithm>
#include<bitset>
#include<cmath>
#include<string>
#include<climits>
#include <fstream>
#include<queue>
#include<cstdlib>
#include<iomanip>
#define rep(i,n) for(int i=0;i<n;i++)
#define repup(i,a,b) for(int i=a;i<=b;i++)
#define repdn(i,a,b) for(int i=b;i>=b;i--)
#define scd(n) scanf("%d",&n);
#define scl(n) scanf("%lld",&n);
#define scs(str) scanf("%s",str);
#define prdl(n) printf("%d\n",n);
#define prll(n) printf("%lld\n",n);
#define prd(n) printf("%d",n);
#define prl(n) printf("%lld",n);
#define pb push_back;
#define mp make_pair;
#define vi vector<int>;
#define vp vector< pair<int ,int> >;
typedef long long ll;
using namespace std;
ll mod=1e9+7;
int main()
{
	ofstream myfile;
	myfile.open ("example.txt");
	int t;
	cin>>t;
	
	repup(j,1,t)
	{
		string str;
		cin>>str;
		int count=0;
		for(int i=str.size()-1;i>=0;i--)
		{
			if((str[i]=='+' && count%2==0) || (str[i]=='-' && count%2!=0))
				continue;
			else if((str[i]=='+' && count%2!=0)|| (str[i]=='-' && count%2==0))
			{
				count++;
			}
		}	
		
		myfile<<"Case #"<<j<<": "<<count<<endl;
	}
	return 0;
}
