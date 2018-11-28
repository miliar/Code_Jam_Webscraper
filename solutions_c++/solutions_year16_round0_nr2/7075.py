
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
using namespace std;

//+++- ---- ++++
//1234 3214 4123
//-+-- ++-+ ---+ ++++

int solve(char ch[]);
void update(char &ch);

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int icase;
    scanf("%d", &icase);
    for(int i=1; i<=icase; ++i) {
        char ch[105];
        scanf("%s", ch);
        printf("Case #%d: %d\n", i, solve(ch));
    }
    return 0;
}

void update(char &ch) {
    ch = ('+'==ch ? '-' : '+');
}

int solve(char ch[]) {
    int ret = 0;
    int len = strlen(ch);
    for(int i=len-1; i>=0; --i) {
        if('+' == ch[i]) { continue; }
        if('+' == ch[0]) {
            for(int j=0; j<=i; ++j) {
                if('+' == ch[j]) {
                    ch[j] = '-';
                }
                else {
                    ++ret;
                    break;
                }
            }
        }
        for(int j=0, r=i; j<r; ++j, --r) {
            swap(ch[j], ch[r]);
        }
        for(int j=0; j<=i; ++j) {
            update(ch[j]);
        }
        ++ret;
        bool tag = true;
        for(int j=0; j<i; ++j) {
            if('-' == ch[j]) {
                tag = false;
                break;
            }
        }
        if(tag) { break; }
 //       puts(ch);
    }
    return ret;
}
