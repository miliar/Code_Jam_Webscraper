#include <cstdio>
#include <queue>

using namespace std;

int main() {
    int T;
    scanf("%d", &T);

    char in[1010];
    for (int times = 0; times < T; times++) {
        scanf("%s", in);

        deque<char> deq;
        for (int i = 0; in[i]; i++) {
            if (deq.size() == 0 or deq.front() <= in[i]) {
                deq.push_front(in[i]);
            } else {
                deq.push_back(in[i]);
            }
        }

        printf("Case #%d: ", times+1);
        for (auto& c : deq) {
            printf("%c", c);
        }
        puts("");
    }
}
