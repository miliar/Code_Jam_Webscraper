#include <cstdio>
#include <map>
#include <queue>

int main() {
    int T;
    scanf("%d",&T);
    std::priority_queue<std::pair<int, int> > q;
    for (int II = 1; II <= T; ++II) {
        int n,a;
        scanf("%d",&n);
        for (int i = 0; i < n; ++i) {
            scanf("%d",&a);
            q.push(std::make_pair(a,i));
        }
        printf("Case #%d:", II);
        while (!q.empty()) {
            std::pair<int, int> theitem = q.top();
            q.pop();
            if (theitem.first == 1 && q.size() == 2) {
               printf(" %c", theitem.second + 'A');
            }
            else if (theitem.first == 1 && q.size() == 1) {
                std::pair<int, int> theseconditem = q.top();
                q.pop();
                printf(" %c%c", theitem.second + 'A', theseconditem.second+'A');
            }
            else if (q.top().first == theitem.first) {
                std::pair<int, int> theseconditem = q.top();
                q.pop();
                theseconditem.first -= 1;
                theitem.first -= 1;
                printf(" %c%c", theseconditem.second+'A', theitem.second+'A');
                q.push(theitem);
                q.push(theseconditem);
            }
            else {
                theitem.first -= 2;
                printf(" %c%c", theitem.second+'A', theitem.second+'A');
                if (theitem.first != 0) q.push(theitem);
            }
        }
        printf("\n");
        q = std::priority_queue<std::pair<int, int> > ();
    }
}
