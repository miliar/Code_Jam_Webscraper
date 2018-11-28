#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <map>
#include <list>

using namespace std;

typedef long long int int64;
typedef long long unsigned int uint64;
typedef unsigned int uint;
#define MAX 101

#define SUCC printf("Case #%d: %d\n", i, flag);
#define CHEATED printf("Case #%d: Volunteer cheated!\n", i);
#define FAIL printf("Case #%d: Bad magician!\n", i);continue;


int main()
{
    int tc;
    int ans;
    int a, b, c, d;

    scanf("%d", &tc);
    for(int i=1; i<=tc; i++) {
        int arr[17]={0};
        int flag=0;
        scanf("%d", &ans);
        for (int j=1; j<5; j++) {
           scanf("%d%d%d%d", &a, &b, &c, &d);
           if (j == ans) {
               arr[a] = 1;
               arr[b] = 1;
               arr[c] = 1;
               arr[d] = 1;
           }
        }
        scanf("%d", &ans);
        for (int j=1; j<5; j++) {
           scanf("%d%d%d%d", &a, &b, &c, &d);
           //cout << a << " " << b << " " << c << " " << d << endl;
           if (j == ans) {
               if (arr[a]) {
                    flag = a;
               }
               if (arr[b]) {
                   if (flag) {
                       FAIL;
                   } else {
                    flag = b;
                   }
               }
               if (arr[c]) {
                   if (flag) {
                       FAIL;
                   } else {
                    flag = c;
                   }
               }
               if (arr[d]) {
                   if (flag) {
                       FAIL;
                   } else {
                    flag = d;
                   }
               }
               if (flag) {
                SUCC;
               } else {
                CHEATED;
               }
           }
        }
        
    }
    return 0;
}
