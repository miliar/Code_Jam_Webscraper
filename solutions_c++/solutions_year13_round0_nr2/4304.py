using namespace std;
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<cassert>
#include<cstring>
#include<cmath>

typedef long double D; typedef long long LL; typedef pair<int,int> pii;
#define ALL(v) (v).begin(),(v).end()
#define REP(i, n) for (int i (0); i < (n); i ++)
#define FORIT(a,b, it) for(__typeof(b)it(a);it!=(b);++it)
#define FOREACH(v, it) FORIT((v).begin(),(v).end(),it)
#define len(v) ((int)(v).size())
#define append push_back
#define _ make_pair
#define fi first
#define se second
#define add insert
#define remove erase
#define TWO(x) (1<<(x))
#define UNIQUE(v) (v).erase(unique(ALL(v)),(v).end())
const int infInt (1010101010);
const LL  infLL  (4 * LL (infInt) * LL (infInt));

template<class T>void pv(T a,T b){FORIT(a,b,it)cout<<*it<<" ";cout<<endl;}

#define NVAR 100000

vector<vector<int> > adj;
vector<vector<int> > radj;
int nv;
void reset() { adj = vector<vector<int> > (NVAR); radj = vector<vector<int> > (NVAR); nv = 0; }
int addVar() { return nv ++; }
int YY(int i) { return 2*i; }
int NN(int i) { return 2*i+1; }
void addEdge(int x, int y) {
	 adj[x].push_back(y);
	radj[y].push_back(x);
}
void OR(int i, int j) {
	addEdge(i^1, j);
	addEdge(j^1, i);
}

#include<deque>
int compnr[NVAR];
vector<bool>done;
deque<int> parent_first;
int compID;
void dfs(int x){
	done[x]=1;FOREACH( adj[x],it)if(!done[*it]) dfs(*it);
	parent_first.push_front(x);
}
void rdfs(int x){
	done[x]=1;FOREACH(radj[x],it)if(!done[*it])rdfs(*it);
	compnr[x] = compID;
}
void scc(int n){
	done = vector<bool> (n);
	parent_first.clear();
	REP(x,n)if(!done[x])dfs(x);
	done = vector<bool> (n);
	compID = 0;
	FOREACH(parent_first,it)if(!done[*it])compID ++,rdfs(*it);
}

bool calc() {
	scc(2*nv);
	for (int i = 0; i < nv; i ++) if (compnr[YY(i)] == compnr[NN(i)]) return false;
	return true;
}

int row[100][105]; // i, h -> is row[i]==h
int col[100][105]; // j, h -> is col[j]==h

int main() {
	const int L = 100;
	int tc;
	cin >> tc;
	for (int casenr = 1; casenr <= tc; casenr ++) {
		int h, w;
		cin >> h >> w;
		reset();
		for (int i = 0; i < h; i ++) {
			for (int lvl = 1; lvl <= L; lvl ++) {
				row[i][lvl] = addVar();
			}
			for (int lvl1 = 1; lvl1 <= L; lvl1 ++) {
				for (int lvl2 = lvl1 + 1; lvl2 <= L; lvl2 ++) {
					OR(NN(row[i][lvl1]), NN(row[i][lvl2]));
				}
			}
		}
		for (int j = 0; j < w; j ++) {
			for (int lvl = 1; lvl <= L; lvl ++) {
				col[j][lvl] = addVar();
			}
			for (int lvl1 = 1; lvl1 <= L; lvl1 ++) {
				for (int lvl2 = lvl1 + 1; lvl2 <= L; lvl2 ++) {
					OR(NN(col[j][lvl1]), NN(col[j][lvl2]));
				}
			}
		}
		for (int i = 0; i < h; i ++) {
			for (int j = 0; j < w; j ++) {
				int lvl;
				cin >> lvl;
				OR(YY(row[i][lvl]), YY(col[j][lvl]));
				for (int lvl2 = 1; lvl2 < lvl; lvl2 ++) {
					OR(NN(row[i][lvl2]), NN(row[i][lvl2]));
					OR(NN(col[j][lvl2]), NN(col[j][lvl2]));
				}
			}
		}
		printf("Case #%d: %s\n", casenr, calc() ? "YES" : "NO");
	}
}
