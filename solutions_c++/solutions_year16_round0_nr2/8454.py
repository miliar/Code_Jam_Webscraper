#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("bb.txt","w",stdout);
    char a[110],b[110],c[110];
    long long int num,result,len,cs=1,tc,i,k,j,r,f;
    scanf("%lld",&tc);
    while(tc--)
    {
        scanf("%s",&a);
        len=strlen(a);
        result=0;
        if(a[0]=='-') result++;
        for(i=0; i<len; i++)
        {
            //if(a[0]=='-') result++;
            if(a[i]=='-')
            {
                if(a[i-1]=='+')
                {
                    result+=2;
                    a[i-1]='-';
                    //else result++;
                }
            }
        }

        printf("Case #%lld: %lld\n",cs++,result);
    }
    return 0;
}
