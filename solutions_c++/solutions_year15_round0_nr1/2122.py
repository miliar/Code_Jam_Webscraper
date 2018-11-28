#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

int main(){
    int T;
    char a[1001];
    int sMax;
    scanf("%d",&T);
    for(int t=0;t++<T;){
        scanf("%d%s", &sMax, a);
        int f = 0;
        int standing = 0;
        for(int i = 0; i < sMax+1; ++i){
            if(f+standing<i)
                f = i-standing;
            standing += a[i]-48;
        }
        printf("Case #%d: %d\n", t, f);
    }
    return 0;
}
