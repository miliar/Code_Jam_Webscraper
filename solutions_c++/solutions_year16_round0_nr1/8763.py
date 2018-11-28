#include <iostream>
#include <string.h>
#include <bits/stdc++.h>

using namespace std;

int taken[10];

int main()
{
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
        int T, tc = 1;
        cin >> T;
        while (T--)
        {
            long long n, temp, ans;
            cin >> n;
            memset(taken, 0, sizeof taken);
            int counter = 0, i = 1;
            cout << "Case #" << tc++ << ": ";
            if (n == 0){
                cout << "INSOMNIA" << endl;
                continue;
                }
            while (counter < 10) {
                ans = temp = n * i;
                while (temp > 0) {
                    if (!taken[temp % 10]){
                        counter++;
                        taken[temp % 10] = 1;
                    }
                    temp /= 10;
                }
                i++;
            }
            cout << ans << endl;
	}
}
