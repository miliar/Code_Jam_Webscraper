#include <bits/stdc++.h>
#define fi(a,b,c) for(int a=b; a<=c; a++)
#define fd(a,b,c) for(int a=b; a>=c; a--)

#define pb push_back
#define mp make_pair
#define ft first
#define sc second

using namespace std;

typedef long long ll;

bool dd[15];
int n;
int tcase;

int main()
{
   // freopen("test.in", "r", stdin);
   // freopen("test.out", "w", stdout);

    scanf("%d", &tcase) ;
    fi(t, 1, tcase)
    {
        scanf("%d", &n);
        if (n == 0) {
            printf("Case #%d: INSOMNIA\n", t);
            continue;
        }
        fi(i, 0, 9) dd[i] = 0;
        int cnt= 0;
        ll j  = 1;
        while(1) {
            ll val = n * (j++);
            while(val != 0)
            {
                if (!dd[val % 10])  dd[val % 10] = 1, cnt++;
                val = val / 10;
            }
            if (cnt == 10)  break;
        }
        j--;
        printf("Case #%d: %lld\n", t, (ll)(n* j));
    }
}
