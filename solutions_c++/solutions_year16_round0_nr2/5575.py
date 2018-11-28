#include <bits/stdc++.h>
using namespace std;

#define LL			long long int
#define rep(i, s, e)for(int i = (s); i < (e); i++)
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



vector <char> vc;

int main(void)
{
#ifdef akid
    freopen("input","r",stdin);
    freopen("output","w",stdout);
#endif // akid

    int cas, co = 0;
    read(cas);
    while(cas --)
    {
        char ch[100 + 10];
        read(ch);
        int len = strlen(ch), ans = 0;
        vc.clear();
        rep(i, 0, len)      vc.push_back(ch[i]);
        while(true)
        {
            if(vc.empty())
                break;
            while(!vc.empty() && vc.back() == '+')
            {
                vc.pop_back();
            }
            int f = 0;
            while(!vc.empty() && vc[0] == '-')
            {
                f = 1;
                vc.erase(vc.begin());
            }
            if(f)
            {
                rep(i, 0, vc.size())
                {
                    vc[i] = (vc[i] == '-' ? '+' : '-');
                }
                reverse(all(vc));
                ans ++;
            }
            else
            {
                int k = 0;
                rep(i, 0, vc.size())
                {
                    k = 1;
                    if(vc[i] == '-')
                        break;
                    vc[i] = '-';
                }
                ans += k;
            }
        }
        printf("Case #%d: %d\n", ++co, ans);
    }
    return 0;
}

