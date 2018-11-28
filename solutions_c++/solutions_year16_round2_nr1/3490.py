#include <cstdio>
#include <iostream>
#include <cassert>
#include <cctype>
#include <cfloat>
#include <climits>
#include <cstring>
#include <bitset>
#include <deque>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <vector>
#include <algorithm>
#include <string>
#include <climits>
#include <cmath>

#define  each(v,c)  for(typeof((c).begin()) v = (c).begin(); v != (c).end(); ++v)
#define  sync(x)    ios_base::sync_with_stdio(x)
#define  sz(a)      ((int)(a.size()))
#define  all(a)     (a).begin(), (a).end()
#define  pb         push_back
#define  mp         make_pair
#define  fi         first
#define  se         second
using namespace std;

#define debug(a,n)    cerr << "["; for(int i = 0; i < n; ++i) cerr << a[i] << " ";cerr << "\b]\n";
#define dbg(args...)  {debug1,args; cerr<<endl;}
#define pause()       cin.get();cin.get();

struct debugger {
    template<typename T> debugger& operator , (const T& v) {
        cerr<<v<<" "; return *this;
    }
} debug1;

template <typename T1, typename T2>
inline ostream& operator << (ostream& os, const pair<T1, T2>& p) {
    return os << "(" << p.first << ", " << p.second << ")";
}

template<typename T>
inline ostream &operator << (ostream & os,const vector<T>& v) {
    bool first = true; os << "[";
    for (typename vector<T>::const_iterator ii = v.begin(); ii != v.end(); ++ii) {
        if(!first) os << ", ";
        os << *ii; first = false;
    }
    return os << "]";
}

typedef long long LL;
typedef pair<int,int> pii;
typedef pair<int,pii> piii;
typedef vector<int> vi;
const int inf = 0x7fffffff;

string no[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

string inp;
int n;
void solve(int tc){
    cin >> inp;
    n = sz(inp);

    // dbg("done",n);
    map<char,int> Map;
    map<char,int> :: iterator it;
    for(int i = 0; i < n; ++i)
        Map[inp[i]]++;

    queue<pair<string,map<char,int> > > q;
    set<pair<string,map<char,int> > > ss;

    q.push(mp("",Map));

    // dbg("running");
    cout << "Case #" << tc << ": ";
    while(!q.empty()){
        string cur = q.front().fi;
        Map = q.front().se;

        if (ss.find(q.front()) != ss.end())
            continue;
        ss.insert(q.front());
        q.pop();

        bool flag = true;
        for(it = Map.begin(); it != Map.end(); ++it){
            if (it->second != 0){
                flag = false;
                break;
            }
        }

        // dbg("looping",cur,cur.size());
        
        if (flag){
            cout << cur << "\n";
            return;
        }

        int num = (cur.size() == 0 ? 0 : int(cur[cur.size()-1]-48));
        for(int i = num; i <= 9; ++i){
            map<char,int> temp = Map;
            string temp_str = cur;
            bool flag = true;
            for(int k = 0; k < no[i].size(); ++k){
                if (temp[no[i][k]] > 0)
                    temp[no[i][k]]--;
                else {
                    flag = false;
                    break;
                }
            }

            if (flag){
                temp_str.pb((char)(i+48));
                q.push(mp(temp_str,temp));
            }
        }
    }
}

int main(int argc, char **argv)
{
    int tc;
    cin >> tc;
    for(int i = 1; i <= tc; ++i)
        solve(i);
    return 0;
}
