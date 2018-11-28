#include <iostream>
#include <cstdio>

using namespace std;

int main() {
    int N;
    cin >> N;

    for (int i = 1; i <= N; i++) {
        int n;
        cin >> n;

        printf("Case #%d: ", i);

        if (n == 0) {
            cout << "INSOMNIA" << endl;
            continue;
        }

        bool seen[10];
        for (int j = 0; j < 10; j++) {
            seen[j] = false;
        }
        int count = 0;
        int mult = 1;

        int result;
        while (count < 10) {
            int x = n * mult;
            result = x;
            mult++;

            while (x != 0) {
                int d = x % 10;
                if (seen[d] == false) {
                    count++;
                    seen[d] = true;
                }
                x /= 10;
            }
        }

        cout << result << endl;

    }
    return 0;
}
