#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

const int MAXN = 10010;
int _;
int X,N;
int a[MAXN];

int main(){
    //freopen("in.txt","r",stdin);
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&_);
    int cas =0;
    while(_--){
        int cnt = 0;
        scanf("%d%d",&N,&X);
        for (int i=1;i<=N;i++) scanf("%d",&a[i]);
        sort(a+1,a+N+1);
        int l = 1;
        int r = N;
        while(l<r){
            if (a[l]+a[r]<=X){
                cnt ++;
                l++;
                r--;
            } else {
                cnt++;
                r--;
            }
        }
        if(l==r) cnt ++;
        printf("Case #%d: %d\n",++cas,cnt);
    }
}
