#include <stdio.h>
#include <string.h>

int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
    int t, cases = 1;
    
    scanf("%d", &t);
    while (t--) {
        int n;
        char str[10005];
        
        scanf("%d", &n);        
        scanf("%s", str);
		
        int i, cnt = 0, ans = 0;
        for (i = 0; i <= n; i++) {
            int x = str[i] - '0';
            if (cnt >= i) cnt += x;
            else {
               ans = ans + i - cnt;
               cnt = i + x;
            }
        }
        printf("Case #%d: %d\n", cases++, ans);
    }
    return 0;
}
