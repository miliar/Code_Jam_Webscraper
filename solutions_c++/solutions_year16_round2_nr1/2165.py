#include <cstdio>
#include <map>
#include <cstring>

const int maxn = 2000 + 20;
char str[maxn];
std::map<char, int> counter;
int answer[10];

int main() {
    int T;

    scanf("%d", &T);
    for (int kase = 1; kase <= T; kase ++) {
        scanf("%s", str);
        counter.clear();
        int length = 0;
        for (int i = 0; str[i] != '\0'; i++) {
            counter[str[i]] ++;
            length ++;
        }
        memset(answer, 0, sizeof(answer));
        answer[0] = counter['Z'];
        answer[8] = counter['G'];
        answer[3] = counter['H'] - answer[8];
        answer[4] = counter['R'] - answer[0] - answer[3];
        answer[2] = counter['T'] - answer[3] - answer[8];
        answer[1] = counter['O'] - answer[0] - answer[2] - answer[4];
        answer[5] = counter['F'] - answer[4];
        answer[7] = counter['V'] - answer[5];
        answer[6] = counter['S'] - answer[7];
        answer[9] = (counter['N'] - answer[1] - answer[7]) / 2;
        printf("Case #%d: ", kase);
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < answer[i]; j++) {
                putchar('0' + i);
            }
        }
        putchar('\n');
    }

    return 0;
}
