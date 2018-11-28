#include <bits/stdc++.h>
using i64 = long long;
using u64 = unsigned long long;
using u32 = unsigned;
using namespace std;
bool isPrimeSqrt(u64 n){
    u64 s = u64(sqrt(n));
    for(size_t i = 2; i <= s; ++i)
        if (n % i == 0)
            return false;

    return true;
}
int main() {
    ios::sync_with_stdio(false);
    ofstream output("out.txt");
    ifstream input("in.txt");

    u64 Len, J;
    u64 cnt = 0;
    input >> Len;
    input >> Len >> J;
    output << "Case #1:\n";
    for(size_t j = 1ULL << Len - 1; j < 1ULL << Len && cnt < J; ++j){
        bool isPrime = false;
        string s = bitset<64>(j).to_string();
        string ans = string(&s[64 - Len], &s[64]);
        if (ans[ans.length() - 1] != '1')
            continue;
        for(size_t i = 2; i <= 10; ++i){
            u64 M = strtoul(&(ans[0]), NULL, i);
            ans += " ";

            if (isPrimeSqrt(M)){
                isPrime = true;
                break;
            }
            for(size_t i = 2; i < M; ++i){
                if (M % i == 0) {
                    ans += to_string(i);
                    ans += " ";
                    break;
                }

            }

        }
        if (!isPrime) {
            cnt++;
            output << ans << "\n";
        }
    }
    return 0;
}