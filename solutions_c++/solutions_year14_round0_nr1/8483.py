#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

bool b[16];

int main() {
    int T; scanf("%d", &T);
    for (int t=1; t<=T; t++) {
        fill(b, b+16, false);
        int R; scanf("%d", &R);
        for (int r=1; r<=4; r++) {
            for (int c=1; c<=4; c++) {
                int x; scanf("%d", &x); x--;
                b[x] = (r==R);
            }
        }
        vector<int> result;
        scanf("%d", &R);
        for (int r=1; r<=4; r++) {
            for (int c=1; c<=4; c++) {
                int x; scanf("%d", &x); x--;
                if (b[x] && r==R)
                    result.push_back(x+1);
            }
        }
        
        if (result.empty())
            printf("Case #%d: Volunteer cheated!\n", t);
        else if (result.size()>1)
            printf("Case #%d: Bad magician!\n", t);
        else
            printf("Case #%d: %d\n", t, result[0]);
    }
    
    return 0;
}
