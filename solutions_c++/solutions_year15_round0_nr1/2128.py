
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

string s;

bool check(int x){
    for (int i=0;i<s.S;i++){
        if (x >= i){
            x += s[i] - '0';
        }else
            return 0;
    }
    return 1;
}

int main(){
    freopen("text.in","r",stdin);  freopen("text.out","w",stdout);

    int t;
    cin>>t;
    for (int tests=1;tests<=t;tests++){
        int n;
        cin>>n;
        cin>>s;
        n++;

        int l = 0;
        int r = 1000000000;

        while (l<r){
            int m = (l+r)>>1;
            if (check(m))
                r = m;
            else
                l = m + 1;

            if (r == l+1)
                if (check(l))
                r--;
            else
                l++;
        }
        int ans;
        ans = l;

        cout<<"Case #"<<tests<<": "<<ans<<endl;
    }

}





