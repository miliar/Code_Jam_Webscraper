#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cstring>

using namespace std;

int main(){
    freopen("inputD.in","r",stdin);
    freopen("outputD.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int co=1;co<=t;co++){
        int x,r,c;
        scanf("%d %d %d",&x,&r,&c);
        if(x>=7 || max(r,c)<x ||(x>=3 && (r==1 || c==1 || max(r,c)<(x+1)/2))||(r*c)%x!=0 || (x==4 && r==2 && c==4) || (x==4 && r==4 && c==2)){
            printf("Case #%d: RICHARD\n",co);
        }
        else{
            printf("Case #%d: GABRIEL\n",co);
        }
    }

}
