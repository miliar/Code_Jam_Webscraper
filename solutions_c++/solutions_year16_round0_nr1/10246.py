#include <iostream>

using namespace std;

int main()
{
    freopen ("in.txt", "r", stdin);
    freopen ("out.txt", "w", stdout);
    int n, tc, k = 0;
    cin >> tc;
    while (tc--)
    {
        int t = 0;
        cin >> n;
        int ans = 0;
        cout << "Case #" << ++k << ": ";
        if (n == 0)
        {
            cout << "INSOMNIA" << endl;
            continue;
        }
        while (t < 1023)
        {
            ans++;
            int m = n * ans;
            while (m)
            {
                int aux = m%10;
                t |= (1<<aux);
                m /= 10;
            }
        }
        cout << n*ans<< endl;
    }
    fclose (stdout);
    return 0;
}
