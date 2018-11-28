#include <bits/stdc++.h>
#include <limits>
using namespace std;

 
#define ff first
#define ss second
#define pb push_back
#define mp make_pair
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef long long ll;
typedef vector<int> vi;
typedef long double ld;
#define var(a,b) __typeof(b) a = b
#define rep(i,n) for(int i = 0;(i) < (n); ++i)
#define rept(i,a,b) for(var(i,a); i < (b); ++i)
#define tr(v,it) for(var(it,v.begin());it!=v.end();++it)
#define fill(a,val) memset(a,val,sizeof(a))
#define all(v) v.begin(),v.end()

int main(){

	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);


	int t;
	cin >> t;
	rep(k,t){
		int x,r,c;
		int flag;
		cin >> x >> r >> c;
		if(x == 1){
			flag = 1;
		}else if(x == 2){
			if(r == 1 && c == 1 || r == 3 && c == 3 || r == 3 && c == 1 || r == 1 && c == 3){
				flag = 0;
			}else flag = 1;
		}else if(x == 3){
			if(r == 1 || c == 1){
				flag = 0;
			}else if(r == 3 || c == 3){
				flag = 1;
			}else flag = 0;
		}else{
			if(r == 4 && c== 4 || r == 4 && c ==3 || r == 3 && c == 4){
				flag = 1;
			}else flag = 0;
		}

		if(flag){
			cout << "Case #" << k + 1 << ": " << "GABRIEL" << endl;
		}else{
			cout << "Case #" << k + 1 << ": " << "RICHARD" << endl;
		}
	}


	return 0;
}