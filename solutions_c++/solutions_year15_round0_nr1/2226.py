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
    ofstream op;
    op.open("out.txt");
    ifstream ip;
    ip.open("A-large.in");
    int t,n;
    ip >> t;
    char ip1[10000];
    rep(i,t){
    	int result = 0;
    	int temp = 0;
    	ip >> n >> ip1;
    	temp = ip1[0] - '0';
    	rep(j,n){
    		if(j+1 > temp){
    			result += (j + 1 - temp);
    			temp = j+1;
    		}
    		temp += ip1[j+1] - '0';
    	}
    	op << "Case #" << i+1 << ": " << result << endl;
    	
    }
    return 0;
}


