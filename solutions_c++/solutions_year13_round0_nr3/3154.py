#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
char cmd[20];
bool isP(long long p)
{
    sprintf(cmd,"%I64d",p);
    int len = strlen(cmd);
    for(int i = 0 , j = len -1 ; i < j ; i ++, j --)
    {
        if(cmd[i] != cmd[j]) return false;
    }
    return true;
}
int check(long long A, long long B)
{
    int ans = 0;
    for(int i = 1 ; 1LL * i * i <= B  ; i ++)
    {
        if(1LL * i * i < A ) continue;
        if(isP(1LL * i * i) && isP(i))
        {
            ans ++;
        }

    }
    return ans;
}
int main()
{
    freopen("C:/Users/v-y/Downloads/C-small-attempt0.in","r",stdin);
    freopen("C:/Users/v-y/Downloads/C-small-attempt0.out","w",stdout);
    int t, cas = 1;
    scanf("%d",&t);
    while(t--)
    {
        long long A , B;
        scanf("%I64d %I64d",&A,&B);
        int ans = check(A , B);
        printf("Case #%d: %d\n",cas++,ans);
    }
    return 0;
}
