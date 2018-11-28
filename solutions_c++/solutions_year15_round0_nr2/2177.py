#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<vi> vvi;
typedef pair<int,int> pii;
typedef vector<pii > vii;
typedef vector<pair<int, pair<int, int> > > viii;
typedef pair<ll,ll> pll;
typedef vector<string> vs;
typedef vector<vii> vvii;

#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define MEM(a,b) memset(a,(b),sizeof(a))
#define all(a) a.begin(),a.end()
#define loop(x,a,b) for(int (x) = (a);(x)<(b);(x)++)
#define rep(x,n)   for(int (x)=0;(x)<(n);(x)++)
#define tr(c,it) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define ain(a,n) int ((a)[(n)]); for(int i=0; i<(n); i++) cin>>((a)[i])  
#define md 1000000007
#define MAXN 200005


int main()
{   
    ios::sync_with_stdio(false);
    ofstream myout;
    myout.open("out.txt");
    ifstream myin;
    myin.open("B-large.in");
    int t,n;
    myin >> t;
    rep(i,t){
    	int n;
    	myin >> n;
    	int ip[n];
    	rep(j,n){
    		myin >> ip[j];
    	}
    	int res = 1002;
    	int min;
    	loop(j,1,1002){
    		min = j;
    		rep(k,n){
    			if(ip[k]>j){
    				min += (ceil((float)ip[k]/(float)j)-1);
    			}
    		}
    		if(res>min){
    			res = min;
    		}

    	}
    	myout << "Case #" << i+1 << ": " << res << endl;
    }
    return 0;
}


