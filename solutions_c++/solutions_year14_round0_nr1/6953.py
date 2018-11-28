#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
#include <unordered_map>
using namespace std;

typedef long long Int;
typedef pair<int,int> PII;
typedef vector<int> VInt;

#define FOR(i, a, b) for(i = (a); i < (b); ++i)
#define RFOR(i, a, b) for(i = (a) - 1; i >= (b); --i)
#define CLEAR(a, b) memset(a, b, sizeof(a))
#define SIZE(a) int((a).size())
#define ALL(a) (a).begin(),(a).end()
#define PB push_back
#define MP make_pair

Int A[1 << 12];
Int B[1 << 12];
Int T[1 << 12];

int SolveTest(int test){
	string res;
	int sol1, sol2;
	unordered_multimap<int,vector<int> > rows;


	for(int i = 0; i < 2; ++i){
		
		int sol;
		if(i == 0){
			scanf("%d", &sol1);
			
			sol = sol1;
		}
		else{
			scanf("%d", &sol2);
			sol = sol2;
		}

		
		int ncol, nrow;
		for(nrow = 1; nrow <= 4; ++nrow){
			vector<int> r;
			for(ncol = 1; ncol <=4; ++ncol){

				int card;
				scanf("%d", &card);
				if(nrow == sol){

					r.push_back(card);
				}
			}
			
			if(nrow == sol){
				
				rows.insert(make_pair(ncol, r));
			}
		}
	}

		int nsame = 0;
		int common;
		auto it = rows.begin();
		vector<int> v = it->second;
		++it;
		vector<int> v2 = it->second;
		for(int card : v)
			if(find(v2.begin(), v2.end(), card) != v2.end()){
				common = card;
				++nsame;
			}
		if(nsame == 0){
			res = "Volunteer cheated!";
		}
		else if(nsame == 1){
			res = to_string(common);
		}
		else{
			res = "Bad magician!";
		}

		



	

	printf("Case #%d: %s\n", test + 1, res.c_str());
	return 0;
}


int main()
{
	freopen("asmall.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int T, t;
	char buf[1 << 7];
	gets(buf);
	sscanf(buf, "%d", &T);

	FOR(t, 0, T)
	{
		fprintf(stderr, "Solving %d/%d\n", t + 1, T);
		SolveTest(t);
	}

	return 0;
};