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
	int t,n;
	cin >> t;
	rep(g,t){
		cin >> n;
		set<int> h;
		cout << "Case #" << g+1 << ": " ;
		For(i,1,200){
			int m = i*n;
			while(m > 0){
				h.insert(m%10);
				m/=10;
			}
			if(h.size() == 10){
				cout << i*n << endl;
				break;
			}
		}
		if(h.size() < 10)
			cout << "INSOMNIA" << endl;
	}
	return 0;
}
