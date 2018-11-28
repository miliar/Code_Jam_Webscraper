#include <cstdio>
#include <iostream>
#include <algorithm>
#define N 1100
#define M (1 << 29) 
#define Max(a, b) ((a) > (b) ? (a) : (b))
#define Min(a, b) ((a) > (b) ? (b) : (a))
using namespace std;

int a[N], sum[N];
int d;

int main(){
    int t;
    scanf("%d", &t);
    for(int di = 1; di <= t; di++){
        scanf("%d", &d);
        for(int i = 0; i < d; i++)
            scanf("%d", &a[i]);
        sort(a, a + d);
        int ans = M;
        for(int i = a[d - 1]; i >= 1; i--){
            int temp = i, k;
            //cerr <<"i = "<< i << endl;
            for(int j = d - 1; j >= 0; j--){
                if(a[j] <= i) k = 0;
                else k = (a[j] % i) ? a[j] / i : (a[j] / i - 1); 
                temp += k;
                //cerr <<"k = "<< k << endl;
            }
            ans = Min(ans, temp);
        }
        printf("Case #%d: %d\n", di, ans);
    }
    return 0;
}

