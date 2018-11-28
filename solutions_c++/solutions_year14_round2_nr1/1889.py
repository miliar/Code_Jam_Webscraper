#include<map>
#include<set>
#include<list>
#include<cmath>
#include<queue>
#include<stack>
#include<cstdio>
#include<string>
#include<vector>
#include<complex>
#include<cstdlib>
#include<cstring>
#include<numeric>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<functional>
 
#define mp          make_pair
#define pb          push_back
#define all(x)      (x).begin(),(x).end()
#define rall(x)     (x).rbegin(),(x).rend()
#define rep(i,n)    for(int i=0;i<(n);i++)
#define rep2(i,d,n) for(int i=(d);i<(n);i++)
#define sz(s)       (s).size()
#define clr(a)      memset((a),0,sizeof(a))
#define mclr(a)     memset((a),-1,sizeof(a))
 
using namespace std;
 
typedef    long long          ll;
typedef    unsigned long long ull;
typedef    vector<bool>       vb;
typedef    vector<int>        vi;
typedef    vector<vb>         vvb;
typedef    vector<vi>         vvi;
typedef    pair<int,int>      pii;
typedef    vector<pair<int,int> > vpii;
 
const int INF=1<<30;
const double EPS=1e-9;
 
const int dx[]={1,0,-1,0},dy[]={0,-1,0,1};

int counts(vector<int> check){
	int res = INF;
	rep(i,check.size()){
		int cnt = 0;
		rep(j,check.size()){
			if(i == j){
				continue;
			}
			cnt += abs(check[i]-check[j]);
		}
		res = min(res,cnt);
	}
	return res;
}

int main(){
	int t;
	cin >> t;
	rep(lp,t){
		int n;
		cin >> n;
		vector<vector<pair<char,int> > > data;

		rep(i,n){
			string str;
			cin >> str;
			int old=str[0];
			int cnt=1;
			vector<pair<char,int> > buf;
			rep2(j,1,str.size()){
				if(old == str[j]){
					cnt++;
				}else{
					buf.pb(mp(old, cnt));
					//cout << "char:" << old << " cnt:" << cnt << endl; 
					cnt = 1;
					old = str[j];
				}
			}
			if(cnt != 1 || old != str[str.size()-2]){
				buf.pb(mp(old, cnt));
				//cout << "char:" << old << " cnt:" << cnt << endl; 
			}
			data.pb(buf);
		}

		bool flag = true;
		int ans = 0;
		rep2(i,1,n){
			if(data[0].size() != data[i].size()){
				flag = false;
				break;
			}
			rep(j,data[0].size()){
				if(data[0][j].first != data[i][j].first){
					flag = false;
				}
			}
			if(flag){
				break;
			}
		}

		if(flag){
			rep(i,data[0].size()){
				vector<int> cnts;
				rep(j,n){
					cnts.pb(data[j][i].second);
				}
				ans += counts(cnts);
			}
			cout << "Case #" << (lp+1) << ": " << ans << endl;
		}else{
			cout << "Case #" << (lp+1) << ": Fegla Won" << endl;
		}
	}
}