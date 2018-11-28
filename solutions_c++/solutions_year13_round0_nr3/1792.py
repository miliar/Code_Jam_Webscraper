#include<iostream>
using namespace std;
#include<algorithm>
#include<set>
#include<string>
#include<cstring>
#include<vector>
#include<queue>
#include<stack>
#include<deque>
#include<cstdio>
#include<map>

typedef long long lli;

#define fi(i,a,b,d) for(i=a;i<=b;i+=d)
#define fir(i,a,b,d) for(i=a;i>=b;i-=d)

#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))

#define vi vector<int>
#define all(v) v.begin(), v.end()

#define mp make_pair
#define pb push_back
#define ppb pop_back
#define pf push_front
#define ppf pop_front


#define inpi(i) scanf("%d", &i)
#define inplli(i) scanf("%lld", &i)
#define inpc(ch) scanf("%c", &ch)
#define printi(i) printf("%d\n", i)
#define printlli(i) printf("%lld\n", i)
#define printc(ch) printf("%c\n", ch)
#define inpfl(fl) scanf("%f", &fl)
#define printfl(fl) printf("%f", fl)


class className
{
    long long max, arr[1010];
    long long t, a, b, i, j, k;

    public:

    bool is_pal(long long num)
    {
        long long num2, num3;

        num2 = num;
        num3 = 0;

        while(num2)
        {
            num3 = num3*10 + num2%10;
            num2/=10;
        }

        if(num3==num)
        return true;

        return false;
    }

    void pre()
    {
        j = -1;

        fi(i, 1, max, 1)
        {
            if(is_pal(i) && is_pal(i*i))
            {
                arr[++j] = i*i;
            }
        }

        //cout<<j<<'\n';
        //fi(i, 1, j, 1)
        //cout<<arr[i]<<'\n';

    }

    int find(long long num)
    {
        int lo, hi, mid, ans;

        lo = 0;
        hi = j;

        while(lo<=hi)
        {
            mid = lo + (hi-lo)/2;

            if(arr[mid]==num)
            return mid;

            if(arr[mid]<num)
            {
                ans = mid;
                lo = mid+1;
            }

            else
            {
                hi = mid-1;
            }
        }

        return ans;
    }

    void solve()
    {
        max = 10000000;
        pre();

        int lans, rans;
        cin>>t;

        fi(k,1,t,1)
        {
            cin>>a>>b;

            cout<<"Case #"<<k<<": ";

            lans = find(a);
            rans = find(b);

            if(arr[lans]<a)
            ++lans;

            if(lans>rans)
            cout<<"0\n";
            else
            cout<<rans-lans+1<<'\n';
        }
    }
};

int main()
{
    className obj;

    obj.solve();
    return 0;
}
