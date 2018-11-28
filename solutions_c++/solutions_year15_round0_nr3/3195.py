#include <iostream>
#include <fstream>
#include <string>
#include <map>

using namespace std;

ifstream in("C-small-attempt4.in");
ofstream out("output.in");

long long T, X, L;
map<char, int> mp;

string Map[4][4] = {{"1", "i", "j", "k"},
                    {"i", "-1", "k", "-j"},
                    {"j", "-k", "-1", "i"},
                    {"k", "j", "-i", "-1"}};

string mul(string str1, string str2) {
    //string str;
    int tag1 = 1, tag2 = 1;
    int len1 = str1.size(), len2 = str2.size();
    if (str1[0] == '-') tag1 = -1;
    if (str2[0] == '-') tag2 = -1;
    string str;
    if (tag1 * tag2 == -1) str += "-";
    str += Map[mp[str1[len1-1]]][mp[str2[len2-1]]];
    if (str[0] == '-' && str[1] == '-') {
        return str.substr(2, str.size() - 2);
    }
    return str;
}

int main(void) {
    mp['1'] = 0, mp['i'] = 1, mp['j'] = 2, mp['k'] = 3;
    in >> T;
    for (long long k = 1; k <= T; k ++) {
        string str, s;
        out << "Case #" << k << ": ";
        in >> L >> X;
        in >> str;
        //X = X % 16;
        for (long long i = 0; i < X; i ++) {
            s += str;
        }
        //out << s << endl;
        //string s = str + str + str;
        string str1 = "1";
        int pos1 = -1, pos2 = -1;
        for (int i = 0; i < s.size(); i ++) {
            str1 = mul(str1, string(1, s[i]));
            if (str1 == "i") {
                pos1 = i;
                break;
            }
        }
        if (pos1 == -1) {
            out << "NO" << endl;
            continue;
        }
        str1 = "1";
        for (int i = s.size() - 1; i >= 0; i --) {
            str1 = mul(string(1, s[i]), str1);
            if (str1 == "k") {
                pos2 = i;
                break;
            }
        }
        if (pos2 == -1 || pos1 >= pos2) {
            out << "NO" << endl;
            continue;
        }
        str1 = "1";
        for (int i = pos1 + 1; i < pos2; i ++) {
            str1 = mul(str1, string(1, s[i]));
        }
        if (str1 == "j") {
            out << "YES" << endl;
        } else {
            out << "NO" << endl;
        }
    }
    return 0;
}