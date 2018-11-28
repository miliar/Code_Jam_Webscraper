#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <queue>
#include <iostream>
using namespace std;
int main(){
    int t;
    int teste=0;
    scanf("%d", &t);
    for(int p=0;p<t;p++){
        teste++;
        int k, c, s;
        scanf("%d %d %d", &k, &c, &s);
        long long int block = pow(k, c-1);
         /*for(int i=0;i<s;i++){
            printf("%lf\n",pow(k, c-1)*i+1);
            //n.push( (long long int)(pow(k, c-1)*i+1 ) );
        }*/
        printf("Case #%d: ", teste);
        /*for(int i=0;i<s;i++){
            printf(" %lld", n.front());
            n.pop();
        }*/
        for(int i=0;i<s;i++){
            cout<<(block*i+1)<<" ";
            //n.push( (long long int)(pow(k, c-1)*i+1 ) );
        }
         cout<<endl;
    }
    return 0;
}
