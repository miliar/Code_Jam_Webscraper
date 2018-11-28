#include <map>
#include <set>
#include <cmath>
#include <stack>
#include <queue>
#include <cstdio>
#include <vector>
#include <cstring>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

#define rep(i,n) for(int i=0; i<n; i++)
#define fr(i,a,b) for(int i=a; i<=b; i++)
#define debug(a) cout<< #a << " = " <<a<<endl;

#define ff first
#define ss second
#define mp make_pair
#define pb push_back

#define MaxInt 2147483647
#define INF 12512523232344LL
#define pi 3.1415926535897932

#define read(a) scanf("%d",&a);
#define read2(a,b) scanf("d",&a,&b);
#define read3(a,b,c) scanf("d%d",&a,&b,&c);

double T, C,F,X;
int cnt= 0 ;
double Fs =2.0;
double ans;

int main(){

    #ifndef ONLINE_JUDGE
    freopen("INPUT.INP", "r", stdin);
    freopen("OUTPUT.OUT", "w", stdout);
    #endif // ONLINE_JUDGE

    cin>>T;
    fr(Tc,1,T)
    {
        ans = 0.0;
        cin>>C>>F>>X;

        Fs = 2.0;
        while(1)
        {
            if(C/Fs + X/(Fs+F) >= X/Fs)
            {
                ans += X/Fs;
                break;
            }
            else
            {
                ans += C/Fs;
            }

            Fs+=F;
        }
        printf("Case #%d: %.7lf\n",Tc,ans);
    }

return 0;
}
