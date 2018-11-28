#include <iostream>
#include <string>

using namespace std;

int main() {
    ios_base::sync_with_stdio(0);

    int t;
    cin >> t;

    int s_max, potrz, wstalo;
    string s;
    for(int x = 0 ; x < t ; x++) {
        potrz = 0;
        wstalo = 0;

        cin >> s_max >> s;

        for(int i = 0 ; i <= s_max ; i++)
            s[i] -= '0';

        wstalo += s[0];
        for(int i = 1 ; i <= s_max ; i++) {
            if(s[i] > 0) {
                if(wstalo >= i)
                    wstalo += s[i];
                else {
                    potrz += i - wstalo;
                    wstalo += i - wstalo + s[i];
                }
            }
        }

        cout << "Case #" << x + 1 << ": " << potrz << endl;
    }

    return 0;
}
