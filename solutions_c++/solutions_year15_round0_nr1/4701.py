#include<map>
#include<set>
#include<vector>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>

using namespace std;
const int N = 1006;

char digit[N];
int main()
{
    int T,CAS,n=0;

    //freopen("data.in","r",stdin);
    //freopen("data.out","w",stdout);
    scanf("%d",&T);
    for(CAS=1;CAS<=T;CAS++)
    {
        scanf("%d %s",&n,digit);
        int sum=0,ans=0;
        for(int i=0;digit[i];i++)
        {
            if(i>sum)
            {
                ans+=i-sum;
                sum=i;
            }
            sum+=digit[i]-'0';
            if(sum>=9) break;
        }
        printf("Case #%d: %d\n",CAS,ans);
    }
    return 0;
}
