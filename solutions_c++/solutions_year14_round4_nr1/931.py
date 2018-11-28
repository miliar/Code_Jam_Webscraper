#include <cstdio>
#include <algorithm>
#include <set>

using namespace std;

multiset<int> secior;

int main ()
{
    int a,b,c,d,z,n,x,w;

    scanf ("%d", &z);

    for (a=1; a<=z; a++)
    {
        scanf ("%d%d", &n, &x);
        w=0;

        while (n--)
        {
            scanf ("%d", &b);
            secior.insert(b);
        }

        while (!secior.empty())
        {
            if (secior.size()==1)
            {
                secior.clear();
                w++;
            }
            else
            {
                b=*secior.rbegin();
                c=secior.size();
                secior.erase(b);

                for (int i=secior.size()+1; i<c; i++)
                    secior.insert(b);

                w++;

                if (*secior.begin()+b<=x)
                    secior.erase(secior.begin());
            }
        }

        printf ("Case #%d: %d\n", a, w);
    }

    return 0;
}
