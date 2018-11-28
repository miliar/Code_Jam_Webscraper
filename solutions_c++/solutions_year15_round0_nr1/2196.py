#include <iostream>
#include <iomanip>
#include <fstream>
#include <stdlib.h>
#include <time.h>
#include<cstring>
#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>
#include <limits.h>
#include<cmath>
#include<map>
#include<queue>
#include<set>
using namespace std;


#define LL long long

const long long  mod =1000000009;  //这个必须是质数

int main()
{
    int T;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    int t=T;
    while (T--){
        int n;
        scanf("%d",&n);
        char z[5555];
        scanf("%s",z);
        int ans=0;
        int now=0;
        while (n>=0 && z[n]=='0') n--;
        for (int j=0;j<=n;j++){
            if (now>=j) {
                now+=z[j]-'0';
                continue;
            }
            ans+=j-now;
            now=j+z[j]-'0';
        }
        printf("Case #%d: %d\n",t-T,ans);
    }
    return 0;
}

