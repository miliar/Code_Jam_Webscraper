#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
char a[10005];
int main()
{
    ll t,n,p,i,j,r,c=1;

    freopen("A-large (3).in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%lld",&t);
    while(t--)
    {
        scanf("%s",&a);
        deque<char> dq;
        printf("Case #%d: ",c++);
        n=strlen(a);
        for(i=0;i<n;i++)
        {
            if(i==0)
            {
                dq.push_back(a[i]);
            }
            else
            {
                if(a[i]>=dq.front())
                {
                    dq.push_front(a[i]);
                }
                else
                {
                    dq.push_back(a[i]);
                }
            }
        }
        for(i=0;i<n;i++)
        {
            printf("%c",dq[i]);
        }
        printf("\n");

    }
    return 0;
}
