/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
 * Created By : Vishwas Tripathi 
 * CSE, MNNIT-ALLAHABAD 
 * vishfrnds@gmail.com
 _._._._._._._._._._._._._._._._._._._._._.*/


#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <cstring>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <set>
#include <assert.h>
using namespace std;

#define MP make_pair
#define pb push_back
#define rep(i,n) for(i=0;i<n;i++)
#define REP(i,a,b) for(i=a;i<=b;i++)
#define PER(i,a,b) for(i=b;i>=a;i--)
#define X first
#define Y second
#define all(c) c.begin(),c.end() //eg sort(all(v));

#define tr(c, itr) for(itr = (c).begin(); itr != (c).end(); itr++)
#define present(container, element) (container.find(element) != container.end()) //for set,map,etc
#define cpresent(container, element) (find(all(container),element) != container.end()) //for vectors

 typedef long long ll;
 typedef vector<int> vi; 
 typedef vector< vi > vvi; 
 typedef pair< int,int > ii; 

#define sz(a) int((a).size())
#define clr(a) memset(a,0,sizeof(a))
#define ini(a) memset(a,-1,sizeof(a))


//i/o
#define inp(n) scanf("%d",&n)
#define inp2(n,m) inp(n), inp(m)
#define ins(s) scanf("%s",s);
#define out(n) printf("%d\n",n)
#define out2(n,m) printf("%d %d\n",n,m)
#define inc(n) scanf("%c",&n)

#define inll(n) scanf("%lld",&n)
#define inll2(n,m) scanf("%lld%lld",&n,&m)
#define outll(n) printf("%lld\n",n)
#define outll(n) printf("%lld\n",n)
#define outll2(n,m) printf("%lld %lld\n",n,m)



//cost
#define MOD 1000000007
#define MOD_INV 1000000006
#define MAX 100009
#define INF 999999999

#define chk(a) cerr << endl << #a << " : " << a << endl
#define chk2(a,b) cerr << endl << #a << " : " << a << "\t" << #b << " : " << b << endl
#define chk3(a,b,c) cerr << endl << #a << " : " << a << "\t" << #b << " : " << b << "\t" << #c << " : " << c << endl
#define chk4(a,b,c,d) cerr << endl << #a << " : " << a << "\t" << #b << " : " << b << "\t" << #c << " : " << c << "\t" << #d << " : " << d << endl

int main()
{
	int t;
	inp (t);
	for (int testCase = 1; testCase <= t; testCase++) {
		int d, mx = 0, ans = 99999999;
		cin >> d;
		int arr[d];
		for (int i = 0; i < d; i++) {
			cin >> arr[i];
			mx = max(mx, arr[i]);
		}
		for (int i = 1; i <= mx; i++) {
			int tans = 0;
			for (int j = 0; j < d; j++) {
				tans += (arr[j] - 1) / i;
			}
			tans += i;
			ans = min(ans, tans);
		}
		cout << "Case #" << testCase <<": " << ans << "\n";
	}
    return 0;
}
