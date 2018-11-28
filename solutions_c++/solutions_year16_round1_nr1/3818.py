#include <iostream>
#include <cmath>
#include <map>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

int t;


string generate(string cur, string left) {
    if (left.empty())
        return cur;
    
    string s1 = generate(cur + left[0], left.substr(1));
    string s2 = generate(left[0]+ cur , left.substr(1));
    return max(s1, s2);
}

string calc(string s) {
  //  return generate(string(""), s);
    string cur;
    cur += s[0];
    for (int i = 1; i < s.length(); i++) {
        cur = max(cur+s[i], s[i]+cur);
    }
    return cur;

}

int main() {
    cin >> t;

    for (int i = 1; i <= t; i++) {
        cout << "Case #"<<i<<": ";
        string s;
        cin >> s;

        cout << calc(s) << endl;
    }

    return 0;
}
