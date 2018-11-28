#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <bitset>
#include <numeric>
#include <utility>
#include <iomanip>
#include <algorithm>
#include <functional>
using namespace std;

typedef long long ll;
typedef vector<int> vint;
typedef vector<ll> vll;
typedef pair<int,int> pint;

#define DE 1
#define FI first
#define SE second
#define PB push_back
#define MP make_pair
#define ALL(s) (s).begin(),(s).end()
#define REP(i,n) for (int i = 0; i < (int)(n); ++i)
#define EACH(i,s) for (typeof((s).begin()) i = (s).begin(); i != (s).end(); ++i)
#define COUT(x) cout<<#x<<" = "<<(x)<<" (L"<<__LINE__<<")"<<endl

template<class T1, class T2> ostream& operator<<(ostream &s, pair<T1,T2> P){return s<<'<'<<P.first<<", "<<P.second<<'>';}
template<class T> ostream& operator<<(ostream &s, vector<T> P) {s<<"{ ";for(int i=0;i<P.size();++i){if(i>0)s<<", ";s<<P[i];}return s<<" }"<<endl;}
template<class T1, class T2> ostream& operator<<(ostream &s, map<T1,T2> P) {s<<"{ ";for(typeof(P.begin()) it=P.begin();it!=P.end();++it){if(it!=P.begin())s<<", ";s<<'<'<<it->first<<"->"<<it->second<<'>';}return s<<" }"<<endl;}



int f, s, num;
bool first[20];

int main() {
	freopen( "C:\\Users\\mistpc\\Dropbox\\Contest\\A-small-attempt1.in.txt", "r", stdin );
    freopen( "C:\\Users\\mistpc\\Dropbox\\Contest\\A.out", "w", stdout );
    
    int T;
    scanf("%d", &T);
    for (int id = 1; id <= T; ++id) {
		memset(first, 0, sizeof(first));
        cin >> f;
		for (int i = 0; i < 16; ++i) {
			cin >> num;
			if ( i >= 4*(f-1) && i < 4*f ) {
				first[num] = true;
			}
		}
		cin >> s;
		vint res;
		for (int i = 0; i < 16; ++i) {
			cin >> num;
			if ( i >= 4*(s-1) && i < 4*s ) {
				if (first[num]) res.PB(num);
			}
		}
        
        printf("Case #%d: ", id);

		if (res.size() == 1) cout << res[0];
		else if (res.size() > 1) cout << "Bad magician!";
		else if (res.size() == 0) cout << "Volunteer cheated!";

        printf("\n");
    }
    
    return 0;
}




