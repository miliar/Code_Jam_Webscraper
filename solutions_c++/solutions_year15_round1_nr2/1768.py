#include <stdio.h>
#include <set>
#include <utility>
using namespace std;
#define bmax 1005
multiset <pair <int, int> > l;
pair <int, int> pr;
int r, t, ii, b, n, M, v[bmax], s, i, poz, mom, br;

int cmmdc(int a, int b)
{
    if (a==0)
        return b;
    if (b==0)
        return a;
    r=a%b;
    while (r)
    {
        a=b;
        b=r;
        r=a%b;
    }
    return b;
}

int cmmmc(int a, int b)
{
    return (a*b)/cmmdc(a,b);
}

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%ld",&t);
    while (t--)
    {
        ii++;
        scanf("%ld %ld",&b,&n);
        M=1;
        l.clear();
        for (i=1;i<=b;i++)
        {
            scanf("%ld",&v[i]);
            M=cmmmc(M,v[i]);
            l.insert(make_pair(0,i));
        }
        s=0;
        for (i=1;i<=b;i++)
            s+=M/v[i];
        n=n%s;
        if (n==0)
            n=s;
        //el.clear();
        poz=0;
        for (i=1;i<=n;i++)
        {
            pr=*l.begin();
            mom=pr.first;
            br=pr.second;
            l.erase(l.begin());
            l.insert(make_pair(mom+v[br],br));

        }
       /* for (mom=1;poz<n;mom++)
        {
            if (l.size()>0)
            {
                br=*l.begin();
                l.erase(l.begin());
                el.insert(make_pair(mom+v[br],br));
                poz++;
            }
            if (el.size()>0)
            {
                pr=el.begin();
                while ((*pr).first==mom)
                {
                    l.insert((*pr).second);
                    el.erase(el.begin());
                    if (el.size()==0)
                        break;
                }
            }
        }*/
        printf("Case #%ld: %ld\n",ii,br);
    }
    return 0;
}
