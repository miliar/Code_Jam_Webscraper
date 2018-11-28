#include<bits/stdc++.h>
using namespace std;

int main(){
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    string pos[3][13];
    int cr[3][13], cs[3][13], cp[3][13];
    pos[0][0]="P";
    cr[0][0]=cs[0][0]=0;
    cp[0][0]=1;
    pos[1][0]="R";
    cp[1][0]=cs[1][0]=0;
    cr[1][0]=1;
    pos[2][0]="S";
    cp[2][0]=cr[2][0]=0;
    cs[2][0]=1;
    int level=1;
    while(level<=12){
        pos[0][level]=pos[0][level-1]+pos[1][level-1];
        cp[0][level]=cp[0][level-1]+cp[1][level-1];
        cr[0][level]=cr[0][level-1]+cr[1][level-1];
        cs[0][level]=cs[0][level-1]+cs[1][level-1];
        pos[1][level]=pos[0][level-1]+pos[2][level-1];
        cp[1][level]=cp[0][level-1]+cp[2][level-1];
        cr[1][level]=cr[0][level-1]+cr[2][level-1];
        cs[1][level]=cs[0][level-1]+cs[2][level-1];
        pos[2][level]=pos[1][level-1]+pos[2][level-1];
        cp[2][level]=cp[1][level-1]+cp[2][level-1];
        cr[2][level]=cr[1][level-1]+cr[2][level-1];
        cs[2][level]=cs[1][level-1]+cs[2][level-1];
        //cout<<pos[0][level]<<endl<<pos[1][level]<<endl<<pos[2][level]<<endl;
        level++;
    }
    int cases,i,t,n,r,p,s,res;
    scanf("%d",&cases);
    for(t=1;t<=cases;t++){
        scanf("%d %d %d %d",&n,&r,&p,&s);
        res=-1;
        if(cp[0][n]==p&&cr[0][n]==r&&cs[0][n]==s)res=0;
        if(cp[1][n]==p&&cr[1][n]==r&&cs[1][n]==s)res=1;
        if(cp[2][n]==p&&cr[2][n]==r&&cs[2][n]==s)res=2;
        printf("Case #%d: ",t);
        if(res==-1){
            printf("IMPOSSIBLE\n");
        }
        else{
            cout<<pos[res][n]<<endl;
        }
    }
    return 0;
}
