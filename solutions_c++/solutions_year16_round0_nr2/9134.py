#include <iostream>
#include <map>
#include <cstring>

using namespace std;

bool finish(char S[], int L);

void doCase(int iCase) {
    printf("Case #%d: ", iCase);

    char S[102]; scanf("%s", S);
    int L = strlen(S);
    
    int n = 0;
    char s[102];
    
    while (!finish(S, L)) {
        int i=1;
        
        while (i < L && S[i] == S[i - 1]) i++;
        
        strncpy(s, S, i);
        for (int j=0; j<i; j++) {
            S[j] = (s[i-1-j] == '+' ? '-' : '+');
        }
        
        n++;
    }
    
    
    printf("%d\n", n);
}

bool finish(char S[], int L) {
    for (int i=0; i<L; i++) {
        if (S[i] == '-') return false;
    }
    return true;
}

int main(void) {
    int T; scanf("%d", &T);
    for (int i=1; i<=T; i++) doCase(i);
	return 0;
}