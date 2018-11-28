#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main(int argc, char **argv)
{
        int T;
        cin >> T;
        for (int t = 0; t < T; t++) {
                string s, u;
                cin >> s;
                for (size_t i = 0; i < s.size(); i++) {
                        if (!i) {
                                u += s[i];
                                continue;
                        }
                        if (u[0] <= s[i])
                                u = s[i] + u;
                        else
                                u = u + s[i];
                }
                cout << "Case #" << t+1 << ": " << u << endl;
        }
        return 0;
}
