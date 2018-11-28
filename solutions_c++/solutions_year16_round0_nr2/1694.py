#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <sstream>

using namespace std;

// unused
/*
void flip(string &s, int i) {
    string dummy;
    for (int j=0; j<i; ++j) {
        s[j] = (s[j] == '+') ? '-' : '+';
        dummy += s[j];
    }

    for (int j=0; j<i; ++j) {
        s[j] = dummy[i-1-j];
    }
}
*/

inline bool is_happy(string s) {
    return (s.find('-') == -1);
}

void trim(string &s) {
    while(s[s.size()-1] == '+') s.erase(s.size()-1);
}

int count_chunks(string s) {
    int ans = 0;
    char last = '0'; // any char apart from + or -

    for(int i=0;i < s.size();++i) {
        if (s[i] != last) {
            last = s[i];
            ++ans;
        }
    }
    return ans;
}

int main()
{

    int t;
    cin >> t;

    for (int c=1; c<=t; ++c)
    {
        string pancake;
        cin >> pancake;
        int answer = 0;

        if (! is_happy(pancake) ) {
            trim(pancake);
            answer = count_chunks(pancake);
        }
        cout << "Case #" << c << ": " << answer << endl;
    }
    return 0;
}
