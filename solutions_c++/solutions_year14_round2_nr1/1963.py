// 1A_A.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <math.h>

using namespace std;

vector <char> getPortrait (const string& s) {
    vector <char> portrait;
    portrait.push_back (s [0]);
    for (int i = 1; i < s.length (); ++i) {
        if (s [i] != s [i - 1]) {
            portrait.push_back (s [i]);
        }
    }
    return portrait;
}

void addString (const string& s, const vector <char>& portrait, vector <int>& sum) {
    int pos = 0;
    for (int i = 0; i < s.size (); ++i) {
        if (s [i] != portrait [pos]) {
            ++pos;
        }
        ++sum [pos];
    }
}

int diff (const string& s, const vector <char>& portrait, const vector <int>& sum) {
    int ans = 0;
    int pos = 0;
    int count = 0;
    for (int i = 0; i < s.size (); ++i) {
        if (s [i] != portrait [pos]) {
            ans += abs (sum [pos] - count);
            count = 0;
            ++pos;
        }
        ++count;
    }
    ans += abs (sum [pos] - count);
    return ans;
}

int main(int argc, char* argv[])
{
    freopen ("input.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int t = 0; t < T; ++t) {
        int n;
        cin >> n;
        vector <string> strings;
        for (int i = 0; i < n; ++i) {
            string s;
            cin >> s;
            strings.push_back (s);
        }
        vector <char> portrait = getPortrait (strings.front ());
        bool b = true;
        for (int i = 1; i < n; ++i) {
            vector <char> p = getPortrait (strings [i]);
            if (p.size () != portrait.size ()) {
                b = false;
                break;
            }
            for (int j = 0; j < p.size (); ++j) {
                if (p [j] != portrait [j]) {
                    b = false;
                    break;
                }
            }
            if (!b) {
                break;
            }
        }
        if (!b) {
            cout << "Case #" << t + 1 << ": Fegla Won" << endl;
            continue;
        }
        vector <int> sum (portrait.size ());
        for (int i = 0; i < n; ++i) {
            addString (strings [i], portrait, sum);
        }
        for (int i = 0; i < sum.size (); ++i) {
            double a = (double) sum [i] / n;
            if ((int)(floor (a * 10)) % 10 >= 5) {
                sum [i] = (int)ceil(a);
            }
            else {
                sum [i] = (int)floor(a);
            }
        }
        int answer = 0;
        for (int i = 0; i < n; ++i) {
            answer += diff (strings [i], portrait, sum);
        }
        cout << "Case #" << t + 1 << ": " << answer << endl;
    }
	return 0;
}

