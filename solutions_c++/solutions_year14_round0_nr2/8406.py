#include<iostream>
#include<stdio.h>

using namespace std;
typedef long double ld;

int main(){


    ld t,c,f,x;
    int tc;
tc  =0;
    cin>>t;

    while(t--){

        cin>>c>>f>>x;

        ld i,ans;
        ans = x/2;

        for(i=1;i<100000000;i++)
            if( ans - x/(2 + f*(i-1) ) + x/(2 + f*i) + c /(2 + f*(i-1)) < ans)
                ans = ans - x/(2 + f*(i-1) ) + x/(2 + f*i) + c /(2 + f*(i-1))  ;

        printf("Case #%d: %.9llf\n",++tc,ans);
    }


}
