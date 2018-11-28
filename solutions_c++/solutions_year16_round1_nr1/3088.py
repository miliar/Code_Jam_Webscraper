#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <cassert>
#include <queue>
#include <iostream>
using namespace std;

#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define lb(x) ((x)&(-(x)))
#define ms(x,y) memset(x,y,sizeof(x))
typedef vector<int> VI;
typedef long long ll;
typedef pair<int,int> PI;
const ll mod=1000000007;
const int inf=0x20202020;
const int N=505;
//head

char s[1005];
char ans[3005];
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int t,n;
	scanf("%d",&t);
	for(int ct=1;ct<=t;ct++) {
		scanf("%d\n",&n);
		scanf("%s",s);
		int len=strlen(s);
		int l=2000,r=2000;
		ans[2000]=s[0];
		for(int i=1;i<len;i++)
			if(s[i]>=ans[l])
				ans[--l]=s[i];
			else
				ans[++r]=s[i];
		printf("Case #%d: ",ct);
		for(int i=l;i<=r;i++)
			printf("%c",ans[i]);
		printf("\n");
	}
}

