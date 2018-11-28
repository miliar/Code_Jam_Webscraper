#include <cstdio>
#include <algorithm>
#include <set>
using namespace std;

const int MAX_N = 10005;

multiset<int> rem;
int vals[MAX_N];

int main() {
    int T;
    scanf("%d",&T);

    for(int z=1;z<=T;z++) {
        int N;
        scanf("%d",&N);

        int X;
        scanf("%d",&X);

        for(int i=0;i<N;i++) {
            scanf("%d",&vals[i]);
        }

        sort(vals, vals+N);

        rem.clear();
        int num = 0;

        for(int i=N-1;i>=0;i--) {
            multiset<int>::iterator it = rem.lower_bound(vals[i]);
            if(it == rem.end()) {
                num++;
                rem.insert(X-vals[i]);
            } else {
                rem.erase(it);
            }
        }

        printf("Case #%d: %d\n",z,num);
    }

    return 0;
}
