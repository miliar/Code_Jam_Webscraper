// iostream is too mainstream
#include <cstdio>
// bitch please
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <list>
#include <cmath>
#include <iomanip>
#define dibs reserve
#define OVER9000 1234567890LL
#define ALL_THE(CAKE,LIE) for(auto LIE =CAKE.begin(); LIE != CAKE.end(); LIE++)
#define tisic 47
#define soclose 1e-10
#define chocolate win
// so much chocolate
#define patkan 9
#define ff first
#define ss second
#define abs(x) ((x < 0)?-(x):x)
#define uint unsigned int
using namespace std;
// mylittledoge

struct node {
	vector<int> son;

	node() {son.resize(26,-1);}
	};

struct trie {
	vector<node> T;

	trie() {
		T.resize(1);}

	void put(string s) {
		int N =s.length(), akt =0;
		for(int i =0; i < N; i++) {
			if(T[akt].son[s[i]-'A'] == -1) {
				int sz =T.size();
				T[akt].son[s[i]-'A'] =sz;
				T.resize(sz+1);}
			akt =T[akt].son[s[i]-'A'];}
		}
	};

int main() {
	cin.sync_with_stdio(0);
	cin.tie(0);
	srand(time(0));
	int T;
	cin >> T;
	for(int t =0; t < T; t++) {
		cout << "Case #" << t+1 << ":";
		int M,N;
		cin >> M >> N;
		vector<string> S(M);
		for(int i =0; i < M; i++) cin >> S[i];
//		long long mod =1000000007;
		int P =1;
		for(int i =0; i < M; i++) P *=N;
		int ansS =0, ansP =0;
		for(int p =0; p < P; p++) {
			vector<trie> V(N);
			int k =p;
			for(int i =0; i < M; i++) {
				V[k%N].put(S[i]);
				k /=N;}
			int S =0;
			for(int i =0; i < N; i++) if(V[i].T.size() > 1)
				S +=V[i].T.size();
			if(S > ansS) {ansS =S; ansP =0;}
			if(S == ansS) ansP++;}
		cout << " " << ansS << " " << ansP << "\n";}
	return 0;}

// look at my code
// my code is amazing
