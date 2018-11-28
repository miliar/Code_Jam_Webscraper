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

int f[10];
int main()
{
	int t,n;
	scanf("%d",&t);
	for(int ct=1;ct<=t;ct++) {
		scanf("%d",&n);
		if(n==0) {
			printf("Case #%d: INSOMNIA\n",ct);
			continue;
		}
		int ans,tmp;
		bool flag;
		memset(f,0,sizeof(f));
		for(int i=n;;i+=n) {
			ans=i;tmp=i;
			for(tmp=i;tmp;tmp/=10)
				f[tmp%10]=true;
			flag=true;
			for(int p=0;p<=9;p++)
				if(f[p]==false)
					flag=false;
			if(flag)break;
		}
		printf("Case #%d: %d\n",ct,ans);
	}


}

