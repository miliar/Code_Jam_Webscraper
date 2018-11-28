#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <climits>
#include <cfloat>
#include <ctime>
#include <map>
#include <utility>
#include <set>
#include <memory>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>

using namespace std;

#define rep(i,b,e) for(int i=b;i<e;++i)
#define mp make_pair
#define pb push_back
#define all(c) (c).begin(),(c).end()

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;

static const ll Zp = 1000000009;
static const double EPS = 1e-9;

int T;

int main(int argc, char *argv[]) {
    cin>>T;
    for(int t=1;t<=T;++t) {
        int c[16] = {0};
        int f;
        int s;
        cin >> f;
        for (int i=0; i<4; ++i) {
            for (int j=0; j<4; ++j) {
                int v;
                cin >> v;
                if (i==f-1) {
                    c[v-1]++;
                }
            }
        }
        cin >> s;
        for (int i=0; i<4; ++i) {
            for (int j=0; j<4; ++j) {
                int v;
                cin >> v;
                if (i==s-1) {
                    c[v-1]++;
                }
            }
        }
        vector<int> a;
        for (int i=0; i<16; ++i) {
            if (c[i] == 2) a.push_back(i);
        }
        if (a.size()==1) {
            cout<<"Case #"<<t<<": "<<(a.front()+1)<<endl;
        } else if (a.size()==0) {
            cout<<"Case #"<<t<<": "<<"Volunteer cheated!"<<endl;
        } else {
            cout<<"Case #"<<t<<": "<<"Bad magician!"<<endl;
        }
    }
	return 0;
}
