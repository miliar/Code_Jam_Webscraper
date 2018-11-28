//Data Structure includes
#include<vector>
#include<stack>
#include<set>
#include<bitset>
#include<map>
#include<queue>
#include<deque>
#include<string>


//Other Includes
#include<iostream>
#include<fstream>
#include<algorithm>
#include<cstring>
#include<cassert>
#include<cstdlib>
#include<cstdio>
#include<cmath>

using namespace std;

#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define mp make_pair
#define s(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)
#define sf(n) scanf("%lf",&n)
#define ss(n) scanf("%s",n)
#define fill(a,v) memset(a, v, sizeof a)
#define sz(a) int((a).size())
#define INF (int)1e9
#define EPS 1e-9
#define bitcount __builtin_popcount
#define all(c) (c).begin(), (c).end()
#define maX(a,b) (a>b?a:b)
#define miN(a,b) (a<b?a:b)
#define DREP(a) sort(all(a)); a.erase(unique(all(a)),a.end())
#define INDEX(arr,ind) lower_bound(all(arr),ind)-arr.begin())
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())

typedef vector<int> VI;
typedef vector<vector<int> > VVI;
typedef long long LL;
typedef vector<long long > VLL;
typedef pair<int, int > PII;
typedef vector< PII > VPII;
/* fast Input*/
#define getcx getchar_unlocked
inline void inp( int &n )
{
	n=0;
	int ch=getcx();
	while( ch < '0' || ch > '9' ){ch=getcx();}
	while( ch >= '0' && ch <= '9' )
		n = (n<<3)+(n<<1) + ch-'0', ch=getcx();
}

vector <string> board;
/*Main Code*/
bool row(int c){
	REP(i,4){
		int flag = 1;
		REP(j,4){
			if(board[i][j] !=c && board[i][j] != 'T'){
				flag = 0;
				break;
			}
		}
		if(flag) return true;
	}
	return false;
}

bool column(int c){
	REP(i,4){
		int flag = 1;
		REP(j,4){
			if(board[j][i] != c && board[j][i] != 'T'){
				flag = 0;
				break;
			}
		}
		if(flag) return true;
	}
	return false;
}

bool dia(int c){
	int flag1 = 1;
	REP(i, 4){
		if(board[i][i] != c && board[i][i] != 'T'){
			flag1 =0;
			break;
		}
	}
	if(flag1) return true;

	int flag2 = 1;
	REP(i,4){
		REP(j,4)
		if(i+j == 3){
			if(board[i][j] != c && board[i][j] != 'T'){
				flag2 = 0;
				break;
			}
		}
	}
	if(flag2) return true;

	return false;
}

bool check(int c){
	if( row(c) || column(c) || dia(c)) return true;
	return false;
}

bool nodot(){
	REP(i,4){
		REP(j,4){
			if(board[i][j] == '.') return false;
		}
	}

	return true;
}
int main(){
	int t;
	s(t);
	for(int TC = 1; TC<=t; TC++){
		board.clear();
		string temp;
		REP(i,4){
			cin>>temp;
			board.pb(temp);
		}

		if(check('X')) printf("Case #%d: X won\n",TC);
		else if(check('O'))printf("Case #%d: O won\n",TC);
		else if(nodot())printf("Case #%d: Draw\n",TC);
		else printf("Case #%d: Game has not completed\n",TC);

	}

	return 0;
}
