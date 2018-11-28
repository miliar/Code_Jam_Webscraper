#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<string>
#include<cmath>
#include<vector>
#include<set>
#include<queue>
#include<map>
#include<stack>
#include<cstring>
#include<fstream>
#include<sstream>
using namespace std;
#define REP(i,N) for(int i=0;i<N;i++)
#define FOR(i,V,N) for(int i=V;i<N;i++)
#define PB(x) push_back(x)

// Global 

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int T;
	scanf("%d",&T);
	FOR(t,1,T+1)
	{
	
		int A,B,K;
		scanf("%d%d%d",&A,&B,&K);
		int res=0;
		REP(i,A)
		{
			REP(j,B)
			{
				int cur=i&j;
				if(cur<K)res++;
			}
		}
		printf("Case #%d: %d\n",t,res);
	}
	return 0;
}
