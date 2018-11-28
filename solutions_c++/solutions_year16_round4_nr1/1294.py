#include <iostream>
#include <string>
#include <vector>
#include <stdio.h>
#include <queue>
#include <set>
#include <algorithm>
using namespace std;

string help(string s)
{
    string res;
    int len = s.size();
    if (len == 2)
    {
        sort(s.begin(), s.end());
        return s;
    }
    if (len == 1)   return s;
    string s1 = help(s.substr(0, len / 2));
    string s2 = help(s.substr(len / 2, len / 2));
    if (s1 <= s2)
        res =  s1 + s2;
    else
        res =  s2 + s1;
    return res;
}

int main() {
    int T, test_num = 0;
    cin>>T;
    while (T--) {
        test_num++;
        int N, R, P, S;
        cin>>N>>R>>P>>S;
        vector <string > code;
        int cp = 1, cr = 0, cs = 0, np = 1, nr = 0, ns = 0;
        for (int i = 0; i < N; i++) {
            np += cs;
            ns += cr;
            nr += cp;
            cp = np;
            cs = ns;
            cr = nr;
        }
        char be;
        //printf("%d %d %d\n", cp, cs, cr);
        if (cp == P && cs == S && cr == R)
            be = 'P';
        else if (cp == R && cs == P && cr == S)
            be = 'R';
        else if (cp == S && cs == R && cr == P)
            be = 'S';
        else {
            printf("Case #%d: IMPOSSIBLE\n", test_num);
            continue;
        }
        for (int i = 0; i < N + 1; i++) {
            //int cnt_p = 0, cnt_r = 0, cnt_s = 0;
            if (i == 0) {
                //vector <char> single;
                string single;
                single.push_back(be);
                code.push_back(single);
               // cnt_p++;
            }
            else {
                //vector <char> single;
                string single;
                for (int j = 0; j < code[i - 1].size(); j++) {
                    if (code[i - 1][j] == 'P')
                    {
                        single.push_back('P');
                        single.push_back('R');
                    }
                    else if (code[i - 1][j] == 'R') {
                        single.push_back('R');
                        single.push_back('S');
                    }
                    else if (code[i - 1][j] == 'S') {
                        single.push_back('S');
                        single.push_back('P');
                    }
                }
                code.push_back(single);
            }
        }
        //cout<<code.size()<<endl;
        /*for (int i = 0; i < code.size(); i++)
        {
             for (int j = 0; j < code[i].size(); j++)
                cout<<code[i][j] << " ";
             cout<<endl;
        }*/
        string res = help(code[N]);
        printf("Case #%d: %s\n", test_num, res.c_str());
    }
    return 0;
}
