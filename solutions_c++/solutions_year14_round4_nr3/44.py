/*
 * in the name of god
 *
 *
 *
 *
 *
 *
 *
 *
 */

#include <iostream> 
#include <fstream> 
#include <sstream> 
#include <cstdio> 
#include <cstring> 
#include <cstdlib> 
#include <cmath> 
#include <ctime> 
#include <algorithm> 
#include <vector> 
#include <queue> 
#include <deque> 
#include <stack> 
#include <set> 
#include <map> 
#include <complex> 
#include <bitset> 
#include <iomanip> 
#include <utility> 

using namespace std;

const int MAXN= 1000000+10;
const int MAXM= 1000000+10;
//const int MAXN = 1000, MAXM = 1000;
const int inf = 1e9;

int n;
bool mark[1000][1000];

int end [MAXN],par[MAXN],last[MAXN];
int prev[MAXM],fx[MAXM],fy[MAXM],wei[MAXM];

struct maxFlow{
	int n,e;
	maxFlow (int _n){
		n = _n;
		e = 0;
		memset(end,-1,sizeof end);
	}
	inline void addEdge (int x, int y, int c){
		prev[e] = end[x]; end[x] = e; fx[e] = x; fy[e] = y; wei[e] = c; e++;
		prev[e] = end[y]; end[y] = e; fx[e] = y; fy[e] = x; wei[e] = 0; e++;
	}
	inline int go(int source, int sink){
		int ret = 0;
		while (true){
			memset(last, 0, sizeof last);
			queue <int> Q;
			Q.push(source);
			last[source] = inf;
			par [source] = -1;
			while (!Q.empty() && last[sink]==0){
				int front = Q.front(); Q.pop();
				for (int cur = end[front]; cur!=-1; cur = prev[cur]) if (wei[cur] &&
						last[fy[cur]]==0){
					Q.push(fy[cur]);
					last[fy[cur]] = min(last[front], wei[cur]);
					par [fy[cur]] = cur;
				}
			}
			if (last[sink] == 0)
				break;
			int C = last[sink];
			int temp = sink;
			while (temp != source){
				int p = par[temp];
				wei[p]-=C; wei[p^1]+=C;
				temp = fx[p];
			}
			ret+= C;
		}
		return ret;
	}
};


const int dx[] = {-1,1,0,0};
const int dy[] = {0,0,-1,1};

int W,H;

int IN(int x, int y){
	return y * W + x;
}

int OUT(int x, int y){
	return IN(x,y) + W*H;
}

void main2(){
	memset(mark, 0, sizeof mark);
	cin >> W >> H;
	int n; cin >> n;
	for (int i=0; i<n; i++){
		int X,Y,XX,YY; cin >> X >> Y >> XX >> YY;
		if (X>XX) swap(X,XX);
		if (Y>YY) swap(Y,YY);
		for (int x = X; x<=XX; x++)
			for (int y = Y; y<=YY; y++)
				mark[x][y] = true;
	}
	maxFlow ans(W*H*2+2);
	for (int i=0; i<W; i++)
		for (int j=0; j<H; j++) if (!mark[i][j]){
			for (int k=0; k<4; k++){
				int ii = i + dx[k];
				int jj = j + dy[k];
				if (ii>=0 && ii<W && jj>=0 && jj<H && !mark[ii][jj])
					ans.addEdge(OUT(i,j), IN(ii,jj), 1);
			}
			ans.addEdge(IN(i,j), OUT(i,j), 1);
		}
	int source = 2*W*H, sink = 2*W*H+1;
	for (int i=0; i<W; i++) if (!mark[i][0])
		ans.addEdge(source, IN(i,0), 1);
	for (int i=0; i<W; i++) if (!mark[i][H-1])
		ans.addEdge(OUT(i,H-1), sink, 1);
	cout << ans.go(source, sink) << endl;
}

int main(){
	int testCase; cin >> testCase;
	for (int o=1; o<=testCase; o++){
		cout << "Case #" << o << ": ";
		main2();
	}
	return 0;
}
