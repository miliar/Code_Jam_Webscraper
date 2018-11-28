#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <bitset>
#include <cmath>
#include <numeric>
#include <iterator>
#include <iostream>
#include <cstdlib>
#include <functional>
#include <queue>
#include <stack>
#include <list>
using namespace std;

int T,N,P,R,S;

char Competitor(char s) {
    if(s=='P') return 'R';
    if(s=='R') return 'S';
    if(s=='S') return 'P';
    return 'e';
}

string SortString(string ss) {
    if(ss.size() == 1 ) return ss;
    //cout << ss << " " <<ss.substr(0,ss.size()/2) << " " <<ss.substr(ss.size()/2,ss.size()) << endl;
    string a = SortString(ss.substr(0,ss.size()/2));
    string b = SortString(ss.substr(ss.size()/2,ss.size()));
    if( a<b ) return a+b;
    else return b+a;
}

string getString(char winner) {
    string res = "";
    res += winner;
    while( res.size() < (1<<N) ) {
        string ret("");
        vector<string> ss;
        for(int i = 0 ; i<res.size(); i++ ) {
            char nowCom = res[i];
            char loser = Competitor(nowCom);
            if( nowCom < loser ) {
                ret += nowCom;
                ret += loser;
            } else {
                ret += loser;
                ret += nowCom;
            }
        }
        res = ret;
        //cout << "***" << res << endl;
    }
    res = SortString(res);
    int p = 0 , r = 0 , s = 0;
    for(int i = 0 ; i < res.size();i++ ) {
        if( res[i] == 'P' ) p++;
        if( res[i] == 'S' ) s++;
        if( res[i] == 'R' ) r++;
        
    }
    //cout << p << " " << r << " " << s << endl;
    //cout << P << " " << R << " " << S << endl;
    if( p==P && R==r && s==S ) return res;
    else return "IMPOSSIBLE";
}

int main() {
    scanf("%d",&T);
    int cases = 1;
    while( T-- ) {
        scanf("%d%d%d%d",&N,&R,&P,&S);
        vector<string> ans;
        string ss = getString('P');
        //cout << "***" << ss << endl;
        if(ss!="IMPOSSIBLE") ans.push_back(ss);
        ss = getString('R');
        //cout << "***" << ss << endl;
        if(ss!="IMPOSSIBLE") ans.push_back(ss);
        ss = getString('S');
        //cout << "***" << ss << endl;
        if(ss!="IMPOSSIBLE") ans.push_back(ss);
        cout << "Case #" << cases++ << ": ";
        if( ans.size() == 0 ) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            sort(ans.begin(),ans.end());
            cout << ans[0] << endl;
        }
    }
    return 0;
}