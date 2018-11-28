#include <bits/stdc++.h>

using namespace std;

#define LL			long long int
#define Max 		1000000 + 10
#define mem(a, v)	memset(a, v, sizeof(a));

#define rep(i, s, e)for(LL i = (s); i < (e); i++)
#define all(v)		v.begin(), v.end()

#define read(args...) input, args
struct Input
{
    inline Input& operator,(int &a)
    {
        scanf("%d", &a);
    }
    inline Input& operator,(long int &a)
    {
        scanf("%ld", &a);
    }
    inline Input& operator,(long long int &a)
    {
        scanf("%lld", &a);
    }
    inline Input& operator,(float &a)
    {
        scanf("%f", &a);
    }
    inline Input& operator,(char ch)
    {
        scanf("%s", &ch);
    }
    inline Input& operator,(double &d)
    {
        scanf("%lf", &d);
    }

    template<typename T> inline Input& operator,(T &a)
    {
        cin >> a;
    }
} input;


template <class T> inline T power(T p,T e)
{
    LL ret = 1;
    while(e > 0)
    {
        if(e & 1) ret = (ret * p);
        p = (p * p);
        e >>= 1;
    }
    return (T)ret;
}


vector < vector <int> > s[100];

int main()
{
#ifdef akid
    freopen("input","r",stdin);
    freopen("output","w",stdout);
#endif // akid

    LL len = (1ll << 17ll), arr[50];
    for(LL i = 1; i <= len; i += 2)
    {
        LL n = i;
        vector <int> vc;
        while(n)
        {
            vc.push_back(n % 2);
            n /= 2;
        }
        reverse(all(vc));
        s[vc.size()].push_back(vc);
    }

    int cas, co = 0, n, j;
    read(cas);

    while(cas --)
    {
        read(n, j);
        printf("Case #%d:\n", ++co);

        rep(i, 0, s[n].size())
        {
            mem(arr, 0);

            rep(k, 0, s[n][i].size())
            {
                for(LL b = 2; b <= 10; b++)
                {
                    arr[b] += (s[n][i][k] * power(b, k));
                }
            }

            int c = 0;
            rep(b, 2, 11)
            {
                LL s = 0, sq = sqrt(arr[b]) + 1;
                rep(k, 2, sq)
                {
                    if(arr[b] % k == 0)
                    {
                        c = c + 1;
                        arr[b] = k;
                        break;
                    }
                }
            }
            if(c == 9 && j)
            {
                j --;
                for(int k = s[n][i].size() - 1; k >= 0; k--)   printf("%d", s[n][i][k]);
                printf(" ");
                rep(b, 2, 11)   printf("%lld%c", arr[b], b == 10 ? '\n' : ' ');
            }
            if(j == 0)
                break;
        }
    }
    return 0;
}

