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

slong N;

void read_data() {
    scanf("%lld", &N);   
}

/*string to_string(int n) {
    stringstream ss;
    ss << n;
    string ret;
    ss >> ret;
    return ret;
}*/

void solve() {
    set<slong> S;
    FOR(i,1,1000000) {
        slong w = N * i;
        for(char c: to_string(w)) S.insert(c);
        if(SIZE(S) == 10) {
            printf("%lld\n", w);   
            return;
        }
    }
    printf("INSOMNIA\n");
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
