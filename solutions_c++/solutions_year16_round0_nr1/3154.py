#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cmath>
#include <iostream>
#include <algorithm>

using namespace std;

bool b[10];
int test, n;

int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    scanf("%d", &test);
    for (int i = 1; i <= test; i++) {
        scanf("%d", &n);
        cerr << n << "  " << i << endl; 
        //if (i == 1) continue;
        memset(b, false, sizeof(b)); 
        int cnt = 0; long long num = 0;
        for (int j = 1; j <= 10000000 && cnt < 10; j++) {
            num += n;
            //cerr << j << " " << num << endl; 
            //if (!(j % 1000000)) cerr << j << endl;
            for (long long k = num; k > 0; k /= 10) 
                if (!b[k % 10]) b[k % 10] = 1, ++cnt;
        } 
        printf("Case #%d: ", i);
        if (cnt < 10) printf("INSOMNIA\n");
        else printf("%I64d\n", num);
    }
} 
        
