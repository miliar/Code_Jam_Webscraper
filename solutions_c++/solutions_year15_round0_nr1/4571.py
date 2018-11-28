#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<utility>
#include<cstring>
#include<cmath>
#define LL long long int
#define mod 1000000007
#define vi vector<int>
#define vvi vector < vi >
#define pii pair<int,int>
#define all(c) c.begin(),c.end()
#define sf(x) scanf("%d",&x);
#define sf2(x,y) scanf("%d%d",&x,&y);
#define mem(a,val) memset(a,val,sizeof(a))
#define nl printf("\n");
#define pb push_back
#define mp make_pair
#define f first
#define s second
using namespace std;
int main()
{	freopen("googleinput.txt","r",stdin);
    freopen("googleoutput.txt","w",stdout);
	int t,i,j,tst,ans,cnt;
	sf(t);
	char str[2005];
	for(tst=1;tst<=t;tst++)
	{	int smax;
		sf(smax);
		scanf("\n");
		gets(str);
		cnt=0;ans=0;
		for(i=0;i<=smax;i++)
		{	if(cnt<i)
			{	ans++;
				cnt++;
			}
			cnt+=str[i]-'0';
		}
		printf("Case #%d: %d\n",tst,ans);
	}
	return 0;
}


