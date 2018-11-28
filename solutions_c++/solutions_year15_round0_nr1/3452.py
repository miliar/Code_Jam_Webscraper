#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int tc;
    cin >> tc;
    for (int t = 1; t <= tc; t++) {
        cout << "Case #" << t << ": ";
        int n;
        cin >> n;
        string s;
        cin >> s;
        int sum_so_far = 0;
        int additional = 0;
        for (int i = 0; i < s.size(); i++) {
            if (i <= sum_so_far) {
                sum_so_far += s[i] - '0';
            } else {
                int additional_in_this = i - sum_so_far;
                additional += additional_in_this;
                sum_so_far += s[i] - '0';
                sum_so_far += additional_in_this;
            }
        }
        cout << additional << endl;
    }

}
