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


/******************************************************************************************/

string s;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    ll T,t,n,cnt,i,j;
    cin >> T;
    for(t=1;t<=T;t++){
        cin >> s;
        cnt = 0;
        n = s.size();
        for(i=n-1;i>=0;i--){
            if(s[i]=='-'){
                cnt++;
                for(j=i;j>=0;j--){
                    if(s[j]=='-') s[j] = '+';
                    else s[j] = '-';
                }
            }
        }
        cout << "Case #" << t << ": " << cnt << endl;
    }
    return 0;
}
