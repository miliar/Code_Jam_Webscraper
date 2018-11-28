#include <iostream>

using namespace std;

int main() {
 	int T;
 	cin >> T;
 	for (int I = 1; I<=T; I++) {
 		int r, c, w, ans=0, t=0;
 		cin >> r >> c >> w;
 		for (int x = w-1; x < c; x += w) {
			for (int y = 0; y < r; y++) {
 				t++;
 				int a = w - 1;
 				if (x < c-1) a++;
 				ans = max(ans, t + a);
 			}
  		}
 		cout << "Case #"<<I<<": ";
 		cout << ans << '\n';
 	}
}