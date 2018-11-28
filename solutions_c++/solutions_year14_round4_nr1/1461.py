#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
typedef long long ll;
const int M=10005;
int n,x;
int s[M];
bool vis[M];

int main() {
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int cas=1,t;
    for(scanf("%d",&t);cas<=t;cas++) {
        memset(vis,0,sizeof(vis));
        scanf("%d %d",&n,&x);
        for(int i=0;i<n;i++) {
            scanf("%d",&s[i]);
        }
        sort(s,s+n);
        int l=0,r=n-1,res=0;
        while(l<r) {
            if(s[l]+s[r]<=x) {
                res++;
                l++;
                r--;
            }
            else {
                res++;
                r--;
            }
        }
        if(l==r) res++;
        printf("Case #%d: %d\n",cas,res);
    }
    return 0;    
}