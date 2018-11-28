#include<bits/stdc++.h>
#define two(a) (1<<(a))
#define LINF (1ll<<61)
#define EPS (1e-14)
#define Lshift(a,b) (a<<b)
#define Rshift(a,b) (a>>b)
#define rep(a,b) for(a=0 ; a<b ; a++)
#define xrep(a,b,c) for(a=b ; a<c ; a++)
#define INF (1<<29)
#define swap(a,b) ( (a^=b) , (b^=a) , (a^=b) )
#define min(a,b) ( a < b ? a : b )
#define max(a,b) ( a > b ? a : b )
#define GET(x) (mark[x>>5]>>(x&31)&1)
#define SET(x) (mark[x>>5]|=1<<(x&31))
#define maxL (10000000>>5)+1
#define mod 1000000007
typedef long long ll;
using namespace std;

char in[1010];


int main() {
    int i, t, tt, n, ans, count;
    cin >> tt;
    xrep(t, 1, tt+1) {
        cin >> n >> in;
        ans = count = 0;
        rep(i, strlen(in)) {
            if (!in[i]) { ans++; }
            else if (count + ans < i) { ans = i - count; }
            count += in[i] - '0';
        }
        cout << "Case #" << t << ": " << ans << endl;
    }
}
