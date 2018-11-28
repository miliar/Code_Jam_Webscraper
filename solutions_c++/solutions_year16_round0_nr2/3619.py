#include <iostream>
#include <cstdio>

using namespace std;

int get_flips(int arr[100], int size, int match) {
    if (size == 0)
        return 0;
    if (size == 1) {
        if (arr[0] == match)
            return 0;
        else
            return 1;
    }
    while (arr[size-1] == match) {
        size--;
        if (size==0)
            return 0;
    }
    return 1 + get_flips(arr, size-1, (match+1)&1);
}

int main(void) {
    int T, len, flips;
    char S[101];
    int P[100];
    scanf ("%d", &T);
    for (int i=1; i<=T; i++) {
        scanf ("%s", S);
        len = 0;
        while (S[len]!='\0') {
            switch(S[len]) {
                case '+': P[len] = 0; break;
                case '-': P[len] = 1; break;
            }
            len++;
        }
        flips = get_flips(P, len, 0);
        printf ("Case #%d: %d\n", i, flips);
    }
    return 0;
}
