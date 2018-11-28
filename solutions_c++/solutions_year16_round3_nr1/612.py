#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

struct Heap {
    char ch;
    int num;
    Heap(char _ch, int _num) {
        ch = _ch; num = _num;
    }
    friend bool operator < (const Heap &a, const Heap &b) {
        return (a.num != b.num ? a.num > b.num : a.ch < b.ch);
    }
};

int n, sum;
set <Heap> heap;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int nTests = 0;
    scanf("%d", &nTests);
    for(int test = 1; test <= nTests; ++test) {
        printf("Case #%d: ", test);
        scanf("%d", &n);
        sum = 0;
        heap.clear();
        for(int i = 1; i <= n; ++i) {
            int x; scanf("%d", &x);
            heap.insert(Heap('A' + (i - 1), x));
            sum += x;
        }
        if (sum & 1) {
            Heap h = *heap.begin();
            heap.erase(heap.begin());
            sum--;
            h.num--;
            printf("%c ", h.ch);
            if (h.num) heap.insert(h);
        }
        while (sum) {
            Heap h1 = *heap.begin(); heap.erase(heap.begin());
            Heap h2 = *heap.begin(); heap.erase(heap.begin());

            if (h1.num == 1) {
                printf("%c%c ", h1.ch, h2.ch);
                sum -= 2;
                continue;
            }

            if (h2.num <= (sum - 2) / 2) {
                printf("%c%c ", h1.ch, h1.ch);
                sum -= 2;
                h1.num -= 2;
                if (h1.num) heap.insert(h1);
                heap.insert(h2);
            }
            else {
                printf("%c%c ", h1.ch, h2.ch);
                sum -= 2;
                h1.num--; h2.num--;
                if (h1.num) heap.insert(h1);
                if (h2.num) heap.insert(h2);
            }
        }
        printf("\n");
    }

    return 0;
}
