
#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <string.h>
using namespace std;
const int MAX_N = 110;
int TC, S, len;
#define INF 9999999
char buffer[1100];
int main()
{
    int T, i, j, k, pos;
    int sum, add;
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &TC);
    for(T = 1; T <= TC; T++ ) {
        scanf("%d", &S);
        printf("Case #%d: ",T);
        scanf("%s", buffer);
        if(S==0) {
            printf("%d\n", 0);
            continue;
        }
        add = 0;
        sum = buffer[0] - '0';
        for(i = 1; i<=S; i++) {
            if(i > sum && buffer[i]!= '0') {
                add +=i-sum;
                sum += add;
            }
            sum += buffer[i] - '0';
        }
        cout<<add<<endl;
    }
    return 0;
}

