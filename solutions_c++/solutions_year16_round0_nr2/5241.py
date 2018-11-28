#include <bits/stdc++.h>

#define sd(x)       scanf("%d", &x)
#define slld(x)     scanf("%lld", &x)
#define sc(x)       scanf("%c", &x)
#define pd(x)       printf("%d", x)
#define plld(x)     printf("%lld\n", x)
#define pc(x)       printf("%c", x)
#define pdln(x)     printf("%d\n", x)
#define prl(x)      cout << x << endl
#define LL          long long
#define forn(i, n)  for(int i = 0; i < (int)n; i++)
#define fori(i, n)  for(int i = 1; i <= (int)n; i++)
#define revn(i, n)  for(int i = (int)(n - 1); i >= 0; i--)
#define pb          push_back
#define pii         pair <int, int>

#define mem(x, y)   memset(x, y, sizeof(x))
#define MAX         100002
#define MOD         1000000007

using namespace std;

char str[102];
int arr[102];

int main()
{
    //freopen("B-large.in", "r", stdin);
    //freopen("B-large.out", "w", stdout);
    int test, caseno;
    scanf("%d\n", &test);
    for(caseno = 1; caseno <= test; caseno++)
    {
        gets(str);
        int cnt = 0;
        int len = strlen(str);
        forn(i, len)
        {
            if(str[i] == '+') arr[i] = 1;
            else arr[i] = 0;
        }
        int l = 0, r = len - 1;
        int inc = 1;
        int cmp = 1;
        forn(i, len)
        {
            //prl(l << " " << r << " " << cmp);
            if(l == r)
            {
                if(arr[l] != cmp) cnt++;
                break;
            }
            if(l < r) inc = 1;
            else inc = -1;
            if(arr[r] == cmp) r = r - inc;
            else
            {
                if(arr[l] == cmp)
                {
                    cnt += 2;
                    //arr[l] = arr[l] ^ 1;
                }
                else cnt++;
                //prl(l);
                if(arr[l] != cmp) l = l + inc;
                else
                {
                    while(arr[l] == cmp)
                    {
                        l = l + inc;
                        //prl(l);
                        //i++;
                    }
                }

                //prl(l << " " << r);

                l = l ^ r;
                r = l ^ r;
                l = l ^ r;

                //prl(l << " " << r);

                cmp = cmp ^ 1;
            }
        }
        printf("Case #%d: %d\n", caseno, cnt);
    }
    return 0;
}


