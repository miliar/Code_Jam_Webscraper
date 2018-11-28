#include <iostream>
#include <vector>
#include <algorithm>

typedef long long ll;

using namespace std;

int main()
{
    int T;

    cin >> T;
    for (int i = 1; i <= T; i++) {
        ll A;
        int N;
        ll m[110];
        int ans = 0;

        cin >> A >> N;
        for (int j = 0; j < N; j++) 
            cin >> m[j];

        sort(m, m + N);
        for (int j = 0; j < N; j++) {
            if (A == 1 && m[j] >= A) {
                ans = N;
                break;
            }
            else if (m[j] >= A) {
                int time = 0;
                ll tmp = A;

                while (true) {
                    tmp += (tmp - 1);
                    time++;
                    if (tmp > m[j])
                        break;
                }
                tmp += m[j];

                if (time < N - j) {
                    A = tmp;
                    ans += time;
                    continue;
                }
                else {
                    ans += (N - j);
                    break;
                }
            }
            else
                A += m[j];
        }

        cout << "Case #" << i << ": ";
        cout << ans << endl;
    }

    return 0;
}
