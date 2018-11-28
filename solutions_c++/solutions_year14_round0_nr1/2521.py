#include <iostream>
#include <cstdio>
#include <cstring>
#define maxn 1010
using namespace std;
int a[10][10],b[10][10];
int t,n,m;
int hashs[20];
int main (){
    //freopen("A-small-attempt1.in","r",stdin);
    //freopen("A-small-attempt1.out","w",stdout);
    scanf("%d",&t);
    for(int Case=1;Case<=t;++Case){
        scanf("%d",&n);
        memset(hashs,0,sizeof(hashs));
        for(int i=0;i<4;++i){
            for(int j=0;j<4;++j){
                scanf("%d",&a[i][j]);
                if(i==n-1)hashs[a[i][j]]++;
            }
        }
        scanf("%d",&m);
        int ans=-1;
        int cnt=0;
        for(int i=0;i<4;++i){
            for(int j=0;j<4;++j){
                scanf("%d",&b[i][j]);
                if(i==m-1){
                    if(hashs[b[i][j]]){
                        ans=b[i][j];
                        cnt++;
                    }
                }
            }
        }
        printf("Case #%d: ",Case);
        if(cnt==0)printf("Volunteer cheated!\n");
        else if(cnt==1)printf("%d\n",ans);
        else printf("Bad magician!\n");
    }
}
