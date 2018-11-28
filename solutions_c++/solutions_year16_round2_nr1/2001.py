#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
#include <utility>
#include <functional>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <deque>
#include <ctime>
 
using namespace std;
 
#define rep(i,n) REP(i,0,n)
#define REP(i,s,e) for(int i=(s); i<(int)(e); i++)
#define pb push_back
#define mp make_pair
#define all(r) r.begin(),r.end()
#define fi first
#define se second
#define println(X) cout<<X<<endl;
#define DBG(X) cout<<#X<<" : "<<X<<endl;
 
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vii;
typedef vector<ll> vl;
typedef vector<vl> vll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

const int INF = 1e9;
const ll MOD = 1e9 + 7;
double EPS = 1e-3;
const double PI = acos(-1);

int dx[]={-1,0,1,0};
int dy[]={0,-1,0,1};

string a = "ZWUXGOHFSE";
string b[] = {"ZERO", "TWO", "FOUR", "SIX", "EIGHT", "ONE", "THREE", "FIVE", "SEVEN", "NINE"};
int p[]={0,2,4,6,8,1,3,5,7,9};

int main(){
	int mCase;
	scanf("%d", &mCase);
	string s;
	for(int Case = 1; Case <= mCase; Case++){
		cin>>s;
		vi v(256, 0);
		vi ans(10, 0);
		for(char c : s) v[c]++;
		rep(i, a.size()){
			if(v[a[i]]==0) continue;
			ans[p[i]]+=v[a[i]];
			int tmp = v[a[i]];
			for(int j = 0; j < b[i].size(); j++){
				v[b[i][j]]-=tmp;
			}
		}
		printf("Case #%d: ", Case);
		for(int i = 0; i < 10; i++){
			for(int j = 0; j < ans[i]; j++){
				printf("%d", i);
			}
		}
		printf("\n");
	}
	// map<char, int> mp;
	// string s[10]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
	// s[0]=s[2]=s[4]=s[6]=s[8]="";
	// s[1]=s[3]=s[5]=s[7]="";
	// rep(i, 10){
	// 	rep(j, s[i].size()){
	// 		mp[s[i][j]]++;
	// 	}
	// }
	// for(auto p : mp){
	// 	cout<<p.fi<<" "<<p.se<<endl;
	// }
}