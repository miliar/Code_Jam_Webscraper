#include <iostream>
#include <iomanip>
using namespace std;

int n;
double x, v;
double r[100], c[100];

void solve(){
	cin >> n >> v >> x;
	for(int i=0; i<n; i++) cin >> r[i] >> c[i];
	if(n == 1){
		if(c[0] == x) cout << fixed << v/r[0];
		else cout << "IMPOSSIBLE";
	}
	else if(n == 2){
		if(c[0] == c[1]){
			if(c[0] == x) cout << fixed << v/(r[0]+r[1]);
			else cout << "IMPOSSIBLE";
		}
		//~ else if(c[0] == x) cout << v/r[0];
		//~ else if(c[1] == x) cout << v/r[1];
		else{
			double t1 = v/r[0]*(x-c[1])/(c[0]-c[1]);
			double t2 = v/r[1]*(x-c[0])/(c[1]-c[0]);
			if(t1 < 0 || t2 < 0) cout << "IMPOSSIBLE";
			else cout << fixed << max(t1, t2);
		}
		
	}
	else cout << "ERROR";
}

int main(){
	int t; cin >> t;
	cout << setprecision(10);
	for(int i=1; i<=t; i++){
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}
	
	return 0;
}
