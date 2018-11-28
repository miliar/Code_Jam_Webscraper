#include <iostream>
#include <iomanip>

using namespace std;

int solve(int n)
{
    int i;
    unsigned found = 0;
    int answer = 0;

    if(n == 0)
        return -1;

    for(i = 1; found != (1 << 10) - 1; ++i) {
        answer += n;
        for(int m = answer; m > 0; m /= 10) {
            found |= (1 << (m % 10));
        }
    }

    return answer;
}

int main(void)
{
    int T;
    cin >> T;

    for(int i = 1; i <= T; ++i) {
        int n, r;

        cin >> n;
        r = solve(n);
        cout << "Case #" << i << ": ";
        if(r == -1) {
            cout << "INSOMNIA" << endl;
        } else {
            cout << r << endl;
        }
    }

    return 0;
}

