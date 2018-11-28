#include "vector"
#include "string"
#include "set"
#include "map"
#include "sstream"
#include "algorithm"
#include "cmath"
#include "cassert"
#include "iostream"
#include "numeric"
#include "fstream"
#include "queue"
#include <functional>
#include <climits>
#include <cstring>
#include <list>
#include <iomanip>

using namespace  std;

#define int64 long long
#define F(vec, index) for (int index=0; index  < vec.size(); ++index)
#define F2(index, vec) for (int index=0; index  < vec.size(); ++index)
#define F3(index, from, vec) for (int indexfrom + 1; index  < vec.size(); ++index)
/*
5
-
-+
+-
+++
--+-
+++++++-
++++--++-
 */
int Process(string str) {
    // +-++ => +-++
    // +--+-+++ => ---+-+++ => +-++++++ => 2 = 4
    // +--+-+++ => ---+-+++ => +-++++++
    
    // ++++++- =>
    int res = 0;
    cout << "str " << str << endl;
    for (int i = 0; i < str.size() - 1; ++i) {
        if (str[i] != str[i + 1])
            ++res;
    }
    if (str[str.size() - 1] == '-') ++res;
    return res;
    /*for (int i = str.size() - 1; i >= 0; --i) {
    	if (str[i] == '-') {
            if (str[0] == '+') {
                for (int j = 0; j <= i; ++j) {
                    if (str[j] == '-') break;
                    str[j] = '-';
                }
                res++;
            }
            for (int j = 0; j <= i; ++j) {
                if (str[j] == '+') {
                    str[j] = '-';
                }
                else {
                    str[j] = '+';
                }
            }
            reverse(str.begin(), str.begin() + i + 1);
            ++res;
        }
    }*/
    return res;
    
}


int main(int argc, char* argv[])
{
    std::ios::sync_with_stdio(false);
    fstream cout("/Users/a-voronin/xcode/codeJam.txt",fstream::out);
    fstream cin("/Users/a-voronin/xcode/codeJam2.txt",fstream::in);
    
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        std::cout << i << endl;
        string str;
        cin >> str;
        int res = Process(str);
        cout << "Case #" << i + 1 << ": " << res << endl;
    }
    return 0;
}