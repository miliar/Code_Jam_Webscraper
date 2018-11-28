#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <algorithm>
#include <functional>
#include <numeric>
#include <sstream>
#include <iostream>
#include <iomanip>
#include<cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include<queue>

using namespace std;

typedef pair<int, int> pii;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vll;
typedef vector<vll> vvll;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef double ld;
typedef vector<ld> vld;


#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define fore(i, a, n) for(int i = (int)(a); i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) int(a.size() - 1)
#define all(a) a.begin(), a.end()
#define fornl(i,n)   for(ll i=0;i<n;i++)
#define len			  size()
#define s(n)          scanf("%d",&n);
#define slld(n)       scanf("%lld",&n);
#define sf(n)         scanf("%lf",&n);
#define ss(n)         scanf("%s",n);
#define MEM(a,b)      memset(a,(b),sizeof(a))  //memset(arr,0,sizeof(arr))
#define MOD           1000000007
#define nl cout<<"\n";

    const long double EPS = 1E-9;
    const int INF = (int) 1E9;
    const ll INF64 = (ll) 1E18;

    int main() {
    	freopen ("input.in", "r", stdin);
	freopen ("output.txt", "w", stdout);
    	int t;
    	cin>>t;
    
    	forn(i,t) {
    		cout<<"Case #"<<i+1<<": ";
    		vi v1;
    		int n;
    		cin>>n;
    		n--;
    		forn(i,4) {
    			forn(j,4) {
    				int p;
    				cin>>p;
    				if(i==n) v1.pb(p);
    			}
    		}
    		vi v2;
    		cin>>n;
    		n--;
    		forn(i,4) {
    			forn(j,4) {
    				int p;
    				cin>>p;
    				if(i==n) v2.pb(p);
    			}
    		}
    		sort(all(v1)); sort(all(v2));
    		int tot=0,ans=-1;
    		forn(i,v1.size()) {
    			forn(j,v2.size()) {
    				if(v1[i]==v2[j]){
    					tot++;
    					ans=v1[i];
    				}
    			}
    		}
    		
    		if(tot>1) {
    			cout<<"Bad magician!";
    		}
    		else if (tot==1) {
    			cout<<ans;
    		}
    		else if(tot==0) {
    			cout<<"Volunteer cheated!";
    		}
    		nl
    	}
    	  //fclose (stdout);
			//  fclose (stdin);

    }


