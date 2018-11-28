#include<cstdio>
#include<algorithm>
using namespace std;
char M[10000];
int main(){
    int cas,t=0;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&cas);
    while(cas--){

        bool flag=true;
        int x,r,c;
        scanf("%d%d%d",&x,&r,&c);
        //if((r*c)%x || x<=2) continue;
        if(r>c)
            swap(r,c);
        //printf("%d %d %d ",x,r,c);
        if( r < (x+1)/2 )
            flag=false;
        else if((r*c)%x)
            flag=false;
        else if(x>=7)
            flag=false;
        else if(x>c)
            flag=false;
        else if(x>=r+2)
            flag=false;


        if(flag)
           printf("Case #%d: GABRIEL\n",++t);
        else
            printf("Case #%d: RICHARD\n",++t);
    }
    return 0;
}

