#include <iostream>
#include <limits>

using namespace std;

int main() {
    int t;
    cin >> t;
    
    for(int i = 1; i <= t; i++) {
        int s_max;
        cin >> s_max;

        string audience;
        getline (cin, audience);

        int n = 0;
        int s = 0;
        int additional = 0;
        for(string::iterator it = audience.begin()+1; it != audience.end(); ++it) {
            if(n < s) {
                additional += s-n;
                n = s;
            }
            n += (*it - '0');
            s++;
            if(s > s_max)
                break;
        }

        cout << "Case #" << i << ": ";
        cout << additional;
        cout << endl;
    }

    return 0;
}

