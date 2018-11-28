#include    <iostream>
#include    <stdio.h>
#include    <vector>
#include    <algorithm>
#include    <stack>
#include    <string.h>
#include    <math.h>
#include    <set>
#include    <map>
#include    <utility>

#define     li              long int
#define     ll              long long int
#define     vi              vector<int>
#define     vii             vector<pair<int,int> >
#define     pii             pair<int,int>
#define     vl              vector<ll>
#define     vll             vector<pair<ll,ll> >
#define     pll             pair<ll,ll>
#define     pli             pair<ll,int>
#define     mp              make_pair
#define     TC()            int t;scanf("%d",&t);while(t--)
#define     REP(i,a,b)      for(i=a;i<b;i++)
#define     REPREV(i,b,a)   for(i=b;i>=a;i--)
#define     INP(x)          scanf("%d",&x)
#define     OUT(x)          printf("%d\n",x)
#define     INPLL(x)        scanf("%lld",&x)
#define     OUTLL(x)        printf("%lld\n",x)
#define     INPS(x)         scanf("%s",x)
#define     OUTS(x)         printf("%s\n",x)
#define     trace1(x)       cout <<#x<<" = "<<x<<endl;
#define     trace2(x, y)    cout <<#x<<" = "<<x<<" & "<<#y<<" = "<<y<< endl;
#define     ENDL            printf("\n")
#define     MOD             1000000007
#define     N               100005

using namespace std;

int main()
{
	int t,i,j,k;
	string s;

	cin>>t;
	for(k=1;k<=t;k++)
	{
		int cntm=0,cntp=0;
		cin>>s;

		for(i=0;i<s.length();i++)
		{
			if(s[i]=='-')
				cntm++;
			if(s[i]=='+')
				cntp++;

		}

		if(cntm==s.length()){
			printf("Case #%d: %d\n",k,1);
			continue;
		}
		if(cntp==s.length())
		{
			printf("Case #%d: %d\n",k,0);
			continue;
		}

		int cnt=0,f=0;
		for(i=1;i<s.length();i++)
		{
			if(s[i-1]=='-' && s[i]=='+' && f==0)
				cnt++,f=1;
			else if(s[i-1]=='+' && s[i]=='-')
				cnt+=2,f=1;
		}

		printf("Case #%d: %d\n",k,cnt);
	}
	return 0;
}
