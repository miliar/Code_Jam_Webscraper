#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iomanip>
#include <list>

using namespace std;
#define deb(a) cout<<#a<<":"<<a<<endl;

int go(int a, vector<int> &motes) {
    if(a== 1) {
        return motes.size();
    }

    if(motes.size() == 0) {
        return 0;
    }

    int c1, c2;

    vector<int> m(motes.begin()+1, motes.end());
    if(a > motes[0]) {
        return go(a+motes[0], m);
    }

    c1 = 1 + go(a, m);

    int tmp = a;
    int oper=0;
    while(1) {
        tmp += tmp -1;
        oper++;
        if(tmp > motes[0]) {break;}
    }

    c2 = oper + go(tmp+motes[0], m);

    return min(c1, c2);
}

int main() {
    string ln;
    int T;

    cin>>T;
    getline(cin, ln);

    for(int t=1; t<=T; t++) {
        int a, n, ans;
        vector<int> motes;
        cin>>a>>n;

        int x;
        for(int i=0; i<n; i++) {
            cin>>x;
            motes.push_back(x);
        }

        sort(motes.begin(), motes.end());
        ans = go(a, motes);
        
        cout<<"Case #"<<t<<": "<<ans<<endl;
    }
    return 0;
}
