#include <iostream>
using namespace std;
int n, N, ans;
long long int r, t;

int main()
{
    cin >> N;
    for (n = 1; n <= N; n++)
    {
        cout << "Case #" << n << ": ";
        cin >> r >> t;
        ans = 0;
        while (t >= 0)
        {
            t -=  2 * r + 1;
            r += 2;
            ans++;
        }
        cout << (ans - 1) << endl;
    }
}

/*

  pi(r+1)^2-(r)^2=pi(2r+1)
  
 */
