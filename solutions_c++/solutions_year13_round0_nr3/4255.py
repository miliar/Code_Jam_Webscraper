#include<cstdio>
#include<algorithm>
#include<string>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<cstdio>
#include<cassert>
#include<iostream>
#include<queue>
#include<map>
#include<set>
#include<vector>
#include<ctime>

using namespace std;

#define MEM(a,b) memset(a,(b),sizeof(a))
#define MAX(a,b)  ((a) > (b) ? (a) : (b))
#define MIN(a,b)  ((a) < (b) ? (a) : (b))

#define MP make_pair
#define pb push_back
#define inf  1000000000
#define maxn 100001
#define maxc 100001
#define MP make_pair

//typedef long long LL;
typedef pair<int,int> pi;
typedef pair<pi,pi> pii;
typedef __int64 LL;


int ispal(LL n)
{
	char str[30];
	sprintf(str,"%I64d",n);
	int l=strlen(str);

	for(int i=0;i<l/2;i++)
		if(str[i]!=str[l-i-1]) return 0;
	return 1;
}



string numTostr(LL n)
{
	char str[30];
	sprintf(str,"%lld",n);
	return (string)str;
}

bool comp(string A,string B)
{
	if(A.size()==B.size())
		return A<B;
	return A.size()<B.size();
}

int main()
{
	int i,j,k,tests,cs=0,n,m,L;
	string s;
	vector<LL> all;
	

	for(i=1;i<10000;i++)
	{
		int x=i;
		LL v=i,p=1,u=i;

		while(x)
		{
			v=  v*10+(x%10);
			if(p>1) u=u*10+(x%10);
			p*=10;
			x/=10;
		}

		if(ispal(v*v)) all.push_back(v);
		if(ispal(u*u)) all.push_back(u);
		//printf("%d %lld %lld\n",i,u,v);
	}

	sort(all.begin(),all.end());


	freopen("C-large-1.in","r",stdin);
	freopen("C-large-1.out","w",stdout);
	scanf("%d",&tests);

	while(tests--)
	{	
		LL a,b;
		int ans=0;
		scanf("%I64d%I64d",&a,&b);

		for(i=0;i<all.size();i++)
		{
			if(all[i]*all[i]>=a && all[i]*all[i]<=b) ans++;
			if(all[i]*all[i]>b) break;
		}

		printf("Case #%d: %d\n",++cs,ans);
	}

	return 0;
} 
