#include<iostream>
#include<cstdio>
#include<conio.h>
#include<algorithm>
using namespace std;

int main(){
    int t,x;
    scanf("%d", &t);
    x = t;
    while(t>0){
        int a,b,k;
        long long count =0;
        scanf("%d%d%d", &a, &b, &k);
        for(int i=0;i<a;i++){
            for(int j=0;j<b;j++){
                if(k> (i&j) ){
                    count++;
                }
            }
        }
        printf("Case #%d: %lld\n", x-t+1, count);   
        t--;
    }
    return 0;
}
