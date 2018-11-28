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

int TT,N,flag,ee;
int cnt[12];

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	
	scanf("%d",&TT);
	for (int gb=1;gb<=TT;gb++)
	{
		scanf("%d",&N);
		memset(cnt,0,sizeof(cnt));
		printf("Case #%d: ",gb);
		flag=1;
		for (int i=1;i<=1000000;i++)
		{
			LL sc=(LL)N*i;
			while (sc>0)
			{
				cnt[sc%10]=1;
				sc/=10;
			}
			ee=0;
			for (int j=0;j<=9;j++) ee+=cnt[j];
			if (ee==10) 
			{
				printf("%lld\n",(LL)N*i);
				flag=0;
				break;
			}
		}
		if (flag==1) printf("INSOMNIA\n");
	}
	
	return 0;
}
