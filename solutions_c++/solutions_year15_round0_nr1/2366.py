#include<cstdio>
#include<string>
#include<iostream>
using namespace std;


int main() {
    int Z;
    scanf("%d", &Z);
    for(int zz = 1; zz <= Z; ++zz){
        int result = 0, tot = 0;
        int k;
        string in;
        cin >> k >> in;
        for (int i = 0; i <= k; ++i) {
            while (tot < i) {
                tot++;
                result++;
            }
            tot += (in[i] - '0');
        }
        printf("Case #%d: %d\n", zz, result);
    }
    return 0;
}
