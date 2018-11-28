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
#include<climits>
#include<numeric>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<functional>
 
#define mp       make_pair
#define pb       push_back
#define all(x)   (x).begin(),(x).end()
#define rep(i,n) for(int i=0;i<(n);i++)
 
using namespace std;
 
typedef    long long          ll;
typedef    unsigned long long ull;
typedef    vector<bool>       vb;
typedef    vector<int>        vi;
typedef    vector<vb>         vvb;
typedef    vector<vi>         vvi;
typedef    pair<int,int>      pii;
 
const double EPS=1e-9;
 
const int dx[]={1,0,-1,0},dy[]={0,-1,0,1};

int main(){
	int n;
	cin >> n;

	rep(loop,n){
		cout << "Case #" << (loop+1) << ": ";

		int ans1,ans2;
		vector<vector<int> > d1,d2;
		cin >> ans1;
		rep(i,4){
			d1.pb(vector<int>());
			rep(j,4){
				int buf;
				cin >> buf;
				d1[i].pb(buf);
			}
		}
		cin >> ans2;
		rep(i,4){
			d2.pb(vector<int>());
			rep(j,4){
				int buf;
				cin >> buf;
				d2[i].pb(buf);
			}
		}

		vector<int> anslist;
		rep(i,4){
			rep(j,4){
				if(d1[ans1-1][i] == d2[ans2-1][j]){
					anslist.pb(d1[ans1-1][i]);
				}
			}
		}

		if(anslist.size() == 0){
			cout << "Volunteer cheated!" << endl;
		}else if(anslist.size() == 1){
			cout << anslist[0] << endl;
		}else{
			cout << "Bad magician!" << endl;
		}
	}
}