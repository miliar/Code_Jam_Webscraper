#include <iostream>
using namespace std;

int n, T;
int main()
{
    scanf("%d", &T);
    string s;
    for (int I = 1; I <= T; ++I)
    {
        scanf("%d", &n);
        cin >> s;
        int sum = 0;
        int ans = 0;
        for (int i = 0;  i <= n; ++i)
        {
            int p = s[i] - '0';
            if (sum >= i)
                sum += p;
            else
            {
                ans += i - sum;
                sum += i - sum;
                sum += p;
            }
        }
        cout << "Case #" << I << ": " << ans << endl;
    }
}
        
