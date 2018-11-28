#include <algorithm>
#include <cmath>
#include <cstring>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

#define pb push_back
#define puts(x) cout << #x << " : " << x << endl;
#pragma GCC diagnostic ignored "-Wconversion"

#define REP(i,n) for (int i=0;i<(n);i++)
#define REPE(i,n) for (int i=0;i<=(n);i++)

#define init(a,b) memset((a), (b), (sizeof(a)));

#define PI 3.14159265
#define EPS (1e-10)
#define EQ(a,b) (abs((a)-(b)) < EPS)

using namespace std;

typedef long long ll;
typedef pair<int, int> P;

int main() {
    int n;cin>>n;
    for(int i=0;i<n;i++){
        ll c;
        cin>>c;
        ll original = c;
        set<int> st;
        for(int j=0;j<1000;j++){
            if(c==0)break;
            stringstream ss;
            string s;
            ss<<c;
            ss>>s;
            for(int k=0;k<s.size();k++)
                st.insert(s[k]-'0');
            if(st.size() == 10) break;
            c += original;
        }
        if(st.size() == 10)
            printf("Case #%d: %lld\n", i+1, c);
        else
            printf("Case #%d: INSOMNIA\n", i+1);
    }
    return 0;
}
