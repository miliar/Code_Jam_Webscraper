#include<cstdio>
#include<cmath>

int z, i;
long long int r, t, tmp, circleIn, circleOut, wynik;

int main(){
    scanf("%d", &z); 
    i = 0;
    while(z--){
        i++;
        wynik = 0;
        scanf("%lld %lld", &r, &t);
        while(true){
            circleIn = r*r;
            r++;
            circleOut = r*r;
            r++;
            tmp = circleOut - circleIn;
            t -= tmp;
            if(t >= 0){
                wynik++;
            }else{
                break;
            }
        }
        printf("Case #%d: %lld\n", i, wynik);
    }
}
