
#include <array>
#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

array<int, 26> ch;
inline int& gc(char c) {
    return ch[c-'A'];
}

string find_solution(const string & s);

int main() {

    int cases;
    int case_num =0;

    cin >> cases;

    while (cases--) {
        ++case_num;
        string s;
        cin >> s;
        auto solution = find_solution(s);
        cout << "Case #" << case_num << ": ";
        cout << solution << endl;
    }
    return 0;
}

inline int helper(char c, const string & dig) {
    const auto count = gc(c);
    for (auto a : dig)
        gc(a) -= count;
    return count;
}

string find_solution(const string & s){
    fill(ch.begin(), ch.end(), 0);
    for(auto c : s)
        gc(c)++;

    string number;
    number.append(helper('Z', "ZERO"), '0');
    number.append(helper('W', "TWO"), '2');
    number.append(helper('X', "SIX"), '6');
    number.append(helper('G', "EIGHT"), '8');
    number.append(helper('S', "SEVEN"), '7');
    number.append(helper('H', "THREE"), '3');
    number.append(helper('R', "FOUR"), '4');
    number.append(helper('F', "FIVE"), '5');
    number.append(helper('I', "NINE"), '9');
    number.append(helper('O', "ONE"), '1');

    sort(number.begin(), number.end());
    return number;
}
