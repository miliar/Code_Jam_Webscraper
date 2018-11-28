#include<iostream>
#include<fstream>
#include<stdio.h>
#include<cstdio>
#include<stdlib.h>
#include<string>
#include<string.h>
#include<ctype.h>
#include<algorithm>
#include<cmath>
#include<set>
#include<queue>
#include<stack>
#include<iomanip>
#include<vector>
#include<map>
#define PB(x) push_back(x)
#define MP(x, y) make_pair(x, y)
#define ff first
#define ss second
#define ll long long
#define pii pair< int, int >
#define MEM(p, v) memset(p, v, sizeof(p))
#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)
#define S system("pause")
#define R return(0)
#define INF int(1e9)
#define MAX_5 int(1e5+5)
#define MAX_6 int(1e6+6)
#define ll long long
#define tree int h,int l1,int r1
#define left 2*h,l1,(l1+r1)/2
#define right 2*h+1,(l1+r1)/2+1,r1
using namespace std;
ll n,k,ans;
string s;
main()
{
	READ("a.in");
	WRITE("go.out");
int t;
cin>>t;
for(int o=1;o<=t;o++)
{
	cin>>n>>s;
	k=s[0]-'0';
	ans=0;
	for(int i=1;i<s.size();i++)
	{
		if(i<=k)k+=s[i]-'0';else
			ans+=i-k,k+=s[i]-'0'+i-k;
	}
	cout<<"Case #"<<o<<": "<<ans<<endl;
}
}
