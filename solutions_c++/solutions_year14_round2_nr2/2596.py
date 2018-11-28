#include <cstdio>
#include <cstdlib>
#include <iostream>

using namespace std;

int cal[1001];

int main() {
    int NN;
    scanf("%d",&NN);
    for (int II = 0; II < NN; ++II) {
        int a,b,k;
        scanf("%d %d %d",&a,&b,&k);
        int count = 0;
        for (int i = 0; i < a; ++i) {
            for (int j = 0; j < b; ++j) {
                if ((i & j) < k) {
                    ++count;
                }
            }
        }
        printf("Case #%d: %d\n", II+1,count);
    }
}
