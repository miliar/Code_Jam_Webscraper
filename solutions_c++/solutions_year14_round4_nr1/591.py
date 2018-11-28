/*===============*\
|  ID: TMANDZU    |
|    LANG: C++    |
\*===============*/
//Tornike Mandzulashvili
//#pragma comment(linker,"/STACK:256000000")
#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <stack>
#include <math.h>
#include <vector>
#include <string>
#include <map>
#include <queue>
#include <iostream>
#include <set>
#include <cstring>
#include <deque>

#define deb(x) cout << "> " << #x << " : " << (x) << endl;
#define EPS 0.000000001
#define Pi 3.1415926535897932384626433832795028841971
#define hash1 1000003
#define hash2 1000033
#define md 1000000007
#define INF ((1<<30)-1)
#define mp make_pair
#define pb push_back
#define S size()
#define MX(aa,bb) (aa>bb?aa:bb)
#define MN(aa,bb) (aa<bb?aa:bb)
#define fi first
#define se second
#define PI pair < ll ,ll  >
#define REP(i,a,n) for(i=a;i<n;i++)
#define sc scanf
#define pt prll f
#define big long long
#define VI vector <ll >
#define DID (long long)
#define ll long long
#define AL(a) (a).begin(),(a).end()
#define INFF DID INF*INF


using namespace std;

const int T=1e5 + 5;


int main(){
    #ifndef ONLINE_JUDGE
        freopen("text.in","r",stdin); freopen("text.out","w",stdout);
    #endif

    int t;
    cin>>t;
    int tt=t;
    while (t--){
        int N,X;
        cin>>N>>X;
        multiset <int> s;
        int a;
        for (int i=0;i<N;i++)
            cin>>a,s.insert(a);
        int ans=0;
        while (s.S){
            ans++;
            int x=*s.rbegin();
            s.erase(s.find(x));
            x=X-x;
            multiset <int> :: iterator it=s.upper_bound(x);
            if (it==s.begin())
                continue;
            it--;
            s.erase(it);
        }
        cout<<"Case #"<<tt-t<<": "<<ans<<endl;
    }

}
