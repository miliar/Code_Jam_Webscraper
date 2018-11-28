#include <iostream>
#include <sstream>
#include <utility>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
#include <cstdio>
#include <climits>

using namespace std;

#define FOR(i, b, e)    for(int i = (b), d((e) < (b) ? -1 : 1), n((e) < (b) ? (e) - 1 : (e) + 1); i != n; i += d)
#define REP(i, n)       for(int i = 0; i < (n); i++)
#define DV(v)           for(auto e : (v)){cout << e << " ";} cout << endl
#define PB(e)           push_back((e))
#define CS(v)           cout << "Case #" << (case_num++) << ": " << (v) << endl
#define ALL(e)          (e).begin(), (e).end()
#define SZ              size()

typedef stringstream        SS;
typedef vector<int>         VI;
typedef pair<int, int>      PII;
typedef vector<string>      VS;
typedef map<string, int>    MSI;

template <class T>
inline string toStr(const T& i){
    ostringstream os("");
    os << i; 
    return os.str(); 
}

ostream &operator<<(ostream &os, const PII &p){
    os << "(" << p.first << ", " << p.second << ")";
    return os;
}

vector<string> &strTok(const string &s, const string &t){
    int b = 0, e = s.SZ, z = t.SZ;
    vector<string> *v = new vector<string>();
    while(1){
        int n;
        if(b >= e) break;
        n = s.find(t, b);
        if(n != b) v->PB(s.substr(b, (n == -1 ? e : n) - b));
        if(n == -1) break;
        b = n + z;
    }
    return *v;
}

int case_num = 1;

void main_(){
    set<int> st[2];
    vector<int> rst(4);
    vector<int>::iterator it;
    REP(i, 2){
        int L;
        cin >> L;
        REP(j, 4){
            REP(k, 4){
                int tmp;
                cin >> tmp;
                if(j == L - 1) st[i].insert(tmp);
            }
        }
    }
    it = set_intersection(st[0].begin(), st[0].end(), st[1].begin(), st[1].end(), rst.begin());
    int ss = it - rst.begin();
    if(ss == 1) CS(rst[0]);
    else if(ss == 0) CS("Volunteer cheated!");
    else CS("Bad magician!");
}

int main(int argc, char *argv[]){
    int T;
    cin >> T;
    REP(t, T) main_();
    return 0;
}
