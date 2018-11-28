#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cstdio>
using namespace std;

int cal(int n)
{
    int rec[10];
    memset(rec,0, sizeof(rec));
    int times=1;
    int cnt=0;

    while(true){
        int cur = times * n;
        while(cur) {
            if (!rec[cur % 10]) ++cnt, rec[cur % 10]++;
            cur /= 10;
        }
        if(cnt==10) {
            break;
        }
        else{
            ++times;
        }
    }

    return times;
}


int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;cin>>T;int ca=0;
    while(T--)
    {
        int n;
        scanf("%d",&n);
        if(n==0) {
            printf("Case #%d: INSOMNIA\n",++ca);
            continue;
        }
        printf("Case #%d: %d\n",++ca,cal(n)*n);
    }
    return 0;
}