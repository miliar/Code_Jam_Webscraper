#include <vector>
#include <cstdio>
#include <iostream>
#include <string>
#include <list>

#define BUFSIZE 10000
typedef long long int LLI;

using namespace std;

string tag(int i) {
    static char buf[BUFSIZE];
    sprintf(buf, "Case #%d: ", i + 1);
    return string(buf);
}

string solve(string s) {
    list<char> lis;
    lis.push_back(s[0]);
    for (int i = 1; i < s.size(); ++i) {
        char c = s[i];
        if (lis.front() <= c) {
            lis.push_front(c);
        } else {
            lis.push_back(c);
        }
    }

    string res = "";
    for (auto it = lis.begin(); it != lis.end(); ++it) {
        res += *it;
    }
    return res;
}

int main(int argc, char *argv[]) {
    char buf[BUFSIZE];
    int num;

    fgets(buf, BUFSIZE, stdin);
    num = atoi(buf);
    
    for (int i = 0; i < num; ++i) {
        fgets(buf, BUFSIZE, stdin);
        buf[strlen(buf)-1] = 0;
        cout << tag(i) << solve(buf) << endl;
    }
    return 0;
}
