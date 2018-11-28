#include <iostream>
#include<cstdio>
#include<cstring>
using namespace std;
char S[1010];
int A[1010];
int main()
{
    //freopen("A-small-attempt0","r",stdin);
    freopen("Qdata.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int kase=1;kase<=T;kase++)
    {
        int ms;
        scanf("%d",&ms);
        scanf("%s",S);
        memset(A,0,sizeof(A));
        int cnt=0,res=0;
        for(int i=0;i<=ms;i++)
        {
            if(cnt>=i)
            {
                cnt+=S[i]-'0';
            }
            else
            {
                res+=(i-cnt);
                cnt=i+S[i]-'0';
            }
        }
        printf("Case #%d: %d\n",kase,res);
    }
    return 0;
}
