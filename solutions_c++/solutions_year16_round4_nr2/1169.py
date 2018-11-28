#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<cstdio>

using namespace std;

struct token {
    int len;
    string source, ans, pred, chk;

    token(const string &str) {
        int sz = str.size(), pos = 0, start = 0;
        while (pos < sz && str[pos] != ' ') ++pos;
        source = str.substr(start, pos - start);
        pos++;
        start = pos;
        while (pos < sz && str[pos] != ' ') ++pos;
        start += 2;
        ans = str.substr(start, pos - start);
        pos++;
        start = pos;
        while (pos < sz && str[pos] != ' ') ++pos;
        start += 4;
        chk = str.substr(start, pos - start);
        start = pos + 3;
        pred = str.substr(start, sz - start);
        len = max(source.size(), ans.size());
        len = max(len, (int)pred.size());
        len = max(len, (int)chk.size());
    }
};

struct sentence {
    vector<token> sent;
    bool flag;

    friend istream& operator >> (istream &in, sentence &ss) {
        string str = "";
        ss.flag = true;
        ss.sent.clear();
        while (getline(in, str)) {
            if (str.size() == 0) break;
            ss.sent.push_back(token(str));
        }
        for (int i = 0; i < ss.sent.size(); i++) if (ss.sent[i].ans != ss.sent[i].pred) ss.flag = false;
        return in;
    }

    friend ostream& operator << (ostream &out, const sentence &ss) {
        for (int i = 0; i < ss.sent.size(); i++) {
            out << ss.sent[i].source;
            for (int j = ss.sent[i].source.size(); j < ss.sent[i].len; j++) out << ' ';
            if (i == ss.sent.size() - 1) out << endl;
            else out << ' ';
        }
        for (int i = 0; i < ss.sent.size(); i++) {
            out << ss.sent[i].chk;
            for (int j = ss.sent[i].chk.size(); j < ss.sent[i].len; j++) out << ' ';
            if (i == ss.sent.size() - 1) out << endl;
            else out << ' ';
        }
        for (int i = 0; i < ss.sent.size(); i++) {
            out << ss.sent[i].ans;
            for (int j = ss.sent[i].ans.size(); j < ss.sent[i].len; j++) out << ' ';
            if (i == ss.sent.size() - 1) out << endl;
            else out << ' ';
        }
        for (int i = 0; i < ss.sent.size(); i++) {
            out << ss.sent[i].pred;
            for (int j = ss.sent[i].pred.size(); j < ss.sent[i].len; j++) out << ' ';
            if (i == ss.sent.size() - 1) out << endl;
            else out << ' ';
        }
        return out;
    }
};

int main() {
    freopen("../showError.txt", "r", stdin);
    freopen("../showErrorOut.txt", "w", stdout);
    ios::sync_with_stdio(false);
    sentence sent;
    while (cin >> sent) {
        if (!sent.flag) {
            cout << sent << endl;
        }
    }
    return 0;
}
