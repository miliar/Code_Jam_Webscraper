#include<iostream>
#include<string>
using namespace std;

int main()
{
    int t = 0;
    while (cin >> t) {
        for (int i = 0; i < t; i++) {
            int max_level = 0;
            cin >> max_level;
            string s;
            cin >> s;
            int to_invite = 0;
            int current_sum = s[0] - '0';
            for (int current_level = 1; current_level <= max_level; current_level++) {
                if (current_sum < current_level) {
                    to_invite += current_level - current_sum;
                    current_sum += current_level - current_sum;
                }
                current_sum += s[current_level] - '0';
            }
            cout << "Case #" << i+1 << ": " << to_invite << endl;
        }
    }
    return 0;
}
