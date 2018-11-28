#include <iostream>
#include <iomanip>
#include <cstring>

#define EPS 1e-7

using namespace std;
typedef long long ll;

int main(){
	ios_base::sync_with_stdio(false);
	
	ll T;
	
	double c, f, x, e, ans;
	
	cin >> T;
	for(int caso = 1; caso <= T; caso++){
		cout << "Case #" << caso << ": ";
		
		cin >> c >> f >> x;
		
		ans = 0;
		e = 2;
		
		for(;;){
			if(ans + (x/e) > ans + (c/e) + (x/(e+f))){
				ans = ans+(c/e);
				e = e+f;
			}
			else{
				ans = ans + (x/e);
				break;
			}
		}
		cout << fixed << setprecision(7) << ans << '\n';
	}
}
