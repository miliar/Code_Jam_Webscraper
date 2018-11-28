#include<iostream>
#include<cstdio>
#include<fstream>

using namespace std;

int main(){

    int t, i, j;
    double c, x, f, temp, val, cok, min, re;
    scanf("%d",&t);

    for(i = 1; i<t; i++){

        temp = 0.0;
        val = -1.0;
        cok = 2.0;
        //num = 0.0;

        scanf("%lf%lf%lf",&c,&f,&x);
        val = x/2.0;
        temp = x;
        min = val;
        re = 0.0;
        for( ; temp>val; ){
            if(val<min)
                min = val;
            temp = val;
            re = re + c/cok;
            val = re + x/(cok+f);
            cok = cok+f;
        }
        printf("Case #%d: %.7lf\n",i,min);
    }
}
