#include<bits/stdc++.h>
using namespace std;
typedef long long int LL;
int main()
{
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        int smax;
        char str[10005];
        scanf("%d",&smax);
        scanf("%s",str);
        int l=smax+1;
        int cnt=0,p=0;
        for(int i=0;i<l;i++)
        {
            int x=str[i]-'0';
            if(p<i && x!=0)
            {
                cnt+=i-p;
                p=i;
            }
                p+=x;
        }
        printf("Case #%d: %d\n",t,cnt);
    }
    return 0;
}
