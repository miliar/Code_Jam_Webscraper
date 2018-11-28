#include <iostream>
#include <cstdio>

using namespace std;

int T;
int Smax;
char S[1010];

int main(){
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);
	cin >> T;
	for (int c = 1; c <= T; ++c){
		int ans = 0, temp = 0;
		cin >> Smax;
		cin >> S;
		for (int i=0; i <= Smax; ++i){
			int ppl = S[i] - '0';
			if (ppl){
				if (i > temp){
					ans += i - temp;
					temp += i - temp;
				}
			}
			temp += ppl;
		}
		cout << "Case #" << c << ": " << ans << endl;
	}
	return 0;
}