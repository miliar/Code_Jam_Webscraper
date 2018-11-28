#include <bits/stdc++.h>

using namespace std;

long long int a[10];

bool digit [10];

int d;


void check (long long int n)
{
    long long int N = n;

    while (n!=0) {
        int tmp = n%10;
        if (!digit[tmp]) {
            digit[tmp]=1;
            d++;
            a[tmp] = N;
        }
        n/=10;
    }
}

int main ()
{
    freopen ("in.txt","r",stdin);
    freopen ("out.txt","w",stdout);

    int t,kase=0;

    scanf ("%d",&t);

    while (t--) {
        long long int n;
        scanf ("%lld",&n);
        memset (digit,0,sizeof digit);
        d = 0;

        printf ("Case #%d: ",++kase);

        if (n==0) {
            printf ("INSOMNIA\n");
            continue;
        }


        for (int i=1;;i++) {
            check(i*n);

            if (d==10) {
                printf ("%lld\n",i*n);

                break;
            }
        }
    }
    return 0;
}
