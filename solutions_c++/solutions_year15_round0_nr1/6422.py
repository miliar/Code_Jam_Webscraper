#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
    int T;
    cin >> T;

    for (int t = 0; t < T; t++) {
        int Smax;
        cin >> Smax;

        string str;
        getline(cin, str);

        vector<int> S;

        size_t sum = 0, y = 0;
        for (size_t i = 0; i < str.size(); i++) {
            if (str[i] >= '0' && str[i] <= '9')
                S.push_back(str[i] - '0');
        }

        for (size_t i = 0; i < S.size(); i++) {
           if (S[i] > 0) {
                if (sum < i) {
                    y += i - sum;
                    sum += i - sum;
                }
                sum += S[i];
            }
        }

        cout << "Case #" << t+1 << ": " << y << endl;
    }
}
