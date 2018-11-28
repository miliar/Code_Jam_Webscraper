#include <iostream>
using namespace std;

long long N, P, K;

long long calc(long long n)
{
    long long r=n+1LL;
    long long worst=0LL;
    for(int i=0; i<=N; i++)
    {
        worst*=2LL;
        if(r==1LL)
            worst++;
        r/=2LL;
        r=max(1LL,r);
    }
    return worst;
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    int tc;
    cin >> tc;
    for(int nt=1; nt<=tc; nt++)
    {
        cin >> N >> P;

        long long bot=0LL, top=(1LL<<N), mid=(top+bot)/2LL;
        K=(1LL<<N)-P;
        while(top-bot>1)
        {
            if(calc(mid)<2LL*K)
                top=mid;
            else
                bot=mid;
            mid=(top+bot)/2LL;
        }
        long long ans1=mid;

        K=P;
        bot=0, top=(1LL<<N)+2LL, mid=(top+bot)/2LL;
        while(top-bot>1)
        {
            if(calc(mid)>=2LL*K)
                bot=mid;
            else
                top=mid;
            mid=(top+bot)/2LL;
        }
        long long ans2=(1LL<<N)-mid-2LL;
        if(P==(1LL<<N)) ans2=P-1LL;
        cout << "Case #" << nt << ": " << ans1 << " " << ans2 << endl;
    }
}
