#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

char s[2000];

int main() {
    int n, T;
    freopen("A.txt", "r", stdin);
    freopen("A_out.txt", "w", stdout);
    scanf("%d",&T);
    for(int cs=1;cs<=T;cs++) {
           scanf("%d%s",&n,s);
           int sum = s[0]-'0';
           int ans = 0;
           for(int i=1;i<n+1;i++)  {
                   if( sum<i) {
                       int k = i-sum;
                       sum += k;
                       ans += k;
                   }
                   sum += s[i]-'0';
           }
           printf("Case #%d: %d\n",cs,  ans);
    }
}
