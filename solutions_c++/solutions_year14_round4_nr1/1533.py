#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<string>
#include<queue>
#include<set>
#include<map>
#include<iostream>
#include<cmath>
using namespace std;
#define mem(a,b) memset(a,b,sizeof(a))
#define pb push_back
typedef long long ll;

const int N = 11000;

int a[N];

int main()
{
	int T; scanf("%d",&T);
	for(int ka=1;ka<=T;ka++) {
        int x;
        int n;
        scanf("%d%d",&n,&x);
        for(int i=0;i<n;i++) scanf("%d",&a[i]);
        sort(a,a+n);
        int r=n-1;
        int cnt=0;
        for(int i=0;i<n;i++) {
            if(a[i]<0) continue;
            cnt++;
            while(i<r && a[r]+a[i]>x) r--;
            if(i<r) a[r]=-1,r--;
        }
        printf("Case #%d: %d\n",ka,cnt);
	}

    return 0;
}
