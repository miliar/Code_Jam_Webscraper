#include<stdio.h>

int main() 
{
    int T;
    int s_max;
    char str[1024];
    scanf("%d", &T);
    for (int item=1; item<=T; ++item) {
        scanf("%d %s", &s_max, str);

        int total = 0;
        int result = 0;
        int now = 0;
        for (int i=0; str[i]; ++i) {
            now = (str[i] -'0');
            int need = 0;
            if (total < i) {
                need = i-total;
            }
            result += need;
            total += now+need;
        }

        printf("Case #%d: %d\n", item, result);
    }
}
