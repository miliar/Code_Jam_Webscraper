#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>

using namespace std;

int T;
int A, B;

bool isPaly(int x) {
    vector<int> pa;
    while(x > 0) {
        pa.push_back(x%10);
        x /= 10;
    }
    for(int i=0; i<pa.size()/2; i++) {
        if(pa[i] != pa[pa.size()-i-1]) return false;
    }
    return true;
}

int main() {
    char name[50];
    char a[50], b[50];
    scanf("%s", name);
    strcpy(a, name);   strcpy(b, name);
    strcat(a, ".in");  strcat(b, ".out");
    FILE *in=fopen(a, "r"), *out=fopen(b,"w");

    fscanf(in, "%d", &T);

    int ans;
    int x, y;

    for(int i=1; i<=T; i++) {
        fscanf(in, "%d %d", &A, &B);

        ans = 0;
        x = sqrt(A);
        y = sqrt(B)+1;

        for(int j=x; j<=y; j++) {
            if(j*j < A || j*j > B) continue;
            if(isPaly(j) && isPaly(j*j)) {
                ans++;
//                fprintf(out, "%d %d\n", j, j*j);
            }
        }

        fprintf(out, "Case #%d: %d\n", i, ans);
    }
    return 0;
}
