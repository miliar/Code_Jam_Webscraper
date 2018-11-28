#include <cstdio>
#include <cstdlib>

int motes[1000000];
int buffcosts[1000000];
int best[1000000];

int min(int a, int b) {return a < b? a : b;}

int compareint(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int readandanswer() {
    int size, nomotes;

    scanf("%d %d", &size, &nomotes);

    for (int i = 0; i < nomotes; i++) {
        scanf("%d", &motes[i]);
    }
    
//    for(int i = 0; i < nomotes; i++) printf("%d ", motes[i]);
//    printf("\n");
    qsort(motes, nomotes, sizeof(int), (&compareint));
//    for(int i = 0; i < nomotes; i++) printf("%d ", motes[i]);
//    printf("\n");

    if (size == 1) return nomotes;

    for (int i = 0; i < nomotes; i++) {
        if (motes[i] < size) {
            size += motes[i];
            buffcosts[i] = 0;
        } else {
            int buffcost = 0;
            while (motes[i] >= size) {size += (size - 1); buffcost++;}
            buffcosts[i] = buffcost;
            size += motes[i];
        }
    }

    best[nomotes-1] = min(buffcosts[nomotes-1], 1);
    for (int i = nomotes-1; i > 0; i--) best[i-1] = min(best[i] + buffcosts[i-1], nomotes - i + 1);
//    for (int i = 0; i < nomotes; i++) printf("%d ", buffcosts[i]);
//    printf("\n");
//   for (int i = 0; i < nomotes; i++) printf("%d ", best[i]);
// printf("\n");
    return best[0];
}

int main() {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        printf("Case #%d: ", i + 1);
        printf("%d\n", readandanswer());
    }
}
