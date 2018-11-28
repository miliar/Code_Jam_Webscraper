#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef vector<pii> vpii;
typedef unsigned long long llu;

#define author ayushtomar
#define rf freopen("in.in", "r", stdin)
#define wf freopen("out.txt", "w", stdout)
#define debug(x) cerr<<#x<<" "<<x<<endl;
#define f first
#define s second
#define mp make_pair
#define pb push_back
int A[12];
int main()
{
    rf;
    wf;
    int n,t,i;
    scanf("%d",&t);
    for(int tt=1; tt<=t; tt++)
    {
        fill(A,A+11,0);
        scanf("%d",&n);
        int counts=0;
        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n",tt);
            continue;
        }
        for(i=1; ; i++)
        {
            int x=n*i;
            while(x)
            {
                if(A[x%10]==0) counts++;
                A[x%10]++;
                x=x/10;
            }
            if(counts==10)
                break;
        }
        printf("Case #%d: %d\n",tt,i*n);
    }
    return 0;
}
