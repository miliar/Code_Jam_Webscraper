#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> PII;
typedef long long LL;
typedef long double LD;
const LL INF=1ll<<60, MaxN=1<<21;
const LD eps=1e-8;

int n,m;
int a[5][5],b[5][5];

int main(){
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);
    int t,cas=0;
    scanf("%d",&t);
    while (t--){
        scanf("%d",&n);
        for (int i=1; i<=4; i++)
            for (int j=1; j<=4; j++) scanf("%d",&a[i][j]);
        scanf("%d",&m);
        for (int i=1; i<=4; i++)
            for (int j=1; j<=4; j++) scanf("%d",&b[i][j]);
        int cnt=0, w=0;
        for (int i=1; i<=4; i++)
            for (int j=1; j<=4; j++)
                if (a[n][i]==b[m][j]) cnt++, w=a[n][i];
        printf("Case #%d: ",++cas);
        if (cnt==1) printf("%d\n",w);
        if (cnt==0) puts("Volunteer cheated!");
        if (cnt>=2) puts("Bad magician!");
    }
    return 0;
}
