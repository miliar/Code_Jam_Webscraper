#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define mp make_pair
#define all(X) (X).begin(),(X).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)

int N,i,j,T;
long long P, Q;

int main()
{
    scanf("%d",&T);
    for(int t = 1; t <= T; t++)
    {
        scanf("%lld/%lld",&P,&Q);
        long long g = __gcd(P, Q);
        //cout << g << endl;
        P /= g;
        Q /= g;
        if((Q & (Q-1)) != 0) printf("Case #%d: impossible\n",t);
        else
        {
            int ans = 0;
            while(P < Q)
            {
                Q /= 2;
                ans++;
            }
            printf("Case #%d: %d\n",t,ans);
        }
    }
    
    return 0;
}

