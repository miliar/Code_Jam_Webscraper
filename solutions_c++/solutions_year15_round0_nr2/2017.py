#include<iostream>
#include<algorithm>
using namespace std;
const int MAXN = 1000 +5;
int a[MAXN];
int main()
{
    int T;
    cin >> T;
    for(int t = 0;t < T;t ++)
    {
        int D;
        cin >> D;
        int mx = 0;
        for(int i = 1;i <= D;i ++)
        {
            cin >> a[i];
            mx = max(mx , a[i]);
        }
        int ans = mx;
        for(int i = 1;i <= mx;i ++)
        {
            int cnt = i;
            for(int j = 1;j <= D;j ++)
                cnt += (a[j] + i - 1) / i - 1;
            ans = min(ans , cnt);
        }
                
                    
        
        cout << "Case #" << t + 1 << ": " <<  ans << endl;
    }
    return 0;
}
