//   <-- Y.L.Asce -->   //
#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;
int t;
int Smax;
char S[2000];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    scanf("%d",&t);
    for(int cas = 1;cas <= t;cas++)
    {
        scanf("%d",&Smax);
        scanf("%s",S);
        int sum = 0,ans = 0;
        for(int i=0;i<Smax;i++)
        {
            sum += S[i]-'0';
            if(S[i+1] > '0' && sum < i+1)
            {
                ans += i+1-sum;
                sum = i+1;
            }
        }
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
