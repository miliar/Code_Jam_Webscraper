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
        int x; cin>>x;
        if(x == 0) {
            cout << "INSOMNIA";
        } else {
            set<int> have;
            int y=x;
            while(true) {
                int c = y;
                while(c > 0) {
                    have.insert(c % 10);
                    c /= 10;
                }

                if(have.size() == 10) {
                    break;
                }
                y += x;
            }
            cout << y;
        }
        cout << endl;
    }
}
