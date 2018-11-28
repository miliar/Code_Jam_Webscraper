#include <vector>
#include <cstdio>
#include <iostream>
#include <string>

#define BUFSIZE 10000
typedef long long int LLI;

using namespace std;

string tag(int i) {
    static char buf[BUFSIZE];
    sprintf(buf, "Case #%d: ", i + 1);
    return string(buf);
}

int solve(vector<int> lis) {
    int r = 0;
    int pos = 0;
    int mode = lis[0];

    for (int i = 0; i < lis.size(); ++i) {
        if (mode != lis[i]) {
            r++;
            mode = lis[i];
        }
    }
    if (mode == 0) r++;
    return r;
}

int main(int argc, char *argv[]) {
    char buf[BUFSIZE];
    int num;

    fgets(buf, BUFSIZE, stdin);
    num = atoi(buf);
    
    for (int i = 0; i < num; ++i) {
        vector<int> lis;
        fgets(buf, BUFSIZE, stdin);
        char *p = buf;
        while (*(p+1)) {
            if (*p == '+') {
                lis.push_back(1);
            } else {
                lis.push_back(0);
            }
            p++;
        }
        
        cout << tag(i) << solve(lis) << endl;
    }
    return 0;
}
