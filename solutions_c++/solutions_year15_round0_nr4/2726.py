#include <stdio.h>
#include <algorithm>

using namespace std;

const int N = 1e3 + 5;

int main() {
    freopen("D-small-attempt3.in", "r", stdin);
    //freopen("in.ads", "r", stdin);
    freopen("out.ads", "w", stdout);
    int T, ncase = 0;
    scanf("%d", &T);
    while(T--) {
        int x, r, c;
        scanf("%d%d%d", &x, &r, &c);
        if(r > c) {
            swap(r, c);
        }
        bool is_complete_cover = false;
        if(((r * c) % x) != 0) {
            is_complete_cover = false;
        }
        else if(x == 1) {
            is_complete_cover = true;
        }
        else if(x == 2) {
            is_complete_cover = true;
        }
        else if(x == 3) {
            if(r == 1) {        //<1,3>
                is_complete_cover = false;
            }
            else {
                is_complete_cover = true;
            }
        }
        else if(x == 4) {
            if(r == 1) {        //<1,4>
                is_complete_cover = false;
            }
            else if(c == 2) {   //<2,2>
                is_complete_cover = false;
            }
            else if(r == 2) {   //<2,4>
                is_complete_cover = false;
            }
            else if(r == 4) {   //<4,4>
                is_complete_cover = true;
            }
            else {              //<3,4>
                is_complete_cover = true;
            }
        }
        printf("Case #%d: %s\n", ++ncase, (is_complete_cover ? "GABRIEL" : "RICHARD"));
    }
    return 0;
}
