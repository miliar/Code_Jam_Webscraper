#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct TDist {
    char type;
    int count;

    TDist(char t = '-', int c = 0)
        : type(t)
        , count(c)
    {
    }
};

void convert(const string& s, vector<TDist>& cur) {
    cur.clear();
    char c = s[0];
    int start = 0;
    int end = 0;
    while (end < s.size()) {
        while (end < s.size() && s[end] == c) {
            ++end;
        }
        cur.push_back(TDist(c, end - start));
        if (end < s.size()) {
            c = s[end];
            start = end;
        }
    }
}

char switch_type(char t) {
    if (t == '-') {
        return '+';
    }
    return '-';
}

void print(const vector<TDist>& cur) {
    for (int i = 0; i < cur.size(); ++i) {
        cout << cur[i].count << cur[i].type;
    }
}

void maneuver(const vector<TDist>& cur, vector<TDist>& new_vec, int count) {
    new_vec.clear();
    for (int i = 0; i < count; ++i) {
        new_vec.push_back(TDist(switch_type(cur[count - i - 1].type), cur[count - i - 1].count));
    }
    for (int j = count; j < cur.size(); ++j) {
        if (j == count) {
            if (new_vec[new_vec.size() - 1].type == cur[j].type) {
                new_vec[new_vec.size() - 1].count += cur[j].count;
            }
        } else {
            new_vec.push_back(cur[j]);
        }
    }
  //cout << "WAS:";
  //print(cur);
  //cout << "; NEW:";
  //print(new_vec);
  //cout << endl;;
}

int main() {
    int t;
    cin >> t;
    string s;
    for (int i = 0; i < t; ++i) {
        cin >> s;
        vector<TDist> cur;
        vector<TDist> new_cur;
        int steps = 0;
        convert(s, cur);
        // print(cur);
        while (cur.size() > 1) {
            if (cur[0].type == '+') {
                maneuver(cur, new_cur, 1);
                ++steps;
                cur = new_cur;
            } else {
                int count_to_swap = cur.size();
                if (cur[cur.size() - 1].type == '+') {
                    --count_to_swap;
                }
                maneuver(cur, new_cur, count_to_swap);
                ++steps;
                cur = new_cur;
            }
        }

        if (cur[0].type == '-') {
            ++steps;
            cur[0].type == '+';
        }
        cout << "Case #" << i + 1 << ": " << steps << endl;
    }
}

