#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<set>

using namespace std;

set<double> s1, s2, t1, t2;
set<double>::iterator its, its2;

int main()
{
    freopen("x.in","r",stdin);
    freopen("x.txt","w",stdout);
    int T, n;
    scanf("%d", &T);
    for(int cas = 1 ; cas <= T ; cas++)
    {
        s1.clear();t1.clear();
        s2.clear();t2.clear();
        scanf("%d", &n);
        for(int i = 0 ; i < n ; i++)
        {
            double x;
            scanf("%lf", &x);
            s1.insert(x);t1.insert(x);
        }
        for(int i = 0 ; i < n ; i++)
        {
            double x;
            scanf("%lf", &x);
            s2.insert(x);t2.insert(x);
        }

        int anss = 0, anst = 0;
        for(its = t1.begin() ; its != t1.end(); its++)
        {
            double x = (*its);
            its2 = t2.lower_bound(x);
            if(its2 == t2.begin())
            {
                its2 = t2.end();
                its2--;
                t2.erase(its2);
            }
            else
            {
                anst++;
                its2--;
                t2.erase(its2);
            }
        }

        for(its = s1.begin() ; its != s1.end(); its++)
        {
            double x = (*its);
            its2 = s2.upper_bound(x);
            if(its2 == s2.end())
            {
                anss++;
                its2 = s2.begin();
            }
            s2.erase(its2);
        }

        printf("Case #%d: %d %d\n", cas, anst, anss);
    }
    return 0;
}
