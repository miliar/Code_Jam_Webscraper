#include <iostream>
#include <cassert>
#define LL long long

using namespace std;
LL k, s, c;
template<typename T, typename S> T expo(T b, S e){if(e <= 1)return e == 0?1: b;\
	return (e&1) == 0?expo((b*b), e>>1): (b*expo((b*b), e>>1));}

int main() {
    ios_base::sync_with_stdio(false);
    int t;
    cin >> t;
    for(int tc = 1; tc <= t; tc++) {
        cin >> k >> c >> s;
        cout << "Case #" << tc << ": ";
        LL K = expo(k, c - 1), st = 1;
        for(int i = 1; i <= k; i++) {
            cout << st << ' ';
            st += K;
        } cout << '\n';
    }
    return 0;
}
