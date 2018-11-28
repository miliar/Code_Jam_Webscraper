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


void Do(int t, fstream &cin, fstream &cout) {
    
    string str;
    cin >> str;
    string res;
    res.push_back(str[0]);
    for (int i = 1; i < str.size(); ++i) {
        if (str[i] >= res[0]) {
            res = str[i] + res;
        }
        else {
            res = res + str[i];
        }
        
    }
    cout << "Case #" << t << ": " << res << endl;
}
int main(int argc, char* argv[])
{
    std::ios::sync_with_stdio(false);
    
    fstream cout("/Users/a-voronin/xcode/CompetitionGeneral/CompetitionGeneral/out.txt",fstream::out);
    fstream cin("/Users/a-voronin/xcode/CompetitionGeneral/CompetitionGeneral/in.txt",fstream::in);
    int t;
    cin >> t;
    
    for (int i = 0; i < t; ++i) {
        Do(i + 1, cin, cout);
    }
    return 0;
}