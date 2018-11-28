#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <sstream>
#include <functional>
#include <map>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <list>
#include <numeric>
using namespace std;
const double PI = 3.14159265358979323846;
const double EPS = 1e-12;
const int INF = 1<<25;
typedef pair<int,int> P;
typedef long long ll;
typedef unsigned long long ull;

#define N 12

string S[N+1][3]; 

void init(){
	S[0][0] = "R";
	S[0][1] = "P";
	S[0][2] = "S";
	for(int i = 1; i <= N; i++){
		for(int j = 0; j < 3; j++){
			int j2 = (j+2)%3;
			string s = S[i-1][j2]+S[i-1][j], t = S[i-1][j]+S[i-1][j2];
			S[i][j] = s<t?s:t;
		}
	}
}

int main(){
	init();
	int T;
	cin>>T;
	for(int Case = 1; Case <= T; Case++){
		int n, a, b, c;
		cin>>n>>a>>b>>c;
		string res = "IMPOSSIBLE";
		for(int i = 0; i < 3; i++){
			int a2 = a, b2 = b, c2 = c;
			for(int j = 0; j < 1<<n; j++){
				if(S[n][i][j]=='R') a2--;
				if(S[n][i][j]=='P') b2--;
				if(S[n][i][j]=='S') c2--;
			}
			if((a2|b2|c2)==0){
				res = S[n][i];
			}
		}
		cout<<"Case #"<<Case<<": "<<res<<endl;
	}
	return 0;
}

