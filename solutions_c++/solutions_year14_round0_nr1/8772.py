#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <utility>
#include <string>
#include <map>
#include <vector>
#include <set>

using namespace std;
const int MAXN = 100;

int t, n1, n2, a;
int one[20], two[20];


int main() {
    scanf("%d", &t);
    for(int f = 1; f <= t; ++f) {
        scanf("%d", &n1);
        for(int i = 0; i < 4; ++i) {
            for(int j = 0; j < 4; ++j) {
                scanf("%d", &a);
                one[4 * i + j] = a;
            }
        }
        scanf("%d", &n2);
        --n1; --n2;
        for(int i = 0; i < 4; ++i) {
            for(int j = 0; j < 4; ++j) {
                scanf("%d", &a);
                two[4 * i + j] = a;
            } 
        }
        /*for(int i = 0; i < 16; ++i) {
            printf("%d ", one[i]);
        } printf("\n");
        for(int i = 0; i < 16; ++i) {
            printf("%d ", two[i]);
        } printf("\n");*/
        vector <int> tmp;
        for(int i = 0; i < 4; ++i) {
            for(int j = 0; j < 4; ++j) {
                if(one[4 * n1 + i] == two[4 * n2 + j]) {
                    tmp.push_back(one[4 * n1 + i]);
                }
            }
        }
        if(tmp.size() == 0) {
            printf("Case #%d: Volunteer cheated!\n", f);
        } else if(tmp.size() == 1) {
            printf("Case #%d: %d\n", f, tmp[0]);
        } else {
            printf("Case #%d: Bad magician!\n", f);
        }
    }    
    return 0;
}
