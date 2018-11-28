#include <bits/stdc++.h>
using namespace std;
const int dx[]={1,0,-1,0,1,-1,-1,1};
const int dy[]={0,1,0,-1,1,1,-1,-1};
const int INF = 1<<30;
const long long LINF = 1e18;
const int EPS = 1e-8;
#define PB push_back
#define mk make_pair
#define fr first
#define sc second
#define ll long long
#define reps(i,j,k) for(int i = (j); i < (k); i++)
#define rep(i,j) reps(i,0,j)
#define MOD 1000000007
typedef pair<int,int> Pii;
typedef pair<int, ll> Pil;
typedef vector<int> vi;
typedef vector<vi> vvi;
struct data{
	string str;
	int cnt;
	data(){}
	data(string str,int cnt){
		this->str = str;
		this->cnt = cnt;
	}
};
bool check(string str){
	rep(i,str.size()){
		if(str[i] == '-'){
			return false;
		}
	}
	return true;
}
int solve(string str){
	int len = str.size();

	map<string,int> memo;
	queue < data > Q;
	Q.push(data(str,1));
	while(!Q.empty()){
		data d = Q.front();Q.pop();
		if(memo[d.str]){
			continue;
		}
		memo[d.str] = d.cnt;
		if(check(d.str)){
			return d.cnt-1;
		}
		string tmp = "";
		rep(i,len){
			tmp += d.str[i];
			string head = tmp;
			string fin = "";
			reps(j,i+1,len){
				fin += d.str[j];
			}
			reverse(head.begin(),head.end());
			//cout << head << " @ ";
			rep(j,i+1){
				if(head[j] == '+'){
					head[j] = '-';
				}
				else if(head[j] == '-'){
					head[j] = '+';
				}
			}
			//cout << head << "\n";
			//cout << "(" << head+fin << "," << d.cnt+1 << ")" << "\n";
			Q.push(data(head+fin,d.cnt+1));
		}
	}
	return -1;
}
int main(){
	int Q;
	cin >> Q;
	rep(q,Q){
		string str;
		cin >> str;
		int res = solve(str);
		printf("Case #%d: %d\n",q+1,res);
	}
	return 0;
}