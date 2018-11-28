#include<cstdio>
#include<cstdlib>
#include<cstring>

using namespace std;

int main(void)
{
    freopen("B.in","r",stdin);
    freopen("Bout.txt","w",stdout);
    int tt;
    int T;
    char str[105];
    int len;
    scanf("%d",&T);

    int l;
    int A[105];
    int B[105];
    int i;
    int ans;
    for(tt = 1;tt<=T;tt++)
    {
        ans = 0;
        scanf("%s",str);
        len = strlen(str);
        l = 0;
        if(str[0]=='+')
            A[l++] = 1;
        else
            A[l++] = 0;
        for(i=1;i<len;i++)
        if(str[i]!=str[i-1])
        {
            A[l] = !A[l-1];
            l++;
        }
        if(A[0]==1)
        {
            for(i=1;i<l;i++)
            if(A[i]==0&&A[i-1]==1)
            {
                ans+=2;
            }

        }
        else
        {
            ans++;
            int zeroEnd = 1;
            for(i=1;i<l;i++)
                if(A[i]==0)
                    zeroEnd = 1;
            for(i=zeroEnd;i>=0;i--)
            {
                B[zeroEnd-i] = !A[i];
            }
            for(i=0;i<=zeroEnd;i++)
                A[i] = B[i];
            for(i=1;i<l;i++)
            if(A[i]==0&&A[i-1]==1)
            {
                ans+=2;
            }
        }
        printf("Case #%d: %d\n",tt,ans);
    }

    return 0;
}
