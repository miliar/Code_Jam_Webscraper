#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <iostream>
#include <fstream>
#include <map>
#include <utility>
#include <vector>
using namespace std;

int main(){

    int T;
    int A, B, C, ans;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&T);
    for(int t=1; t<=T; t++){
        scanf("%d%d%d",&A,&B,&C);
        ans = 0;
        //printf("A B and C is %d, %d, %d\n", A,B,C);
        for(int i=0; i<A; i++){
            for(int j=0; j<B; j++){
                    //printf()
                if( (i&j) < C) ans++ ;
            }
        }
        printf("Case #%d: %d\n",t,ans);
    }


return 0;
}

