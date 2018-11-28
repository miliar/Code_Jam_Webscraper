#include <iostream>
#include <string>
#include <cstring>


using namespace std;


int main()
{
        int nt;
        cin >> nt;
        for (int i = 1; i <= nt; i++) {
                string s;
                cin >> s;
                int ans = -1;
                char cur = '/';
                for (int j = 0; j < s.length(); j++) {
                        if (s[j] != cur) {
                                ans++;
                                cur = s[j];
                        }
                        if (j + 1 == s.length()) {
                                if (s[j] == '-')
                                        ans++;
                        }
                }

                cout << "Case #" << i << ": " << ans << endl;
        }
}
