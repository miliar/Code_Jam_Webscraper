#include <iostream>
#include <stdio.h>

using namespace std;
char a[1005];
int main()
{
    int t,sp,extra,i,n,p;

    freopen( "A-large.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );

    scanf("%d",&t);
    for(p=1;p<=t;p++)
    {
        extra=0;sp=0;
        scanf("%d",&n);
        scanf("%s",a);
        sp+=(a[0]-'0');
        for(i=1;i<=n;i++)
        {
            if(a[i]=='0')
                continue;
            if(a[i-1]=='0'){
                if(sp<i){
                    extra+=i-sp;
                    sp+=i-sp;
                }
            }
            sp+=(a[i]-'0');
        }
        printf("Case #%d: %d\n",p,extra);
    }
    return 0;
}
