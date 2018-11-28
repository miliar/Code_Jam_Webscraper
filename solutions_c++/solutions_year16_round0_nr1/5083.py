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

bool st[12];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T,t,x,y,cnt,n;
    cin >> T;
    for(t=1;t<=T;t++){
        cin >> n;
        CLR(st);
        if(n==0){
            cout << "Case #" << t << ": INSOMNIA\n";
            continue;
        }
        cnt = 0;
        for(int i=1;;i++){
            x = n*i;
            while(x){
                y = x % 10;
                x /= 10;
                if(!st[y]){
                    st[y]=1;
                    cnt++;
                }
            }
            if(cnt==10){
                cout << "Case #" << t << ": " << n*i << "\n";
                break;
            }
        }
    }
    return 0;
}
