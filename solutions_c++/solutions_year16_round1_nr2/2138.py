#include<iostream>
#include<vector>
#include<algorithm>
#include<cstring>
#include<set>
#include<map>
#include<cmath>
#include<cstdlib>
#include<complex>
#include<sstream>
#include<iomanip>

using namespace std;

#define rep(i,n) for(int i=0;i<n;i++)
#define For(i,a,b) for(int i=a;i<b;i++)
#define pb(x) push_back(x)
#define ll long long
#define VI vector<int>

int main(){
	ios::sync_with_stdio(false);
	int n,t;
	cin >> t;
	rep(g,t){
		cin >> n;
		vector<VI > rc;
		rep(i,2*n-1){
			VI v;
			rep(j,n){
				int x;
				cin >> x;
				v.pb(x);
			}
			rc.pb(v);
		}
		rep(i,n){
			VI tmp;
			rep(j,rc.size())
				tmp.pb(rc[j][i]);
			sort(tmp.begin(), tmp.end());
			int m = 2 * i;
			if(m+1 >= tmp.size() || tmp[m] != tmp[m+1]){
				multiset<int> ans;
				rep(j,rc.size())
					ans.insert(rc[j][i]);
				rep(j,rc.size())
					if(rc[j][i] == tmp[m]){
						rep(k,n)
							ans.erase(ans.find(rc[j][k]));
						break;
					}
				ans.insert(tmp[m]);
				cout << "Case #" << g+1 << ": " ;
				for(set<int>::iterator it = ans.begin();it!=ans.end();++it)
					cout << *it << " ";
				cout << endl;
				break;
			}
		}
	}
	return 0;
}
