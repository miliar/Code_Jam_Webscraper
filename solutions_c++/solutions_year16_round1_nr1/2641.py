#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <set>
#include <stack>
#include <deque>
#include <queue>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <iomanip>
#include <climits>
#include <cfloat>
#include <cstdio>
#define x first
#define y second
#define IN(x, n) (0 <= (x) && (x) < n)
#define MAX 1010
#define MOD 1000000007
using namespace std;

typedef long long int entero;
typedef pair<int, int> Point;

string solve(string s){
    vector<char> r;
    r.push_back(s[0]);
    for(int i = 1; i < s.size(); i++){
        if(s[i] >= r[0]){
            r.insert(r.begin(), s[i]);
        }
        else{
            r.push_back(s[i]);
        }
    }
    string t = "";
    for(int i = 0; i < r.size(); i++){
        t+=char(r[i]);
    }
    return t;
}

int main(){
    int casos;
    string s;
    cin >> casos;
    for(int i = 1; i <= casos; i++){
        cin >> s;
        printf("Case #%d: %s\n", i, solve(s).c_str());
    }
	return 0;
}
