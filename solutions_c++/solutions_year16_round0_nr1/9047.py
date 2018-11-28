#include <bits/stdc++.h>

using namespace std;

int main(){

    freopen("in.c","r",stdin);
    freopen("out.c","w",stdout);

    int TC;
    int NC = 0;
    cin>>TC;

    while(TC--){
        NC++;
        long long n;
        cin>>n;

        long long answer = -1;

        if(n == 0){
            printf("Case #%d: INSOMNIA\n" , NC);
        }else{
            int ind  = 1;
            int mask = 0;

            while(1){
                long long newVal = n*ind;

                while(newVal>0){
                    int dig = newVal%10;
                    newVal/=10;
                    mask|=(1LL<<dig);
                }

                if(mask == ((1LL<<10) - 1) )  break;
                ind++;
            }
            answer = ind*n;
            printf("Case #%d: %lld\n" , NC , answer);
        }



    }




    return 0;
}
