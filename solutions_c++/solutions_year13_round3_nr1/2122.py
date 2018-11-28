#include <cstdio>
#include <cstring>
using namespace std;
int main()
{
    FILE * in, *out;
    char s[101];
    short n,T,q,w,nr,k,i,u,q1,i1,j;
    unsigned long long e;
    in=freopen("in.in","r",stdin);
    out=freopen("out.out","w",stdout);
    scanf("%hd",&T);
    for(k=1;k<=T;++k)
    {
        scanf("%s%hd",&s,&n);
        q=strlen(s);
        e=0;
        nr=0;
        w=0;
        u=0;
        for(i=0;i<q;++i)
        {
            if ((s[i]=='a')||(s[i]=='e')||(s[i]=='i')||(s[i]=='o')||(s[i]=='u')) nr=0;
            else
            {
                ++nr;
            if (nr==n)
            {

                  e=e+(q-i)*(i-n-u+2);




                --nr;
                u=i-n+2;
            }
            }

        }
        printf("Case #%hd: %llu\n",k,e);

    }
    fclose(in);
    fclose(out);
    return 0;
}
