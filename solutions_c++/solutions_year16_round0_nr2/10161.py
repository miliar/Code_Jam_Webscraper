#include <cstdio>
#include <cstring>
using namespace std;
char s[150];
int nrm, nrp, op,T;
void rezolva_problema()
{
    int t,i;
    scanf("%d\n", &T);
    for(t=1;t<=T;++t)
    {
        gets(s);
        nrm=nrp=op=0;
        int lg=strlen(s);
        if(s[0]=='-') nrm++;
        else nrp++;
        for(i=1;i<lg;++i)
        {
            if(s[i]=='-'&&s[i-1]=='-') nrm++;
            if(s[i]=='+'&&s[i-1]=='+') nrp++;
            if(s[i]=='+'&&s[i-1]=='-')
            {
                nrp=nrm+1;
                op++;
                nrm=0;
            }
            if(s[i]=='-'&&s[i-1]=='+')
            {
                nrm=nrp+1;
                op++;
                nrp=0;
            }
        }
        if(nrp==lg) printf("Case #%d: %d\n", t,op);
        else printf("Case #%d: %d\n", t,op+1);
    }
}
int main()
{
    freopen("pkn.in", "r", stdin);
    freopen("pkn.out", "w", stdout);
    rezolva_problema();
    return 0;
}
