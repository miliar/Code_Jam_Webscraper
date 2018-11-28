#include<cstdio>

using namespace std;

bool allHappy(int pancake[], int n) {
    for(int i = 0; i < n; i++) {
        if(pancake[i] == -1) return false;
    }
    return true;
}

int main() {
    int t, casei = 0;
    scanf("%d", &t);
    while(t--) {
        char str[101], tmp;
        int pancake[100];
        scanf("%s", str);
        int n = 0;
        while((tmp = str[n]) != '\0') {
            if(tmp == '+') pancake[n] = 1;
            else pancake[n] = -1;
            ++n;
        }
        int res = 0, pos = 0;
        while(pos < n) {
            if(allHappy(pancake, n)) break;
            ++res;
            int pivotElement = pancake[0], pos = 0;
            while(pos < n && pancake[pos] == pivotElement) {
                pancake[pos] *= -1;
                ++pos;
            }
        }
        if(pancake[0] == -1) ++res;
        printf("Case #%d: %d\n", ++casei, res);
    }
    return 0;
}
