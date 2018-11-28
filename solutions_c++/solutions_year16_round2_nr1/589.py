#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace::std;

void normalize(vector<int>& v, string s, int count)
{
    for (int i = 0; i < s.size(); ++i)
        v[s[i] - 'A'] -= count;
}

int main ()
{
    int T;
    cin >> T;

    for (int t = 0; t < T; ++t)
    {
        string s;
        cin >> s;

        vector<int> v(26, 0);
        for (int i = 0; i < s.size(); ++i)
            ++v[s[i] - 'A'];

        int zero = v['Z' - 'A'];
        normalize(v, "ZERO", zero);
        //cout << "zero = " << zero << endl;

        int six = v['X' - 'A'];
        normalize(v, "SIX", six);
        //cout << "six = " << six << endl;

        int two = v['W' - 'A'];
        normalize(v, "TWO", two);
        //cout << "two = " << two << endl;

        int four = v['U' - 'A'];
        normalize(v, "FOUR", four);
        //cout << "four = " << four << endl;

        int five = v['F' - 'A'];
        normalize(v, "FIVE", five);
        //cout << "five = " << five << endl;

        int seven = v['V' - 'A'];
        normalize(v, "SEVEN", seven);
        //cout << "seven = " << seven << endl;

        int eight = v['G' - 'A'];
        normalize(v, "EIGHT", eight);
        //cout << "eight = " << eight << endl;

        int nine = v['I' - 'A'];
        normalize(v, "NINE", nine);
        //cout << "nine = " << nine << endl;

        int one = v['O' - 'A'];
        normalize(v, "ONE", one);
        //cout << "one = " << one << endl;

        int three = v['T' - 'A'];
        normalize(v, "THREE", three);
        //cout << "three = " << three << endl;

        cout << "Case #" << t + 1 << ": ";
        while (zero > 0) {cout << "0"; --zero;}
        while (one > 0) {cout << "1"; --one;}
        while (two > 0) {cout << "2"; --two;}
        while (three > 0) {cout << "3"; --three;}
        while (four > 0) {cout << "4"; --four;}
        while (five > 0) {cout << "5"; --five;}
        while (six > 0) {cout << "6"; --six;}
        while (seven > 0) {cout << "7"; --seven;}
        while (eight > 0) {cout << "8"; --eight;}
        while (nine > 0) {cout << "9"; --nine;}
        cout << endl;
    }
}
