#include <cstdio>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
int main() {
    int tc;
    scanf("%d",&tc);
    for ( int _tc = 1 ; _tc <= tc ; _tc++ ) {
        printf("Case #%d: ",_tc);
        int D;
        scanf("%d",&D);
        vector<int> v;
        for ( int i = 0 ; i < D ; i++ ) {
            int t;
            scanf("%d",&t);
            v.push_back(t);
        }
        int ans = 987654321;
        for ( int i = 1 ; i <= 1000 ; i++ ) {
            int now = 0;
            for ( int j = 0 ; j < (int)v.size() ; j++ ) {
                if ( i >= v[j] ) continue;
                int t = v[j];
                while ( t > i ) t-=i,now++;
            }
            ans = min(ans,i+now);
        }
        printf("%d\n",ans);
    }
    return 0;
}
