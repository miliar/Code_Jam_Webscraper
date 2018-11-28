#include <cstdio>
#include <queue>
using namespace std;

#define MAX_S 11
#define MAX_STATES (1<<MAX_S)

int initial_state = 0;
int n_keks;

bool seen[MAX_STATES];

#define FINISHED_STATE ((1<<n_keks)-1)

int search(int s);
int reverse_substring(int input, int start, int end);

queue<int> q;
queue<int> c;

int main() {
    int num_t, t;
    scanf("%d ", &num_t);
    for (t = 1; t <= num_t; t++) {
        q = queue<int>();
        c = queue<int>();
        int i;
        n_keks = 0;
        initial_state = 0;
        for (i = 0; i < MAX_STATES; i++) {
            seen[i] = 0;
        }
        printf("Case #%d:", t);
        int cur_char = getchar();
        while (cur_char != '\n' && cur_char != EOF) {
            n_keks++;
            initial_state <<= 1;
            initial_state |= (cur_char == '+' ? 1 : 0);
            cur_char = getchar();
        }
        printf(" %d\n", search(initial_state));
    }
    return 0;
}

int search(int start_state) {
    int i;
    q.push(start_state);
    c.push(0);
    while (!q.empty()) {
        int s,cost;
        s = q.front();
        q.pop();
        cost = c.front();
        c.pop();
        if (seen[s]) continue;
        seen[s] = true;

        if (s == FINISHED_STATE) {
            return cost;
        }
        for (i = 0; i < n_keks; i++) {
            int next_state = reverse_substring(s, n_keks-1, i);
            q.push(next_state);
            c.push(cost+1);
        }
    }
    return -1;
}

int reverse_substring(int input, int start, int end) {
    int s = 1 << start;
    int e = 1 << end;
    int result = input;
    while (s >= e) {
        result &= ~(s|e);
        result |= (s&(~input) ? e : 0);
        result |= (e&(~input) ? s : 0);
        s >>= 1;
        e <<= 1;
    }
    return result;
}
