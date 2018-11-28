#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>

using namespace std;

int main()
{
    int testCase;
    freopen("/Users/qianjay/Documents/algorithm/pa/in", "r", stdin);
    scanf("%d",&testCase);
    for (int id=1; id <= testCase; id++) {
        printf("Case #%d: ",id);
        int number;
        scanf("%d",&number);
        if (number==0) {
            printf("INSOMNIA\n");
            continue;
        }
        int cnt=0;
        int digit[10];
        memset(digit, 0, sizeof(digit));
        int i;
        for (i=1; cnt<10; i++) {
            int val=number*i;
            while (val) {
                int d=val%10;
                val/=10;
                if (digit[d]==0) {
                    cnt++;
                }
                digit[d]++;
            }
        }
        printf("%d\n",(i-1)*number);
    }
    return 0;
}