#include <iostream>
#include <fstream>

using namespace std;

int n, len, sum, answer;
char s[1050];

int main()
{
    freopen("standingovation.in", "r", stdin);
    freopen("standingovation.out", "w", stdout);
    scanf("%d", &n);
    for(int c = 1; c <= n; c++) {
        scanf("%d %s", &len, s);
        sum = answer = 0;
        for(int i = 0; i <= len; i++) {
            if(i <= sum) {
                sum += s[i] - '0';
            }
            else if(s[i] != '0'){
                answer += i - sum;
                sum += answer + s[i] - '0';
            }
        }
        printf("Case #%d: %d\n", c, answer);
    }
    return 0;
}
