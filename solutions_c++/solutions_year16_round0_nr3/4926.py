#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;
char s[50];
unsigned long long ans[15];
int n, m, l;
int primer_judge(unsigned long long a)
{
    int i;
    
    for(i = 2; i*i <= a; i++)
        if(a%i == 0)
            return 0;
    return a != 1;
}
int judge()
{
    int i, j, p, pes = 0, k, q;
    unsigned long long g = 0;
    
    for(i = 2; i <= 10; i++)
    {
        g = 0;
        q = 0;
        for(j = n-1; j >= 0; j--)
        {
            p = s[j]-'0';
            g += p*pow(i, q++);
        }
        if(primer_judge(g))
            return 0;
        for(k = 2; k*k <= g; k++)
            if(g % k == 0)
            {
                ans[pes++] = k;
                break;
            }
    }
    return 1;
}
void get_gcd()
{
    
}
void dfs(int k)
{
    if(l == m)
        return;
    if(k == n-1)
    {
        int res = judge();
        
        if(res)
        {
            int i;
            
            l++;
            get_gcd();
            for(i = 0; i < n; i++)
            	printf("%c", s[i]);
            printf(" ");
            for(i = 0; i < 9; i++)
                printf("%lld ", ans[i]);
            printf("\n");
        }
        return;
    }
    else if(k < n-1)
    {
        s[k] = '0';
        dfs(k+1);
        s[k] = '1';
        dfs(k+1);
    }
    return;
}
int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("output3.out", "w", stdout);
    int t, count = 0;
    
    cin >> t;
    while(t--)
    {
        l = 0;
        cin >> n >> m;
        s[0] = '1';
        s[n-1] = '1';
        printf("Case #%d:\n", ++count);
        if(n > 1)
            dfs(1);
    }
    return 0;
}
