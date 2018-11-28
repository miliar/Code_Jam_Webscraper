#include<bits/stdc++.h>
#define ALL(X)        X.begin(),X.end()
#define FOR(I,A,B)    for(int (I) = (A); (I) <= (B); (I)++)
#define FORW(I,A,B)   for(int (I) = (A); (I) < (B);  (I)++)
#define FORD(I,A,B)   for(int (I) = (A); (I) >= (B); (I)--)
#define CLEAR(X)      memset(X,0,sizeof(X))
#define SIZE(X)       int(X.size())
#define CONTAINS(A,X) (A.find(X) != A.end())
#define PB            push_back
#define MP            make_pair
#define X             first
#define Y             second
using namespace std;
typedef signed long long slong;
typedef long double ldouble;
const slong INF = 1000000100;
const ldouble EPS = 1e-9;

string s;

void read_data() {
    cin >> s;
}

bool ok() {
    for(char c: s) if(c == '-') return false;
    return true;
}

void solve() {
    int ret = 0;
    while(!ok()) {
        ++ret;
        int idx = s.rfind('-');
        FOR(i,0,idx) {
            if(s[i] == '-') s[i] = '+';
            else s[i] = '-';
        }
    }
    printf("%d\n", ret);
}

int main() {
    int z;
    scanf("%d", &z);
    FOR(test_id,1,z) {
        printf("Case #%d: ", test_id);
        read_data();
        solve();
    }
}
