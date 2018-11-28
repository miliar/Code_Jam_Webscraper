#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,s,c,r,k=0;
    char a[1005];
    scanf("%d",&t);
    while(t--)
    {
        c=0;
        r=0;
        scanf("%d%s",&s,&a);
        for(int i=0;i<=s;i++)
        {
            if(a[i]>'0')
            {
                if(c+r<i)
                    r+=(i-c-r);
                //cout<<r<<" ";
            }
            c+=(a[i]-'0');
        }
        printf("Case #%d: %d\n",k+1,r);
        k++;
    }
}
