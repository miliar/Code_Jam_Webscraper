#include <cstdio>
#include <queue>
#include <stack>
#include <iostream>
#include <limits.h>
#include <cstring>
#include <map>
#include <string>
#include <vector>
using namespace std;
#define MAXN 10000
#define INF INT_MAX //nao ha perigo de overflow


int main(){
    int a,b,k,count,t;

    scanf("%d", &t);
    for(int p = 0;p<t;p++){
        count = 0;
        scanf("%d %d %d", &a, &b, &k);
        for(int i = 0;i<a;i++){
            for(int j = 0;j<b;j++){
                if( (i&j) < k) count++;
            }
        }
        printf("Case #%d: %d\n", p+1, count);

    }


    return 0;
}