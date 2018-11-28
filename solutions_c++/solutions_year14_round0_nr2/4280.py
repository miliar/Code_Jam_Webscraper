#include<stdio.h>

int main(){
    int t;
    double c,f,x, sec = 0, cookie = 2.0, direct, get_cookie;
    scanf("%d",&t);
    for(int j = 1; j <=t; j++){
        scanf("%lf%lf%lf",&c,&f,&x);
        direct = x/cookie;
        get_cookie = c/cookie + x/(cookie+f);
        while(get_cookie < direct){
            sec += c/cookie;
            cookie += f;
            direct = x/cookie;
            get_cookie = c/cookie + x/(cookie+f);
        }
        if(get_cookie >= direct)
            sec += x/cookie;
        printf("Case #%d: %lf\n",j,sec);
        sec=0;
        cookie = 2.0;
    }
    return 0;
}
