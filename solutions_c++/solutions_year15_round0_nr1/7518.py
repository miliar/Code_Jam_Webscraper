#include <stdio.h>

void processTask(int taskNum) {
    int levels = 0;
    scanf("%d", &levels);
    int ovating = 0;
    int guests = 0;
    for (int i = 0; i < levels + 1; ++i) {
        int num = 0;
        scanf("%1d", &num);
        if (num == 0) {
            continue;
        }
        if (ovating < i) {
            int needGuests = (i - ovating);
            ovating += needGuests;
            guests += needGuests;
        }
        ovating += num;
    }
    printf("Case #%d: %d\n", taskNum+1, guests);
}

int main() {
    int N = 0;
    scanf("%d", &N);
    for (int i = 0; i < N; ++i) {
        processTask(i);
    }
}
