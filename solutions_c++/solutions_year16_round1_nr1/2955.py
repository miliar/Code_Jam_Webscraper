#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

#define pb              push_back
#define sz              size
#define PII             pair <int,int>
#define PLL             pair <ll,ll>
#define mp              make_pair
#define xx              first
#define yy              second
#define all(v)          v.begin(),v.end()

#define CLR(a)          memset(a,0,sizeof(a))
#define SET(a)          memset(a,-1,sizeof(a))

#define eps             1e-9
#define PI              acos(-1.0)
#define INF             1000000000

/******************************************************************************************/

string s,r;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T,t,i;
    cin >> T;
    for(t=1;t<=T;t++){
        cin >> s;
        r = "";
        for(i=0;i<s.size();i++){
            if(s[i]>=r[0]) r = s[i] + r;
            else r = r + s[i];
        }
        cout << "Case #" << t << ": " << r << endl;
    }
    return  0;
}
