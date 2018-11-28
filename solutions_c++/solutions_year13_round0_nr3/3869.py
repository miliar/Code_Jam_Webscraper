#include <cstdio>
#include <cmath>


int n;

int isPalindrome(long long a){
    long long w = a;

    long long start;
    if(w>10){
        start    = pow(10,floor(log10(w)));
    } else return 1;
    while(w>9 && w%10==w/start){
        w-=w/start*start;
        w/=10;
        start/=100;
    }
    return w<10;
}
bool t[1000000];

void alg(int testcase){
    int a,b, w= 0;
    scanf("%d%d", &a, &b);
    for(int i=a; i<=b; i++){
        if(t[i]){
            w++;
        }
    }

    printf("Case #%d: %d\n", testcase, w);
}

int main(){
       scanf("%d", &n);
       for(int i=1; i<1000; i++){
           if(isPalindrome(i) && isPalindrome(i*i)){
                t[i*i] = 1;
           }
       }
    for(int __i=1; __i<=n; __i++){
        alg(__i);
   }
}
