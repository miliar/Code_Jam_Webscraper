#include<cstdio>
using namespace std;

int main(void){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int tc;
    int r,t,res,now, area;
    scanf("%d",&tc);
    for(int z=1;z<=tc;z++){
        scanf("%d %d",&r,&t);
        res = 0;
        area = 0;
        while(true){
            area = (r+1)*(r+1)-(r*r);
            t-=area;
            if(t<0)break;
            r+=2;
            res++;
        }
        printf("Case #%d: %d\n",z,res);
    }

}
