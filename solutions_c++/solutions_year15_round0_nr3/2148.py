
/*===============*\
|  ID: TMANDZU    |
|    LANG: C++    |
\*===============*/
//Tornike Mandzulashvili
//std::ios_base::sync_with_stdio (false);

#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <stack>
#include <math.h>
#include <vector>
#include <string>
#include <iomanip>
#include <map>
#include <assert.h>
#include <queue>
#include <iostream>
#include <set>
#include <cstring>
#include <deque>
#include <fstream>
#include <bitset>

#define endl '\n'
#define deb(x) cout << "> " << #x << " : " << (x) << endl;
#define EPS (1e-9)
#define Pi 3.1415926535897932384626433832795028841971
#define hash1 1000003
#define hash2 1000033
#define INF 1000000500
#define pb push_back
#define mp make_pair
#define S size()
#define MX(aa,bb) (aa>bb?aa:bb)
#define MN(aa,bb) (aa<bb?aa:bb)
#define fi first
#define se second
#define PI pair < int , int >
#define REP(i,a,n) for(i=a;i<n;i++)
#define sc scanf
#define big long long
#define VI vector < int >
#define DID (long long)
#define ll long long
#define AL(a) (a).begin(),(a).end()
#define INFF DID INF*INF
#define debug 1

using namespace std;

int g[4][4]={
{
    1,2,3,4
},
{
    2,-1,4,-3
},
{
    3,-4,-1,2
},
{
    4,3,-2,-1
}
};

int mul(int a,int b){
    int x = 0;
    if (a < 0)
        a = -a, x++;
    if (b < 0)
        b = -b, x++;
    a--,b--;
    if (x&1)
        return -g[a][b];
    else
        return g[a][b];
}


const int T = 1e5 + 5;
int A[T],B[T];
int L,X;
string s,ans;

int get(char k){
    if (k=='i')
        return 2;
    if (k=='j')
        return 3;
    return 4;
}

int main(){
    freopen("text.in","r",stdin);  freopen("text.out","w",stdout);

    int t;
    cin>>t;
    for (int tests=1;tests<=t;tests++){
        cin>>L>>X;
        cin>>s;
        ans = "";
        for (int i=0;i<X;i++)
            ans += s;

        A[0]=1;
        int n = ans.S;
     //   cout<<ans.S<<endl;
        B[n+1]=1;
        for (int i = 1;i<=n;i++)
            A[i]=mul(A[i-1],get(ans[i-1]));
        for (int i = n;i>=1;i--)
            B[i]=mul(get(ans[i-1]),B[i+1]);


        bool ok = false;

    //    cout<<A[1]<<" "<<A[2]<<" "<<mul(1,2)<<endl;

        for (int i=1;!ok && i<=n-2;i++)if (A[i]==2){
            int have = 1;
            for (int j =i+1;!ok && j<n;j++){
                have = mul(have, get(ans[j-1]));
     //           cout<<have<<" "<<i<<" "<<j<<endl;
                if (have == 3 && B[j+1]==4)
                    ok = true;
            }
        }

        cout<<"Case #"<<tests<<": "<<(ok ? "YES" : "NO")<<endl;
    }

}





