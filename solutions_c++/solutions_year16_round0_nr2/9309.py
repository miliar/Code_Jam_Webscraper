#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

const double eps = 1e-8;
const int dx[] = { 1, 0, -1, 0, -1, -1, 1, 1 };
const int dy[] = { 0, 1, 0, -1, -1, 1, -1, 1 };
const int OO = INT_MAX;

#define SZ(x)          (int)x.size()
#define ALL(x)         (x).begin(),(x).end()
#define ALLR(x)        (x).rbegin(),(x).rend()
#define rep(i,st,en)    for(int i=st ; i< en; i++)
#define repR(i,st,en)   for(int i=st;i>=en ; i--)
#define fill(v, d)       memset(v, d, sizeof(v))
/**************************************************************/
string flipMenu(string s){
	reverse(ALL(s));
	rep(i, 0, SZ(s)){
		if(s[i] == '+'){
			s[i] = '-';
		}else{
			s[i] = '+';
		}
	}
	return s;
}

int solve(string s){
	string target = "";
	int n = SZ(s);
	rep(i, 0, n){
		target += '+';
	}
	set<string>isVisited;
	queue< pair<string , int> > q;
	q.push({s, 0});
	int res = 0;
	while(!q.empty()){
		pair<string, int>p = q.front();
		q.pop();
		if(isVisited.find(p.first) != isVisited.end()){
			continue;
		}
		if(target == p.first){
			res = p.second;
			break;
		}
		isVisited.insert(p.first);//mark visited
		string temp = "";
		rep(i, 0, n){
			temp += p.first[i];
			q.push( {flipMenu(temp) + p.first.substr(i+1), p.second + 1} );
		}
	}
	return res;
}

int main() {

	freopen("B-small-attempt0.in" , "r",stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	int T;
	cin >> T;
	rep(t, 1, T+1){
		string s;
		cin >> s;
		int res = solve(s);
		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}
