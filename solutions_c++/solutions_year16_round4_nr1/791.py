#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <set>
#include <map>

#define fii(x,y) for(int i=x;i<y;i++)
#define fjj(x,y) for(int j=x;j<y;j++)
#define fkk(x,y) for(int k=x;k<y;k++)
#define fi(x) fii(0,x)
#define fj(x) fjj(0,x)
#define fk(x) fkk(0,x)
#define eps 0.0000000001
#define inf 1<<28

using namespace std;

typedef long long ll;
typedef vector <int> VI;
typedef vector <VI> VVI;
typedef vector <VVI> VVVI;
typedef vector <ll> VL;
typedef vector <VL> VVL;
typedef vector <double> VD;
typedef vector <VD> VVD;
typedef vector <bool> VB;
typedef vector <VB> VVB;
typedef queue <int> QI;
typedef pair<int,int> PI;
typedef pair<int,PI> PT;
typedef queue<PI> QPI;
typedef priority_queue<PT> QPT;
typedef pair<double,double> PD;

string itc = "PRS";
map<char,int> cti;

string getstring(int v, int level) {
    if (level == 0)
        return string(1,itc[v]);
    
    string left = getstring(v, level - 1);
    string right = getstring((v+1)%3, level - 1);
    if (left < right)
        return left + right;
    return right + left;
}

vector<int> getcount(string& s) {
    vector<int> ans(3,0);
    for (int i = 0; i < s.size(); i++)
        ans[cti[s[i]]]++;
    return ans;
}

string compute() {
    int n;
    cin >> n;
    vector<int> val(3);
    cin >> val[1] >> val[0] >> val[2];
    set<string> candidates;
    for (int i = 0; i < 3; i++) {
        string cand = getstring(i, n);
        vector<int> count = getcount(cand);
        if (count == val)
            candidates.insert(cand);
    }
    if (candidates.size() > 0) 
        return *(candidates.begin());
    return "";
    
}

int main() {
    cti['P']=0;
    cti['R']=1;
    cti['S']=2;
    int nc;
    cin >> nc;
    for (int caso = 1; caso <= nc; caso++) {
        string s = compute();
        cout << "Case #" << caso << ": ";
        if (s.size() == 0)
            cout << "IMPOSSIBLE" << endl;
        else
            cout << s << endl;
    }
}