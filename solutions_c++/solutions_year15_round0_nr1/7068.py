#include<iostream>
#include<cstdlib>
#include<cstdio>

int ss[2000] = {0};

int main() {

    char c;
    int k = 0,t,s;
    scanf("%d",&t);
    while (t--) {
        ++k;
        scanf("%d",&s);
        scanf("%c",&c);
        for (int i = 0;i <= s;++i) {
            scanf("%c",&c);
            ss[i] = c - '0';
        }
        int answer = 0;
        int sum = 0;
        for (int i = 0;i <= s;++i)
            if (i > sum) {
                answer += (i - sum);
                sum = i + ss[i];
            } else {
                sum += ss[i];
            }
        printf("Case #%d: %d\n",k,answer);
    }
    return 0;
}
