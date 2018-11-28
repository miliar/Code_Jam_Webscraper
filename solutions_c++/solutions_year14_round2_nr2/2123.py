#include<iostream>
using namespace std;
int k,t;
int a , b ;
int main(){
    scanf("%d",&t);
    int counter =1;
    while (t--) {
        int res =0;
        scanf("%d %d %d",&a,&b,&k);
        for (int i =0; i<a; i++) {
            for (int j =0 ; j<b; j++) {
                if ((i&j)<k) {
                    res++;
                }
            }
        }
        printf("Case #%d: %d\n",counter,res);
        counter++;
    }
    return 0;
}