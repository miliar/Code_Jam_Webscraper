#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#define ll long long
using namespace std;
const int N=100+5;
char str[N];
int main()
{
/*#ifndef ONLINE_JUDGE
    freopen("B-large.in","r",stdin);
    freopen("out.txt", "w",stdout);
#endif*/
    int T;cin>>T;
    for(int ca=1;ca<=T;ca++){
        scanf("%s",str);
        int n=strlen(str);
        int ip=n-1;
        int ans=0;
        while(ip>=0)
        {
            if(str[ip]=='+'){
                ip--;
                continue;
            }
            ans++;
            for(int i=ip;i>=0;i--){
                if(str[i]=='+')str[i]='-';
                else str[i]='+';
            }
            ip--;
        }
        printf("Case #%d: %d\n",ca,ans);
    }
    return 0;
}
