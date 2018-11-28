#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <string>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <set>
#include <utility>
#include <vector>
#include <queue>

using namespace std;

typedef pair<int,int> PII;
typedef pair<int,PII> PIII;

#define LL long long
#define ULL unsigned long long
#define m_p make_pair
#define l_b lower_bound
#define p_b push_back
#define w1 first
#define w2 second
#define maxlongint 2147483647
#define biglongint 2139062143

int TT,N,sm;
char st[1005];

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	
	scanf("%d",&TT);
	for (int gb=1;gb<=TT;gb++)
	{
		scanf("%s",st);
		N=strlen(st);
		if (st[0]=='-') sm=1; else sm=0;
		for (int i=1;i<N;i++)
			if ((st[i]=='-')&&(st[i-1]=='+')) sm+=2;
		printf("Case #%d: %d\n",gb,sm);
	}
	
	return 0;
}
