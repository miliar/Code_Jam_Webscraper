#include<bits/stdc++.h>
char str[1001];
int main()
{
    freopen( "A-large.in", "r", stdin );
	freopen( "output.txt", "w", stdout );
    int t, i, j, ans, cnt, s;
    char c;
    scanf("%d", &t);
    i = 1;
    while(i <= t)
    {
        scanf("%d", &s);
        cnt = ans = 0;
        scanf("%s", &str);
        for(j=0;j<=s;j++)
        {
            c = str[j];
            if(c !='0')
            {
                if(j > cnt)
                {
                    ans += (j-cnt);
                    cnt += j-cnt;
                }
                cnt += c-'0';
            }
        }
        printf("Case #%d: %d\n", i, ans);
        i++;
    }

}
