#include<bits/stdc++.h>
using namespace std;
int main ()
{
    int T;
    freopen("A-large.in","r",stdin);
    freopen("out3.txt","w",stdout);
    cin>>T;
    for(int q=1; q<=T; q++)
    {
        int sz;
        scanf("%d",&sz);
        char a[sz+2];
        scanf("%s",a);
        int sum=0;
        int n=0;
        for(int i=0; i<=sz; i++)
        {
            sum+=a[i]-48;
            while(sum<i+1)
            {
                n++;
                sum++;
            }
        }
        printf("Case #%d: %d\n",q,n);
    }
    return 0;
}
