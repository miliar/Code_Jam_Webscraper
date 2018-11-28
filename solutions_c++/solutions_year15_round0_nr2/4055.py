#include <cstdio>
#include <cstdlib>
#include <list>
#include <algorithm>
using namespace std;
bool cmp(const int& first, const int& second) {
    return first > second;
}
int maxL(list<int> &L) {
    auto iter = L.begin();
    int ans = 0;
    while(iter != L.end()) {
        if (*iter > ans)
            ans = *iter;
        iter++;
    }
    return ans;
}
#ifdef DEBUG
void print(list<int> &L) {
    auto iter = L.begin();
    while (iter != L.end()) {
        printf("- %d ", *iter++);
    }
    printf("\n");
}
#endif
int solve(list<int> &L) {
    L.sort(cmp);
#ifdef DEBUG
    print(L);
#endif
    if (L.front() == 1)
        return 1;
    int size = L.front();
    int ans = maxL(L);
    for (int i = 2; i < size/2+1; i++) {
        list<int> LL = L;
        auto iter = LL.begin();
        *iter -= i;
        LL.push_back(i);
        ans = min(ans, solve(LL)+1);
    }
    return ans;
}
int main(int argc, char *argv[]) {
    int t;
    scanf("%d", &t);
    for (int tat = 0; tat < t; tat++) {
        int n;
        scanf("%d", &n);
        list<int> L;
        for (int i = 0; i < n; i++) {
            int tmp;
            scanf("%d", &tmp);
            L.push_back(tmp);
        }
        
        printf("Case #%d: %d\n", tat+1, solve(L));
    }
    
    return 0;
}
