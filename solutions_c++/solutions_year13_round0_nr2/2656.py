#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <queue>
using namespace std;

const int MAXN = 102;

struct node{
	int x, y, h;
};
struct cmp{
	bool operator()(const struct node &a, const struct node &b){
		return a.h > b.h;
	}
};
priority_queue<struct node, vector<struct node>, cmp> que;

int mp[MAXN][MAXN], N, M, cor_num, tol_num;
bool vst[MAXN][MAXN];

inline int getint(){
	int res;
	char ch;
	while(ch=getchar(), ch<'0' || ch>'9');
	res = ch-'0';
	while(ch=getchar(), ch>='0' && ch<='9') res = (res<<3)+(res<<1)+ch-'0';
	return res;
}

void init(){
	memset(mp, 0, sizeof(mp));
	memset(vst, 0, sizeof(vst));
	while(!que.empty())que.pop();
	cor_num = 0;
	tol_num = N*M;
}

bool judge_row(int x, int y, int h){
	int i, j, nx, ny;
	int hd = -x, ed = N-x;
	for(i=hd; i<ed; ++i){
		nx = x + i;
		ny = y;
		if(nx>=0 && nx<N && (!vst[nx][ny])){
			if(mp[nx][ny] > h) return false;
		}
	}
	for(i=hd; i<ed; ++i){
		nx = x + i;
		ny = y;
		if(nx>=0 && nx<N && (!vst[nx][ny])){
			vst[nx][ny] = true;
			cor_num ++;
		}
	}
	return true;
}

bool judge_col(int x, int y, int h){
	int i, j, nx, ny;
	int hd = -y, ed = M-y;
	for(i=hd; i<ed; ++i){
		nx = x;
		ny = y + i;
		if(ny>=0 && ny<M && (!vst[nx][ny])){
			if(mp[nx][ny] > h) return false;
		}
	}
	for(i=hd; i<ed; ++i){
		nx = x;
		ny = y + i;
		if(ny>=0 && ny<M && (!vst[nx][ny])){
			vst[nx][ny] = true;
			cor_num ++;
		}
	}
	return true;
}

bool solve(){
	bool isok1, isok2;
	node cur;
	int x, y, h;
	while(!que.empty()){
		cur = que.top();
		que.pop();
		x = cur.x;
		y = cur.y;
		h = cur.h;
		if(vst[x][y]) continue;

		isok1 = judge_row(x, y, h);
		isok2 = judge_col(x, y, h);
		if((!isok1) && (!isok2)) return false;

		if(cor_num >= tol_num) return true;
	}
	return true;
}

int main(){
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	int T, cases;
	node nd;
	scanf("%d", &T);
	for(cases=1; cases<=T; ++cases){
		scanf("%d%d", &N, &M);
		init();
		for(int i=0; i<N; ++i){
			for(int j=0; j<M; ++j){
				mp[i][j] = getint();
				nd.x = i;
				nd.y = j;
				nd.h = mp[i][j];
				que.push(nd);
			}
		}

		if(solve()){
			printf("Case #%d: YES\n", cases);
		}else{
			printf("Case #%d: NO\n",cases);
		}
	}
	return 0;
}
