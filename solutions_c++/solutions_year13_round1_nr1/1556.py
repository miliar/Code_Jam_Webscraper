#include <cstdio>
#include <cstring>
#include <vector>
#include <iostream>

using namespace std;

int T, a, b;
int ans;

int main() {
    char name[50];
    char aa[50], bb[50];
    scanf("%s", name);
    strcpy(aa, name);   strcpy(bb, name);
    strcat(aa, ".in");  strcat(bb, ".out");
    FILE *in=fopen(aa, "r"), *out=fopen(bb,"w");

    fscanf(in, "%d", &T);

    for(int testCase=1; testCase <= T; testCase++) {
        fscanf(in, "%d %d", &a, &b);

        ans = 0;

        a += 1;
//        cout << a << " " << b << endl;
        b -= 2*a - 1;

        while(b >= 0) {
            ans++;
            a += 2;

//            cout << a << " " << b << endl;
            b -= 2*a - 1;
//            cout << a << " " << b << endl;
        }






        fprintf(out,"Case #%d: %d\n", testCase, ans);
    }

    return 0;
}
