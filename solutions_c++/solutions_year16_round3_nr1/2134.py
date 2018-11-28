#include <bits/stdc++.h>
#define REP(i, a, b) for(int i = int(a); i < int(b); i++)
using namespace std;

int main(int argc, char** argv)
{
    // freopen("input.txt", "r", stdin);
    // freopen("output.txt", "w", stdout);

    int T, t;
    cin >> T;
    REP(t, 1, T + 1)
    {
        cout << "Case #" << t << ": ";
        int N, i;
        cin >> N;
        int arr[N], total = 0, max = 0, maxi[N] = { 0 }, maxcount = 0;
        REP(i, 0, N)
        {
            cin >> arr[i];
            total += arr[i];
            if(max <= arr[i]) {
                max = arr[i];
            }
        }

        REP(i, 0, N)
        {
            if(arr[i] == max) {
                maxi[i] = 1;
                maxcount++;
            }
        }

        while(total != 0) {
            int count = 0;
            REP(i, 0, N)
            {
                if(maxi[i] == 1) {
                    char ch = (char)('A' + i);
                    cout << ch;
                    count++;
                    arr[i]--;
                    total--;
                    maxi[i] = 0;
                    if(count == 2 || (arr[i] == 0 && maxcount > 2)) {
                        break;
                    }
                }
            }

            cout << " ";
            max = 0;
            maxcount = 0;
            REP(i, 0, N)
            {
                maxi[i] = 0;
                if(max <= arr[i] && arr[i] != 0) {
                    max = arr[i];
                }
            }

            REP(i, 0, N)
            {
                if(arr[i] == max) {
                    maxi[i] = 1;
                    maxcount++;
                }
            }
        }
        cout << endl;
    }
    // fclose(stdin);
    // fclose(stdout);
    return 0;
}
