#include <iostream>
#include <string>
#include <vector>

using namespace std;

int T, N, X;
int s[10005];

bool mark[10005];

int ans;

int main(int argc, char *argv[]) {
    std::cin >> T;
    for (int i = 0; i < T; ++i) {
        ans = 0;
        std::cin >> N >> X;
        for (int j = 0; j < N; ++j) {
            std::cin >> s[j];
        }

        memset(mark, false, sizeof(mark));
        vector<int> sv(s, s + N);
        std::sort(sv.begin(), sv.end());
        for (int j = N - 1; j >= 0; j--) {
            if (!mark[j]) {
                mark[j] = true;
                ans++;
                for (int k = 0; k < j; ++k) {
                    if (!mark[k] && sv[k] <= X - sv[j]) {
                        mark[k] = true;
                        break;
                    }
                }
            }
        }
        std::cout << "Case #" << i + 1 << ": " << ans << std::endl;
    }
}
