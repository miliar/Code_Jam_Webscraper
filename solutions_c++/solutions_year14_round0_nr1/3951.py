#include <bits/stdc++.h>
using namespace std;

int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int test;
    int cases=0;
    for(scanf("%d",&test);test>0;--test){
        int a,b;
        int A[10][10],B[10][10];
        scanf("%d",&a);
        for(int i=1;i<=4;++i) for(int j=1;j<=4;++j) scanf("%d",&A[i][j]);
        scanf("%d",&b);
        for(int i=1;i<=4;++i) for(int j=1;j<=4;++j) scanf("%d",&B[i][j]);
        int cnt=0;
        int t;
        for(int i=1;i<=4;++i) for(int j=1;j<=4;++j) if(A[a][i]==B[b][j]){ t=A[a][i]; ++cnt;}
        if(cnt==1) printf("Case #%d: %d\n",++cases,t);
        else if(cnt==0) printf("Case #%d: Volunteer cheated!\n",++cases);
        else printf("Case #%d: Bad magician!\n",++cases);
    }
    return 0;
}
