//wawando's template

#include <iostream>
#include <string>
#include <fstream>
#include <functional>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <list>
#include <set>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>  //clock_t , clock() , CLOCKS_PER_SEC
#include <cstring>
#include <cctype>
#include <climits> // LLONG_MAX , LLONG_MIN , INT_MAX , INT_MIN

//MACROS
#define pb              push_back
#define mp              make_pair
#define INF             1000000000     //1 billion safer for floyd warshall, avoid overflow
		
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef pair<int, ii> iii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<iii> viii;

int TC, caseNo = 1;

int main() {
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	//ios::sync_with_stdio(false);
	scanf("%d",&TC);
	bool can_3[5][5],can_4[5][5];
	memset(can_3, 0, sizeof(can_3));
	memset(can_4, 0, sizeof(can_4));

	can_3[3][2] = true;
	can_3[2][3] = true;
	can_3[3][3] = true;
	can_3[3][4] = true;
	can_3[4][3] = true;

	can_4[3][4] = true;
	can_4[4][3] = true;
	can_4[4][4] = true;	

	while(TC--){
		int X,R,C;
		scanf("%d %d %d", &X, &R, &C);
		printf("Case #%d: ",caseNo++);
		if(X == 1){
			puts("GABRIEL");
		}
		else if(X == 2){
			puts(R*C % 2 == 0 ? "GABRIEL" : "RICHARD");
		}
		else if(X == 3){
			
			puts(can_3[R][C] ? "GABRIEL" : "RICHARD");
		}
		else{
			puts(can_4[R][C] ? "GABRIEL" : "RICHARD");
		}

	}
	return 0;
}
