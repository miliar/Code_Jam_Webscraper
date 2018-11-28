#include<iostream>
#include<cstdio>
#include<vector>
#include<cstdlib>
#include<cmath>
#include<iomanip>
#include<algorithm>
#include<set>
#include<iomanip>
#include<queue>
#include<map>
#include<deque>

using namespace std;

#define VI vector<int>
#define PI pair<int,int>
#define F first
#define S second
#define MP make_pair
#define LL long long
#define PB push_back
#define VB vector<bool>
#define VS vector<string>
#define VVS vector<VS>
#define MAXN 1024

int N;
int ans;
int f[MAXN];
map<PI,int> z;

void divein(int start){
	map<int,int> vis;
	int cur = start;
	vis[cur] = 1;
	int idx = 2;
	while(true){
		int nxt = f[cur];
		if(vis.find(nxt) == vis.end()){
			vis[nxt] = idx;
			idx++;
			cur = nxt;
		}
		else{
			int posn = vis[nxt];
			if(posn == idx - 2){
				int sz = vis.size();
				int l = sz - 2;
				PI p = MP(nxt,cur);
				if(z.find(p) == z.end()){
					//printf("adding (%d,%d) = %d to z\n", p.F, p.S, l);
					z[p] = l;
				}
				else{
					z[p] = max(z[p],l);
					//printf("updating (%d,%d) = %d to z\n", p.F, p.S, z[p]);
				}
			}
			else{
				int c = idx - posn;
				ans = max(ans,c);
			}
			break;
		}
	}
}

void compute(){
	ans = 0;
	z.clear();
//	printf("size of z is %d\n", (int)z.size());
	for(int i=1;i<=N;i++){
		divein(i);
	}

	int a = 0;
	for(int i=1;i<=N;i++){
		for(int j=i+1;j<=N;j++){
			PI p1 = MP(i,j);
			PI p2 = MP(j,i);
			int l1 = -1;
			int l2 = -1;
			if(z.find(p1) != z.end()){
				l1 = z[p1];
			}

			if(z.find(p2) != z.end()){
				l2 = z[p2];
			}
/*
			if(l1 != -1 or l2 != -1){
				printf("at pair %d %d\n", p1.F, p1.S);
			}
*/
			if(l1 == -1 and l2 != -1){
				a += 2 + l2;
			}
			else if(l1 != -1 and l2 == -1){
				a += 2 + l1;
			}
			else if(l1 != -1 and l2 != -1){
				a += 2 + l1 + l2;
			}
			else{
				continue;
			}
			//printf("a is now %d\n", a);
		}
	}
	ans = max(ans,a);
}

int main()
{
	freopen("/Users/Sharat/GoogleDrive/Coding/C++/Contests/GCJ2016/C_input2.txt", "r", stdin);
	freopen("/Users/Sharat/GoogleDrive/Coding/C++/Contests/GCJ2016/C_output2.txt", "w", stdout);
	int cases;
	scanf("%d", &cases);

	for(int casenum=1;casenum<=cases;casenum++){
		scanf("%d", &N);
		for(int i=1;i<=N;i++)
			scanf("%d", &f[i]);
		compute();
		printf("Case #%d: %d\n", casenum, ans);
	}

	return 0;
}
