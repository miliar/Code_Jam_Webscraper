#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;

set<int> st;
set<int>::iterator it;

vector<int> ans;

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int _, cnt = 1;
    scanf("%d", &_);
    while(_--) {
        st.clear();
        int a, b;
        scanf("%d", &a);
        for(int i = 1; i <= 4; i++) {
            for(int j = 0; j < 4; j++) {
                scanf("%d", &b);
                if(a == i) st.insert(b);
            }
        }
        ans.clear();
        scanf("%d", &a);
        for(int i = 1; i <= 4; i++) {
            for(int j = 0; j < 4; j++) {
                scanf("%d", &b);
                if(a == i) {
                    if(st.find(b) != st.end()) ans.push_back(b);
                }
            }
        }
        printf("Case #%d: ", cnt++);
        if(ans.size() > 1) printf("Bad magician!\n");
        else if(ans.size() == 1) printf("%d\n", ans[0]);
        else printf("Volunteer cheated!\n");
    }

    return 0;
}
