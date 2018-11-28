#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

void flip(string &s) {
    for(char &c : s) c == '-' ? c = '+' : c = '-';
}

int main()
{
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        string s;
        cin >> s;
        int answer = 0;
        while(s.size() > 0) {
            if(s.back() == '-') {
                answer++;
                flip(s);
            }
            s.pop_back();
        }
        cout << "Case #" << t << ": " << answer << endl;
    }
    return 0;
}
