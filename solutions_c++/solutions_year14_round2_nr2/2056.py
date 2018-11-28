#include<iostream>
using namespace std;
long long int q,t;
long long int a , b ;
long long int main(){
    scanf("%lld",&t);
    long long int counter =1;
    while (t--) {
        int res =0;
        scanf("%lld %lld %lld",&a,&b,&q);
        for (long long int i =0; i<a; i++) {
            for (long long int j =0 ; j<b; j++) {
                if ((i&j)<q) {
                    res++;
                }
            }
        }
        printf("Case #%lld: %d\n",counter,res);
        counter++;
    }
    return 0;
}