#include<iostream>
#include<algorithm>
#define INF 1000000000
using namespace std;

//format maxleft[last killed][moves left]
//Looks at position when we start dealing with the monster
int T, h[100], g[100], maxgold[101][1001];

int main() {
	cin.sync_with_stdio(false);
	cin >> T;
	
	for(int TCASE=1;TCASE<=T;TCASE++) {
		int p, q, n;
		cin >> p >> q >> n;
		
		for(int i=0;i<n;i++)
			cin >> h[i] >> g[i];
		
		for(int i=0;i<=n;i++)
			for(int j=0;j<=1000;j++)
				maxgold[i][j] = -INF;
		
		maxgold[0][1] = 0;
		
		for(int i=0;i<n;i++) {
			int towmove = (h[i] - 1) / q, dianamove = (h[i] - 1) % q / p + 1;
			
			for(int j=0;j<1001;j++) {
				if(j + towmove + 1 < 1001)
					maxgold[i+1][j + towmove + 1] = maxgold[i][j];
					
				if(j + towmove - dianamove >= 0 && j + towmove - dianamove < 1001)
					maxgold[i+1][j + towmove - dianamove] = max(maxgold[i+1][j + towmove - dianamove],
										maxgold[i][j] + g[i]);
			}
		}
		
		int result = 0;
		for(int i=0;i<1001;i++)
			result = max(result, maxgold[n][i]);
			
		cout << "Case #" << TCASE << ": " << result << '\n';
	}
	
	return 0;
}
