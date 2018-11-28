#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>

using namespace std;

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int t, a, b, c[4], match, ans;
	cin >> t;
	for(int cases = 1; cases <= t; cases++){
		match = 0;
		cin >> a;
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				if(i == a-1){
					cin >> c[j];
				}
				else{
					cin >> b;
				}
			}
		}
		cin >> a;
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				if(i == a-1){
					cin >> b;
					for(int k = 0; k < 4; k++){
						if(c[k] == b){
							match++;
							ans = b;
						}
					}
				}
				else{
					cin >> b;
				}
			}
		}

		if(match == 1){
			cout << "Case #" << cases << ": " << ans << endl;
		}
		else if(match == 0){
			cout << "Case #" << cases << ": Volunteer cheated!" << endl;
		}
		else{
			cout << "Case #" << cases << ": Bad magician!" << endl;
		}
	}

    return 0;
}
