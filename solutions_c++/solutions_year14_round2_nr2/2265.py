#include<cstdio>
#include<vector>
#include<map>
#include<set>
#include<iostream>
#include<iomanip>
#include<time.h>
#include<sstream>
#include<fstream>
#include<string>
#include<string.h>
#include<algorithm>

#define nl printf("\n")

using namespace std;

int main()
{
    int T;
    scanf("%d", &T);

    for (int t = 0; t < T; t++) {
        int a, b, k;
        scanf("%d %d %d", &a, &b, &k);

        int num = 0;
        for (int i = 0; i < a; i++) {
            for (int j = 0; j < b; j++) {
                if ((i & j) < k) {
                    num++;
                }
            }
        }

        printf("Case #%d: %d\n", t+1, num);
    }

}

