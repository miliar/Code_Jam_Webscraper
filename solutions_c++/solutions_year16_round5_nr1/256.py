#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

#define For(i,a,b) for(int i = a; i < b; i++)
#define rep(i,x) For(i,0,x)
#define foreach(i,c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define sz(x) ((int)(x).size())
#define F first
#define S second
#define pb push_back
#define mp make_pair
#define TWO(x) (1LL<<(x))

using namespace std;


int main() {
    int np; cin>>np;
    rep(i, np){
        cout << "Case #"<<(i+1)<<": ";

        set<pair<int, bool> > a;

        vector<int> todo;

        string s; cin>>s; 
        bool prev = false;
        rep(i, sz(s)) {
            bool cur = (s[i] == 'C');
            a.insert(mp(i, cur));
            if(cur == prev) {
                todo.push_back(i);
            }
            prev = cur;
        }

        int cnt = 0;
        while(sz(todo)) {
            vector<int> todo2;
            for(int x : todo) {
                auto it = a.lower_bound(mp(x, false));
                if(it == a.end()) {
                    continue;
                }
                rep(i, 2) {
                    auto it2 = it;
                    if(i == 0) {
                        it2++;
                        if(it2 == a.end()) {
                            continue;
                        }
                    } else {
                        if(it2 == a.begin()) {
                            continue;
                        }
                        it2--;
                    }
                    if(it->second == it2->second) {
                        todo2.push_back(it->first);
                        a.erase(it); 
                        a.erase(it2);
                        cnt += 10;
                        break;
                    }
                }
            }
            todo = todo2;
        }

        cnt += (a.size()/2) * 5;

        cout << cnt <<endl;
    }
}
