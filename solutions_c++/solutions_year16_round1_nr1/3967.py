
#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<string>
#include<bitset>
#include<vector>
#include<deque>
#include<queue>
#include<stack>
#include<map>
#include<functional> //highest
#include<algorithm>	//sort, heap etc.
#include<utility>	//pair

using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef stack<int> si;
typedef queue<int> qi;
typedef pair<int,int> ii;
typedef pair<int,ii> iii;
typedef vector<vi> vvi;
typedef vector<ii> vii;
typedef vector<vii> vvii;
typedef vector<iii> elst;

#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define ABS(a,b) ((a) < (b) ? (b)-(a) : (a)-(b))

#define FORN(i,j,n) for(int i=j;i<(int)n;i++)
#define forn(i,n) FORN(i,0,n)
#define pb(x) push_back(x)
#define mp(x,y) make_pair((x),(y))
#define sz size()
#define ff first
#define ss second
#define pq priority_queue
#define all(x) (x).begin(),(x).end()
#define mlc(t,n) ((t*)malloc(n*sizeof(t)))
#define mset(m,v) memset(m,v,sizeof(m))

#define INF 1000000000
#define M 1000000007

//---------------------------------------------//
void count() {
 
    string i,o;
    cin >> i;
    o = i[0];
    
    for(int j =1;j<i.length();j++){ 
    if(o[0] > i[j]){
        o = o + i[j];
    } else { 
    o = i[j] + o;
    } 
    }
	cout << o << endl;
 return;
}

int main() {
	// freopen("/storage/sdcard0/CppDroid/projects/Codejam/1A/ain.txt", "r", stdin);
 //freopen("/storage/sdcard0/Download/A-small-attempt0.in", "r", stdin);
 freopen("/storage/sdcard0/Download/A-large.in", "r", stdin);
    
freopen("/storage/sdcard0/CppDroid/projects/Codejam/1A/aout.txt","w", stdout);

	int T;
	scanf("%d",&T);

	for(int t=1;t<=T;t++) {
		printf("Case #%d: ", t);
 count();
        	}
 return 0;
}

