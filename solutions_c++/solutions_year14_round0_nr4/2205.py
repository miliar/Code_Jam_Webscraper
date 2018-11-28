#include<stdio.h>
#include<algorithm>
using namespace std;
int T,N;
double a[1010],b[1010];

int wins() {
    int x=1,y=1;
    int w = 0;
    while(x<=N && y<=N) {
        while(a[x]>b[y] && y<=N) {
            ++y;
        }
        if(y<=N) {
            ++w;
            ++x;
            ++y;
        }
    }
    return N-w;
}

int cheat() {
    int x=1,y=1;
    int w = 0;
    while(x<=N && y<=N) {
        while(a[x]<b[y] && x<=N) {
            ++x;
        }
        if(x<=N) {
            ++w;
            ++x;
            ++y;
        }
    }
    return w;
}
int main() {
    freopen("war.in","r",stdin);
    freopen("war.out","w",stdout);
    scanf("%d",&T);
    for(int t=1;t<=T;++t) {
        printf("Case #%d: ",t);
        scanf("%d",&N);
        for(int i=1;i<=N;++i) {
            scanf("%lf",&a[i]);
        }
        sort(a+1,a+N+1);
        for(int i=1;i<=N;++i) {
            scanf("%lf",&b[i]);
        }
        sort(b+1,b+N+1);
        printf("%d %d\n",cheat(),wins());
    }
}
