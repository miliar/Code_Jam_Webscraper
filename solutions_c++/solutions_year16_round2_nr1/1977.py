#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>

#define rep(i,n) for(int i=0; i<(n); i++)
#define rrep(i,n) for(int i=(n)-1; i>=0; i--)
#define all(X) (X).begin(),(X).end()

using namespace std;
typedef long long int ll;
typedef pair<int,int> P;

template<class T> bool chmax(T &a, const T &b) { if (a<b) { a=b; return 1; } return 0; }
template<class T> bool chmin(T &a, const T &b) { if (a>b) { a=b; return 1; } return 0; }

template<class A, size_t N, class T> void Fill(A (&a)[N], const T &v){ fill( (T*)a, (T*)(a+N), v ); }

const int INF = 0x3fffffff;


int main(){
	int T;
	string deg[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

	cin >> T;
	for(int caseNum=1; caseNum <= T; caseNum++){
		string s, ans;
		int cnt[255]={};
		vector<int> d;

		cin >> s;
		for(auto c: s){
			cnt[c]++;
		}
		while(cnt['Z']){ for(auto c: deg[0]) cnt[c]--; d.push_back(0); }
		while(cnt['W']){ for(auto c: deg[2]) cnt[c]--; d.push_back(2); }
		while(cnt['U']){ for(auto c: deg[4]) cnt[c]--; d.push_back(4); }
		while(cnt['X']){ for(auto c: deg[6]) cnt[c]--; d.push_back(6); }
		while(cnt['G']){ for(auto c: deg[8]) cnt[c]--; d.push_back(8); }

		while(cnt['F']){ for(auto c: deg[5]) cnt[c]--; d.push_back(5); }
		while(cnt['R']){ for(auto c: deg[3]) cnt[c]--; d.push_back(3); }
		while(cnt['O']){ for(auto c: deg[1]) cnt[c]--; d.push_back(1); }
		while(cnt['S']){ for(auto c: deg[7]) cnt[c]--; d.push_back(7); }

		while(cnt['I']){ for(auto c: deg[9]) cnt[c]--; d.push_back(9); }

		sort( all(d) );
		printf("Case #%d: ", caseNum);
		for(auto t: d){ cout << t; }
		printf("\n");

	}

	return 0;
}
