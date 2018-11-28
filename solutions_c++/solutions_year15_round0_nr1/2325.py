#include<stdio.h>

char inp[3000];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,ti,s,i,curr,ans;
    scanf ("%d",&t);
    for (ti=0;ti<t;++ti)
    {
        curr = ans = 0;
        scanf ("%d %s",&s,inp);
        for (i=0;i<=s;++i)
        {
            if (curr<i && inp[i]!='0')
            {
                ans += i-curr;
                curr = i;
            }
            curr += inp[i]-'0';
        }
        printf ("Case #%d: %d\n",ti+1,ans);
    }
    return 0;
}
