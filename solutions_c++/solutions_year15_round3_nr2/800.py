#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cstring>
using namespace std;
int T;
int k,l,s;
char sk[200];
char sl[200];
char ss[200];
int num = 0;
int maxx = 0;
int cou = 0;

int f[200];
void getf(char p[],int lp)
{
    f[0] = -1;
    for(int j=1;j<lp;j++)
    {
        int k = f[j-1] + 1;
        while(p[k] != p[j] && k > 0) k = f[k -1] + 1;
        if (p[k] == p[j])
        {
            f[j] = k;
        }
        else
            f[j] = -1;
    }
}
int ekmp(int j,int k,int lp,int ls,char p[], char s[])
{
    int aans = 0;
    while(lp - k <= ls - j )
    {
        if (s[j] == p[k])
        {
            k++;
            j++;
            if (k == lp)
            {
                aans++;
                k = f[k - 1] + 1;
            }
        }
        else if (k > 0)
        {
            k = f[k - 1] + 1;
        }
        else
        {
            j++;
        }
    }
    return aans;
}

void dsf(int len)
{
    if (len == s)
    {
        ss[len] = '\0';
        int kj = ekmp(0,0,l,s,sl,ss);
        if (kj>maxx) maxx = kj;
        cou += kj;
        num++;
        return;
    }
    for(int i=0;i<k;i++)
    {
        ss[len] = sk[i];
        dsf(len+1);
    }
}
int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    cin>>T;
    int t = 0;
    while(t < T)
    {
        cin>>k>>l>>s;
        scanf("%s%s",sk,sl);
        getf(sl,l);
        num = 0;
        maxx = 0;
        cou = 0;
        int len = 0;
        for(int i=0;i<k;i++)
        {
            ss[len] = sk[i];
            dsf(len+1);
        }
        double ans = maxx;
        ans = ans - 1.0*cou/num;
        t++;
        printf("Case #%d: %.7lf\n",t,ans);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
