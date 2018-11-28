#include<iostream>
#include<vector>
#include<math.h>
#include<climits>
using namespace std;

void check(unsigned long long num, int &unique,bool &flag,bool count[]) {
    int digit = 0;
    while(num!=0) {
        digit = num % 10;
        if(count[digit] == 0) {
            count[digit] = 1;
            unique++;
            if(unique == 10) {
                flag = true;
                break;
            }
        }
        num/=10;
    }
}

int main() {

    freopen("A-large.in","rt",stdin);
    freopen("output.txt","wt",stdout); 
     bool flag = false;
    int unique = 0;
    int test,n;
    unsigned long long i = 0;
    scanf("%d",&test);
    for(int j=1;j<=test;j++) {
        scanf("%d",&n);
        bool count[10] = {0};
        unsigned long long max_limit = ULONG_MAX;
        unique = 0;
        flag = false;
        if(n!=0) {
           
           for(i=1;i<max_limit;i++) {
                check(i*n,unique,flag,count);
                if(flag) break;
           }    
        }
           printf("Case #%d: ",j);
           if(i==max_limit || !flag) {
              printf("INSOMNIA");
           } else {
              printf("%llu",i*n);
           }
        printf("\n");
    }
    return 0;
}
