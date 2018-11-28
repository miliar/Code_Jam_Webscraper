#include <iostream>
#include <iomanip>
#include <math.h>

using namespace std;

int main(){
	
	int T;
	cin >> T;
	for (int y = 1; y <= T; y++){
		double c,f,x;
		cin >> c >> f >> x;
		double round = x/c - 2/f - 1;
		double ans = 0;
		round = ceil(round);
		if (round > 0){
		for (int i = 0; i < round; i++){
			ans += c/(2+ i*f);
			}
			ans+=x/(2 + round*f);
		}
		else{
				ans+=x/2;
			}

			cout << "Case #" << y << ": ";
			cout << fixed << setw(13) << setprecision(7) << ans << endl;
	}
}
