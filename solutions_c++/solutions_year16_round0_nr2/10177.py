#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <queue>
#include <cmath>
#include <bitset>
#include <set>
#include <iomanip>
#include <cassert>
#include <stack>
#include <ctime>
#include <map>
#include <list>
#include <functional>
#include <complex>
#include <iomanip>

using namespace std;

int main(){
    ifstream cin("/Users/youyurong/Desktop/test.txt");
    ofstream cout("/Users/youyurong/Desktop/out.txt");
    int T;
    cin >> T;
    for (int kase = 0; kase < T; ++kase){
        string s;
        cin >> s;
        int part = 1;
        char prev;
        prev = s[0];
        for (int i = 1; i < s.length(); ++i){
            if (s[i] != prev){
                part++;
                prev = s[i];
            }
        }
        cout << "Case " << "#" << kase + 1 << ": ";
        if (s[s.length() - 1] == '+') cout << part - 1;
        else cout << part;
        cout << endl;
    }
}