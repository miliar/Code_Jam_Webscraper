#include<cstdio>
#include<cstring>
#include<string>
#include<cmath>
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
double eps = 1e-9;
int main()
{
    int tn, i, j, n;
    char in[105];
    freopen("gcbl.in", "r", stdin);
    freopen("gcbl.out", "w", stdout);
    scanf("%d", &tn);
    for(int tt = 1; tt<=tn;tt++){
        scanf("%s", in);
        n = strlen(in);
        int ret = 0;
        for(i=n-1;i>=0;i--){
            if(in[i] == '-'){
                n = i+1;
                in[n] = 0;
                ret = 1;
                break;
            }
        }
        for(i=0;i<n-1;i++){
            if(in[i] != in[i+1])
                ret++;
        }
        printf("Case #%d: %d\n",tt ,ret);
    }
}
