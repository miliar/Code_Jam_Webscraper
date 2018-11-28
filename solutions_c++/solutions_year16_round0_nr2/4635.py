#include <bits/stdc++.h>
using namespace std;

char str[1000];

int fun(int l)
{
    str[l]='+';
    int i,j,ans;
    ans=0;

    for(i=0;i<l;i++)
    {
        if(str[i]!=str[i+1])
        {
            ans++;
            for(j=0;j<=i;j++)
            {
                str[j]=str[i+1];
            }
        }
    }

    return ans;

}

int main()
{
    freopen("0in.txt","r",stdin);
    freopen("0out.txt","w",stdout);

    int test,testno;

    scanf("%d",&testno);
    for(test=1;test<=testno;test++)
    {
        scanf("%s",str);
        printf("Case #%d: ",test);
        printf("%d\n",fun(strlen(str)));

    }

}
