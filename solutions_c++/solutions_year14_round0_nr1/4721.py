/**************************************************
 * Author	 : xiaohao Z
 * Blog	 : http://www.cnblogs.com/shu-xiaohao/
 * Last modified : 2014-04-12 19:48
 * Filename	 : 2014_pre_A.cpp
 * Description	 : 
 * ************************************************/

#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <queue>
#include <stack>
#include <vector>
#include <set>
#include <map>
#define MP(a, b) make_pair(a, b)
#define PB(a) push_back(a)

using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<unsigned int,unsigned int> puu;
typedef pair<int, double> pid;
typedef pair<ll, int> pli;
typedef pair<int, ll> pil;

const int INF = 0x3f3f3f3f;
const double eps = 1E-6;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T, kase = 1, a[4][4], b[4][4];
	cin >> T;
	while(T--){
		int r1, r2, ans = -1;
		cin >> r1;r1--;
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				cin >> a[i][j];
		int f[100];
		memset(f, 0, sizeof f);
		for(int i=0; i<4; i++)f[a[r1][i]] = 1;
		cin >> r2;r2--;
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				cin >> b[i][j];
		for(int i=0; i<4; i++){
			if(ans < 0 && f[b[r2][i]])
				ans = b[r2][i];
			else if(ans > 0 && f[b[r2][i]]){
				ans = -2;
			   break;	
			}	
		}
		printf("Case #%d: ", kase++);
		if(ans == -2) cout << "Bad magician!" << endl;
		else if(ans == -1) cout << "volunteer cheated!" << endl;
		else cout << ans << endl;
	}
	return 0;
}

