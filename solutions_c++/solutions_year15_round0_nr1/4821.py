/*
 * Author:  xtestw
 * Created Time:  2015/4/11 20:13:59
 * File Name: A.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <time.h>
using namespace std;
const int maxint = -1u>>1;
char str[1010];
int main() {
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int T;
    cin>>T;
    for(int ca=1;ca<=T;ca++)
    {
       int n;
       scanf("%d%s",&n,&str[0]);
       int ans=0;
       int cur=0;
       for(int i=0;i<=n;i++)
       {
           if(cur>=9) break;
            if(cur<i){
                ans+=(i-cur);
                cur=i;
            }
            cur+=str[i]-'0';
       }      
       printf("Case #%d: %d\n",ca,ans);
    }
    return 0;
}

