#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
const int N = 1000000;
char s[N];
int main()
{
#ifndef ONLINE_JUDGE  
    freopen("in.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif 
   // ios::sync_with_stdio(0);
    int T, cas = 1;
    scanf("%d", &T);
    while (T--)
    {
       printf("Case #%d: ", cas++);
       scanf("%s", s);
       string ans = "";
       int len = 0;
       for (int i = 0;s[i] != '\0'; i++)
        if (len == 0)
        {
            ans += s[i];            
            len++;
        }
        else
        {
            if (s[i] >=  ans[0])
                ans = s[i] + ans;
            else
                ans += s[i];
        }
        cout << ans <<endl;
    }
   
    
    
    return 0;
}