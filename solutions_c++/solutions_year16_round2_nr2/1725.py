#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<cstdlib>

typedef long long ll;
typedef unsigned long long ull;

using namespace std;

bool sedi(int c, string x) {
    for (int i = x.size()-1; i>=0; --i) {
        if (x[i] == '?') c/=10;
        else if (c%10+'0' != x[i]) return false;
        else c /= 10;
    }
    return c == 0;
}

pair<int, int> brut(string c, string j) {
    vector<int> cv, jv;
    for (int i = 0; i<1000; ++i) {
        if (sedi(i, c)) {
            cv.push_back(i); 
        }
        if (sedi(i, j)) {
            jv.push_back(i);
        }
    }
    int minr = 2000, minc = 1000, minj = 1000;
    for (unsigned i = 0; i<cv.size(); ++i) {
        for (unsigned j = 0; j<jv.size(); ++j) {
            if (abs(cv[i]-jv[j]) < minr) {
                minr = abs(cv[i]-jv[j]);
                minc = cv[i];
                minj = jv[j];
            }
        }
    }
    return make_pair(minc, minj);
}

int main() {
    int T;
    cin>>T;
    for (int t = 0; t<T; ++t) {
        string c,j;
        cin>>c>>j;
        cout<<"Case #"<<t+1<<": ";
        auto ret = brut(c,j);
        string cs = to_string(ret.first);
        string js = to_string(ret.second);
        for (int i = cs.length(); i<c.length(); ++i) cs = "0" + cs;
        for (int i = js.length(); i<j.length(); ++i) js = "0" + js;
        cout<<cs<<" "<<js<<"\n";
    }
    
    return 0;
}
