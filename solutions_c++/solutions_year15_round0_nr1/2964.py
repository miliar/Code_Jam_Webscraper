#include <iostream>

using namespace std;

int main()
{
    int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
        int S;
        char numK[1001+1] = {0};
        cin >> S >> numK;
        int needed = 0;
        int cur = 0;
        for (int i = 0; i <= S; i++) {
            if (cur + needed < i)
                needed += i - cur - needed;
            cur += numK[i]-'0';
        }
		cout << "Case #" << t << ": " << needed << endl;
	}
	return 0;
}
