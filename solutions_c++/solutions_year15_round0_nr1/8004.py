#include<bits/stdc++.h>

#define long long ll
using namespace std;

int main()
{
    freopen("in","r",stdin);
    freopen("out","w",stdout);

    int test;
    scanf("%d",&test);

    for(int t=1;t<=test;t++)
    {
        int n;
        char people[1050];
        scanf("%d",&n);

        scanf("%s",people);
        int l=strlen(people);

        int pcount=0;
        int extra=0;
        int e_sum=0;
        for(int i=0;i<l;i++)
        {
            if(pcount>=i)
            {
                pcount+=(people[i]-48);
            }
            else
            {
                extra=(i-pcount);
                e_sum+=extra;
                pcount+=extra;
                pcount+=(people[i]-48);
            }
        }

        printf("Case #%d: %d\n",t,e_sum);
    }

    return 0;
}
