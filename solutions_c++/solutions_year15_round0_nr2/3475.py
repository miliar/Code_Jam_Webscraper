#include<bits/stdc++.h>
#define rep(i,k,n) for(int i = k; i < (int) n; i++)
#define mp make_pair
#define pb push_back
#define ft first
#define sd second
typedef long long ll;
const long long inf = 9223372036854775807;
const int iinf = 2147483647;
const int limit = 1048576;
using namespace std;

int main(){
	freopen("Inf_Pancake.txt","w",stdout);
	freopen("B-large.in","r",stdin);
	int t; cin >> t;
	
	rep(j, 1, t + 1){
		int din; cin >> din;
		
		vector<int> pancakes; int t1;
		rep(i, 0, din){
			cin >> t1; pancakes.pb(t1);
		}
		
		int res = iinf;
		rep(i, 1, 1001){
			int tym_res = i;
			rep(j, 0, din){
				if(pancakes[j] <= i) continue;
				tym_res += (pancakes[j] - i)/i;
				if(pancakes[j] % i) tym_res++;
			}
			res = min(res, tym_res);
		}
		
		cout << "Case #" << j << ": " << res <<"\n";
	}

	return 0;
}
