#include<cstdio>
#include<algorithm>
using namespace std;
const int MAXN = 12;
int tc,n,cnt[MAXN+5][4][4],a[4];
char arr[5005];
char pr[4]="PRS";

void ans(int s, int e, int win) {
    if(s==e) arr[s] = pr[win];
    else {
        ans(s,(s+e)/2,win);
        ans((s+e)/2+1,e,(win+1)%3);
        int i; bool flag = false;
        for(i=s;i<=(s+e)/2;i++) {
            if(arr[(s+e)/2+1-s+i]<arr[i]) {
                flag = true; break;
            }
            if(arr[(s+e)/2+1-s+i]>arr[i]) break;
        }
        if(flag) {
            for(i=s;i<=(s+e)/2;i++) {
                swap(arr[i],arr[(s+e)/2+1-s+i]);
            }
        }
    }
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int i,j,k,q;
    for(i=0;i<3;i++) {
        for(j=0;j<3;j++) {
            cnt[0][i][j] = (i==j);
        }
    }
    for(i=1;i<=MAXN;i++) {
        for(j=0;j<3;j++) {
            for(k=0;k<3;k++) {
                cnt[i][j][k] += cnt[i-1][j][k]+cnt[i-1][(j+1)%3][k];
            }
        }
    }
    scanf("%d",&tc);
    for(q=1;q<=tc;q++) {
        scanf("%d%d%d%d",&n,&a[1],&a[0],&a[2]);
        printf("Case #%d: ",q);
        for(i=0;i<5000;i++) arr[i] = 0;
        bool flag;
        for(i=0;i<3;i++) {
            flag = true;
            for(j=0;j<3;j++) {
                if(cnt[n][i][j]!=a[j]) flag = false;
            }
            if(flag) {
                ans(0,(1<<n)-1,i);
                printf("%s\n",arr);
                break;
            }
        }
        if(!flag) puts("IMPOSSIBLE");
    }
}
