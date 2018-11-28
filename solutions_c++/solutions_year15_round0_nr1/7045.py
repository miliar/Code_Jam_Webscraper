#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int t, ss;
    string str;
    cin >> t;
    for(int n = 1; n <= t; ++n) {
        cin >> ss >> str;
        int need = 0;
        int count = 0;
        for(int s = 0; s <= ss; ++s) {
            if(count >= s) {
                count += str[s] - '0';
            } else {
                need += s - count;
                count = s + str[s] - '0';
            }
        }
        cout << "Case #" << n << ": " << need << endl;
    }
    return 0;
}
