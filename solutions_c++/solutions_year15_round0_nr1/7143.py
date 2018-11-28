#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;




int main(int argc, char const *argv[])
{
    int t,n, c, f;
    char s[1001];
    scanf("%d",&t);

    for(int i=1;i<=t;++i)
    {
        c= 0; f=0;
        scanf("%d %s",&n,s);

        if(s[0]=='0') c = f = 1;
        else c = s[0]-'0';

        unsigned sz = strlen(s);

        for(unsigned ii=1;ii<sz;++ii)
        {
            if(c>=n)
                break;
            else
            {
                if(c >= ii)
                {
                    if(s[ii]!='0')
                        c+= (s[ii]-'0') ;
                }else
                {
                    if(s[ii]!='0')
                    {
                        f += (ii-c);
                        c += ii-c + (s[ii]-'0');
                    }
                }
            }
        }
        printf("Case #%d: %d\n",i,f);
    }

    return 0;
}
