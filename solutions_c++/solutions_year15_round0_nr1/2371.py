#include <fstream>
#include <cstring>

using namespace std;

char _string[1005];

int main()
{
    ifstream cin("large.in");
    ofstream cout("large.out");

    int t = 0;
    cin >> t;

    for (int i = 1; i <= t; i++) {
        int n = 0;
        cin >> n;
        cin.get(); cin.get(_string, 1005);

        int bonus = 0;
        int sum = 0;

        for (int i = 0; i <= n; i++) {
            if (i > sum) {
                bonus += (i - sum);
                sum = i;
            }
            sum += (_string[i] - '0');
        }

        cout << "Case #" << i << ": " << bonus << '\n';
    }

    cin.close();
    cout.close();
    return 0;
}
