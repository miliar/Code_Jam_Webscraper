#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    int t,s;
    char a[1005];
    int shy[1005];
    scanf("%d",&t);
    int j=1;
    while(t--)
    {

        scanf("%d%s",&s,a);
        memset(shy,0,1005);
        for(int i=0;i<strlen(a);i++)
            shy[i]=a[i]-48;
        int b=shy[0],need=0;
        for(int i=1;i<strlen(a);i++)
        {
            if(shy[i]>0)
            {
                if(i>b)
                {
                    need+=i-b;
                    b+=i-b+shy[i];
                }
                else
                {
                    b+=shy[i];
                }
            }


        }
        printf("Case #%d: %d\n",j,need);
            j++;
    }
    return 0;
}
