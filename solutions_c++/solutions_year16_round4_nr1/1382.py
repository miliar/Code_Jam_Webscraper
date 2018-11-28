#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int N, R, P, S;

map<char, string> which;

string how_many(char match, int rounds) {
    char a = which[match][0];
    char b = which[match][1];
    string empty = "";
    if(rounds == 0) {
        empty += match;
        return empty;
    }
    string f = how_many(a, rounds - 1);
    string s = how_many(b, rounds - 1);
    // printf("match = %s, rounds = %d, f = %s, s = %s\n", match.c_str(), rounds, f.c_str(), s.c_str());
    if(f < s) return f + s;
    return s + f;
}

bool are_equal(string a, int P, int R, int S) {
    int pc = 0, rc = 0, sc = 0;
    for(int i = 0; i < a.size(); ++i) {
        char x = a[i];
        if(x == 'P') ++pc;
        else if(x == 'R') ++rc;
        else if(x == 'S') ++sc;
    }
    // printf("pc = %d, rc = %d, sc = %d, P = %d, R = %d, S = %d\n", pc, rc, sc, P, R, S);
    if(pc == P && rc == R && sc == S)
        return true;
    return false;
}

bool is_string_good(string a) {
    string temp = a;
    while(temp.size() > 1) {
        string temp1 = "";
        for(int i = 0; i < temp.size() / 2; ++i) {
            int pos_a = i * 2;
            int pos_b = pos_a + 1;
            char a = temp[pos_a];
            char b = temp[pos_b];

            if(a == b)
                return false;
            if(a == 'P' && b == 'R') temp1 += 'P';
            if(a == 'R' && b == 'P') temp1 += 'P';
            if(a == 'R' && b == 'S') temp1 += 'R';
            if(a == 'S' && b == 'R') temp1 += 'R';
            if(a == 'P' && b == 'S') temp1 += 'S';
            if(a == 'S' && b == 'P') temp1 += 'S';
        }
        temp = temp1;
    }
    return true;
}

string check_str(int P, int R, int S) {
    string x = "";
    for(int i = 0; i < P; ++i) x += 'P';
    for(int i = 0; i < R; ++i) x += 'R';
    for(int i = 0; i < S; ++i) x += 'S';
    bool found = false;
    do {
        if(is_string_good(x)) {
            // printf("%s\n", x.c_str());
            found = true;
            break;
        }
    } while(next_permutation(x.begin(), x.end()));
    if(!found)
        return "IMPOSSIBLE";
    return x;
}

int main() {
    int T;
    scanf("%d", &T);
    which['P'] = "PR";
    which['R'] = "RS";
    which['S'] = "PS";
    for(int test = 1; test <= T; ++test) {
        printf("Case #%d: ", test);
        scanf("%d %d %d %d", &N, &R, &P, &S);

        string res = "";
        // res = check_str(P, R, S);
        // printf("%s\n", res.c_str());
        // continue;

        string a = how_many('P', N);
        string b = how_many('R', N);
        string c = how_many('S', N);

        // printf("%s\n", a.c_str());
        // printf("%s\n", b.c_str());
        // printf("%s\n", c.c_str());

        if(are_equal(a, P, R, S)) res = a;
        if(are_equal(b, P, R, S)) {
            if(res == "")
                res = b;
            else
                res = res > b ? b : res;
        }
        if(are_equal(c, P, R, S)) {
            if(res == "")
                res = c;
            else
                res = res > c ? c : res;
        }

        if(res == "")
            printf("IMPOSSIBLE");
        else
            printf("%s", res.c_str());

        printf("\n");
    }

    return 0;
}
