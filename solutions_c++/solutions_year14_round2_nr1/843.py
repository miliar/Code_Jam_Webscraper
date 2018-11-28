#include <bits/stdc++.h>

using namespace std;

#define MAX 110
#define INF INT_MAX
#define EPS 1e-7
#define PI acos(-1.0)

#define PRINT(x) cout<<#x<<" = "<<x<<endl

#define READ() freopen("input.txt", "r", stdin)
#define WRITE() freopen("output.txt", "w", stdout)

#define CLR(x) memset( x, 0, sizeof(x) )
#define SET(x) memset( x, -1, sizeof(x) )

#define CHKBIT(x, i) ( ( ( x & ( 1 << i ) ) == 0 ) ? 0 : 1 )
#define SETBIT(x, i) ( x | ( 1 << i ) )
#define CLRBIT(x, i) ( x & (!( 1 << i )) )

#define pb push_back

#define ff first
#define ss second
#define mp make_pair
typedef pair<int, int> pii;

int main(){
	freopen("a_input.txt", "r", stdin);
	freopen("a_output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int t=1; t<=T; t++){
		int n;
		char s[MAX][MAX];
		string ss[MAX];
		set <string> sx;
		vector <int> v[MAX];
		scanf("%d", &n);
		for(int i=0; i<n; i++){
			scanf("%s", s[i]);
			//PRINT(s[i]);
			
			ss[i] = "";
			v[i].clear();
			
			ss[i].push_back(s[i][0]);
			v[i].push_back(1);
			
			for(int j=1; s[i][j]; j++){
				if( s[i][j] != s[i][j-1] ){
					ss[i].push_back(s[i][j]);
					v[i].push_back(1);
				}
				else{
					v[i][v[i].size()-1]++;
				}
			}
			
			sx.insert(ss[i]);
			//PRINT(ss[i]);
		}
		
		printf("Case #%d: ", t);
		
		if( sx.size() > 1 ){
			printf("Fegla Won\n");
		}
		else{
			int x = (*sx.begin()).size();
			int res = 0;
			for(int i=0; i<x; i++){
				int tres = INF;
				for(int j=1; j<MAX; j++){
					int temp = 0;
					for(int k=0; k<n; k++){
						temp += abs(v[k][i] - j);
					}
					tres = min(tres, temp);
				}
				res += tres;
			}
			printf("%d\n", res);
		}
	}
	return 0;
}
