#include<stdio.h>
#include<map>
#include<queue>
#include<string>
#include<stdlib.h>
#include<iostream>
#include<string.h>
#include<vector>
#include<algorithm>
using namespace std;
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define CLR(s) memset(s,0,sizeof(s))
typedef long long LL;
#define PB push_back

int n,m,a[10][10],b[10][10];
int occ[20];
int main(){
    int ca; scanf("%d",&ca);
    FOE(tt,1,ca){
        scanf("%d",&n);
        CLR(occ);
        FOR(i,0,4) FOR(j,0,4){
            scanf("%d",&a[i][j]);
            if (i==n-1) occ[a[i][j]]++;
        }
        scanf("%d",&m);
        FOR(i,0,4) FOR(j,0,4){
            scanf("%d",&b[i][j]);
            if (i==m-1) occ[b[i][j]]++;
        }
        int nans=0, ans=-1;
        FOR(i,1,17){
            if (occ[i]==2){
                ans=i;
                nans++;
            }
        }
        if (nans==1) printf("Case #%d: %d\n", tt, ans);
        else if (nans>1) printf("Case #%d: Bad magician!\n", tt);
        else printf("Case #%d: Volunteer cheated!\n", tt);
    }
    return 0;
}
