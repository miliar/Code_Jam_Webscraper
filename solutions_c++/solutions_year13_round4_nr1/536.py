#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <stack>
#include <vector>

using namespace std;

#define f(o, e, p) (2ll * n + 1ll - ( (e)-(o) )) * ( (e)-(o) ) / 2 * (p);
#define M 1000002013ll
#define min(x, y) (x < y ? x : y)

int main(int argc, char** argv) {
   freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    long T;
    cin >> T;

    for (long t = 0; t < T; ++t) {
        long long n, m;
        long o, e, p;
        cin >> n >> m;
        
        vector< pair<long, long> > br(2 * m);
        long long g1 = 0ll, g2 = 0ll;
        
        for (long i = 0; i < m; ++i) {
            scanf ("%ld %ld %ld", &o, &e, &p);
            br[2 * i].first = o;
            br[2 * i].second = -p;
            
            br[2 * i + 1].first = e;
            br[2 * i + 1].second = p;
            
            g1 += f((long long)o, (long long)e, (long long)p);
            g1 %= M;
        }
        
        sort(br.begin(), br.end());
        
        stack< pair<long, long long> > st;
        
        for (long i = 0; i < 2*m; ++i) {
            if (br[i].second < 0)
                st.push( br[i] );
            
            else {
                while (br[i].second) {
                    long d, num;
                    
                    num = min(br[i].second, -(st.top().second));
                    d = br[i].first - st.top().first;
                    
                    g2 += f(0ll, (long long)d, num);
                    g2 %= M;
                    
                    st.top().second += (long long)num;
                    br[i].second -= num;
                    
                    if (st.top().second == 0ll)
                        st.pop();
                }
            }
        }
        
        long ans = (long)( (g1 - g2 + M) % M );
        
        printf("Case #%ld: %ld\n", t + 1, ans);
    }
    
    return 0;
}

