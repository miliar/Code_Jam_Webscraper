#include<cstdio>
#define REP(n,i) for(int i=0;i<n;i++)
int a[4][4];
int b[4][4];
int tmp;
int calc(int ar,int br){
    int ans=0;
    REP(4,i)REP(4,j){
        if(a[ar][i]==b[br][j]){
            ans++;
            tmp=a[ar][i];
        }
        
    }
    return ans;
}
int main(){
    int t,c=0;
    
    freopen("A-small-attempt0.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&t);
    while(c++<t){
        int x,y;
        scanf("%d",&x);
        REP(4,i)REP(4,j)scanf("%d",&a[i][j]);
        scanf("%d",&y);
        REP(4,i)REP(4,j)scanf("%d",&b[i][j]);
        int ans=calc(x-1,y-1);
        //printf("ans %d\n",ans);
        printf("Case #%d: ",c);
        if(ans==0)puts("Volunteer cheated!");
        else if(ans==1)printf("%d\n",tmp);
        else puts("Bad magician!");
    }
    return 0;
}
