#include<cstdio>
#include<iostream>
#include<algorithm>
#define rep(i,n) for(int i=0;i<n;i++)
using namespace std;

int a[20],b[6][6];

int main(){
    freopen("test.inp","r",stdin);
    freopen("test.out","w",stdout);
    int st;
    scanf("%d",&st);
    rep(xxx,st){
        printf("Case #%d: ",xxx+1);
        int dem=0,res,x;
        rep(i,17) a[i]=0;
        scanf("%d",&x);
        x--;
        rep(i,4) rep(j,4) scanf("%d",&b[i][j]);
        rep(i,4) a[b[x][i]]++;
        scanf("%d",&x);
        x--;
        rep(i,4) rep(j,4) scanf("%d",&b[i][j]);
        rep(i,4) a[b[x][i]]++;
        rep(i,17) if (a[i]>1) dem++,res=i;
        if (dem>1) printf("Bad magician!\n");
        if (dem==0) printf("Volunteer cheated!\n");
        if (dem==1) printf("%d\n",res);
    }

}
