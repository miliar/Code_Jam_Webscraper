#include <iostream>
#include <stack>
#include <queue>
#include <bitset>
#include <list>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <cctype>
#include <functional>
#include <utility>
#include <sstream>
#include <iomanip>
#include <ctime>
#include <cassert>
#include <unordered_map>
#include <unordered_set>
using namespace std;

/*
 
 */

unordered_map<string, string> mp;


char get(char s1, char s2, int &neg) {
    if (s1 == '1') return s2;
    if (s2 == '1') return s1;
    if (s1 == s2) {
        neg++;
        return '1';
    }
    if (s1 == 'i' && s2 == 'j') return 'k';
    if (s1 == 'i' && s2 == 'k') {
        neg++;
        return 'j';
    }
    if (s1 == 'j' && s2 == 'k') return 'i';
    if (s1 == 'j' && s2 == 'i') {
        neg++;
        return 'k';
    }
    if (s1 == 'k' && s2 == 'i') return 'j';
    if (s1 == 'k' && s2 == 'j') {
        neg++;
        return 'i';
    }
    return ' ';
}


string multi(char *s, int from, int to) {
    int neg = 0;
    char t =  s[from];
    for (int i = from+1; i < to; i++) {
        t = get(t, s[i], neg);
    }
    string r;
    r.push_back(t);
    if (neg & 1) r = "-" + r;
    return r;
}

string run() {
    long long x, l;
    cin >> x >> l;
    string s;
    cin >> s;
    string ss = "";
    for (int i = 0; i < l; i++) {
        ss += s;
    }
    char str[10005];
    string pre[10005];
    strcpy(str, ss.c_str());
    // preprocess
    char t = str[0];
    pre[0].push_back(t);
    int len = strlen(str);
    int neg = 0;
    for (int i = 1; i < len; i++) {
        t = get(t,str[i],neg);
        if (neg % 2) pre[i].push_back('-');
        pre[i].push_back(t);
    }
    
    if (pre[len-1] == "-1") {
        for (int i = 0; i < len; i++) {
            for (int j = i + 1; j < len; j++) {
                if (pre[i] == "i" && pre[j] == "k") return "YES";
            }
        }
    }
    
    return "NO";
}

int main(int argc, char *argv[]) {
    freopen("C-small-attempt1.in","r",stdin);
    freopen("3.out","w",stdout);
    int t;
    cin >> t;
    int k = 0;
    while (t--) {
        cout << "Case #" << ++k << ": " << run() << endl;
    }	
    return 0;
}