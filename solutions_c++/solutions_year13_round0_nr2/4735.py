#include <iostream>
#include <fstream>
#include <set>

#define VI			deque<int>

#define REP(i,a,b)	for(i=(int)a ; i<=(int)b ; i++)
#define FOR(i,N)	REP(i,0,N-1)

#define II			pair<int,int>
#define St			pair<int,II>
#define xx			second.first
#define yy			second.second
#define val			first

using namespace std;

int B[100][100];
int R[100];
int C[100];

int main(){
	ifstream cin("input.txt");
	ofstream cout("b2.out");
	int T,t;
	cin >> T;
	REP(t,1,T){
		int i,j;
		int N,M;
		cin >> N >> M;
		FOR(i,N) FOR(j,M) cin >> B[i][j];

		set<St> s;
		FOR(i,N) FOR(j,M) s.insert(St(-B[i][j],II(i,j)));

		FOR(i,N) R[i] = 0;
		FOR(j,M) C[j] = 0;

		while(!s.empty()){
			int v = -(*s.begin()).val;
			int x = (*s.begin()).xx;
			int y = (*s.begin()).yy;
			if(R[x]>v && C[y]>v) break;
			R[x] = max(R[x],v);
			C[y] = max(C[y],v);
			s.erase(s.begin());
		}
		cout <<"Case #"<<t<<": ";
		if(s.empty()) cout <<"YES"<<endl;
		else cout <<"NO"<<endl;
	}
}
