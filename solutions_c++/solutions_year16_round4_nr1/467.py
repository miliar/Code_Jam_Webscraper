#include "iostream"
#include "cstdio"
#include "cstdlib"
#include "cstring"
#include "cmath"
#include "algorithm"
#include "set"
#include "map"
#include "queue"
#include "vector"
using namespace std;
#define rep(i,n) for(int i=0; i<(n); ++i)
#define repp(i,a,b) for(int i=a; i<a+b; ++i)
#define sz size()
#define X first
#define Y second
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef pair<int,int> pii;
#define maxn 5005


// void sol(int a, int b, int c){
// 	int n = a + b + c;
// 	if(a+b+c==1){
// 		if(a) s[0] = 'S';
// 		if(b) s[0] = 'P';
// 		if(c) s[0] = 'R';
// 		return;
// 	}
// 	int ta,tb,tc;
// 	ta = (a+b-c);
// 	tb = (b+c-a);
// 	tc = (c+a-b);
// 	if(ta < 0 || tb < 0 || tc < 0 || ta&1 || tb&1 || tc&1){
// 		ans = -1;
// 		return;
// 	} 
// 	ta /= 2, tb /= 2, tc /= 2;
// 	sol(ta, tb, tc);
// }

int s[20][maxn];
int cnt[20][3];
void pre(){
	s[0][0] = 0;
	cnt[0][0] = 1;
	rep(i,12){
		int k = 0;
		for(int j=0; j<(1<<i); ++j){
			s[i+1][k++] = s[i][j];
			s[i+1][k++] = (s[i][j]+1)%3;
			cnt[i+1][s[i][j]]++;
			cnt[i+1][(s[i][j]+1)%3]++;
		}
	}
}

char ch[3];
char ans[maxn];

string get(int st, int len){
	if(len==1){
		string res;
		if(ans[st]=='S') res = "S";
		if(ans[st]=='P') res = "P";
		if(ans[st]=='R') res = "R";
		return res;
	}
	string sl = get(st, len>>1);
	string sr = get(st+(len>>1), len>>1);
	if(sl < sr) return sl + sr; else return sr + sl;
}

void run(){
	int a,b,c,n;
	cin >> n >> a >> b >> c;
	rep(i,3){
		int j = (i+1)%3;
		int k = (j+1)%3;
		if(a==cnt[n][i] && b==cnt[n][j] && c==cnt[n][k]){
			ch[i] = 'R', ch[j] = 'P', ch[k] = 'S';
			rep(t,1<<n){
				ans[t] = ch[s[n][t]];
				// printf("%c", ch[s[n][t]]);
			}
			string res = get(0, 1<<n);
			cout << res << endl;
			return;
		}
	}
	printf("IMPOSSIBLE\n");
}

int main(int argc, char const *argv[])
{
	pre();
	int cas;
	cin >> cas;
	rep(ca,cas){
		printf("Case #%d: ", ca+1);
		run();
	}
	return 0;
}