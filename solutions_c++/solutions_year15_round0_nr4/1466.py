#include <cstdio>
using namespace std;

int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int test;
    int cases=0;
    for(scanf("%d",&test);test>0;--test){
        int x,r,c;
        bool valid = true;
        scanf("%d%d%d",&x,&r,&c);
        if(r*c%x || r*c<x) valid=false;
        if(x==3 && (r==1 || c==1)) valid=false;
        if(x==4 && (r<3 || c<3)) valid=false;
        if(valid) printf("Case #%d: GABRIEL\n",++cases);
        else printf("Case #%d: RICHARD\n",++cases);
    }
    return 0;
}
