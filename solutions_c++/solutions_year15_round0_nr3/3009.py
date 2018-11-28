#include<cstdio>
#define lli long long int
using namespace std;
char s[10005];
int main()
{
    int t;
    #ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    #endif

    scanf("%d",&t);


    for(lli j=1;j<=t;j++)
    {

        lli c=0,l,x;
        char ch='1';
        lli sign=1;
        scanf("%lld%lld",&l,&x);
        scanf("%s",s);
        for(lli i=0;i<x;i++)
        {
            for(lli k=0;k<l;k++)
            {
                if(ch=='1')
                {
                    if((s[k]=='i' && c==0) || (s[k]=='j' && c==1) || (s[k]=='k' && c==2))
                        c++;
                    else
                        ch=s[k];
                }
                else if(ch=='i' && s[k]=='j')
                {
                    if(c==2)
                    {
                        c++;
                        ch='1';
                    }
                    else
                        ch='k';
                }
                else if(ch=='j' && s[k]=='k')
                {
                    if(c==0)
                    {
                        c++;
                        ch='1';
                    }
                    else
                        ch='i';
                }
                else if(ch=='k' && s[k]=='i')
                {
                    if(c==1)
                    {
                        c++;
                        ch='1';
                    }
                    else
                        ch='j';
                }
                else if(ch=='i' && s[k]=='k')
                {
                    if(c==1)
                    {
                        c++;
                        ch='1';
                    }
                    else
                        ch='j';
                    sign=sign*-1;
                }
                else if(ch=='j' && s[k]=='i')
                {
                    if(c==2)
                    {
                        c++;
                        ch='1';
                    }
                    else
                        ch='k';
                    sign=sign*-1;
                }
                else if(ch=='k' && s[k]=='j')
                {
                    if(c==0)
                    {
                        c++;
                        ch='1';
                    }
                    else
                        ch='i';
                    sign=sign*-1;
                }
                else
                {
                    ch='1';
                    sign=sign*-1;
                }
            }
        }
        if(c==3 && ch=='1' && sign==1)
            printf("Case #%lld: YES\n",j);
        else
            printf("Case #%lld: NO\n",j);
    }

    return 0;
}
