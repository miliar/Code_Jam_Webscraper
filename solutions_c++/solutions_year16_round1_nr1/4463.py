#include <bits/stdc++.h>
using namespace std;
#define forn(i, n) for(int i = 0; i < (int) (n); i++)

string w, t;
int tc;

int main(){
	freopen("large", "r", stdin);
	freopen("large.out", "w", stdout);
	scanf("%d", &tc);
	for(int TC = 1; TC <= tc; TC++){
		cin >> w; t = w[0];
		for(int i = 1; i < (int) w.size(); i++){
			if(t[0] <= w[i]){
				t = w[i] + t;
			}
			else t += w[i];
		}
		printf("Case #%d: ", TC); cout << t << endl;
	}
		
	return 0;
}
