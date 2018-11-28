#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cstdio>
using namespace std;
int m[10002];

void process(){
    int n, i;
    long long int max=0;
    scanf("%d", &n);
    
    for(i=0;i<n;i++){
        scanf("%d", &m[i]);
        if (i){
            if (m[i-1]-m[i]>max){
                max = m[i-1]-m[i];
            }
        }
    }

    long long int ans = 0;
    for (i=1; i<n;i++){
        ans+=  m[i-1]-m[i] >0? m[i-1]-m[i]:0;
    }
    printf("%lld ", ans);
    
    ans=0;
    for (i=0; i<n-1;i++){
        if (m[i]>=max){
            ans+=max;
        }else{
            ans+=m[i];
        }
    }

    printf("%lld\n", ans);
}

int main(){
    int t, i;
    scanf("%d", &t);
    for (i = 1; i <= t; ++i)
    {
        printf("Case #%d: ", i);
        process();
    }
    return 0;
}