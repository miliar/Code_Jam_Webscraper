#include<iostream>
#include<cstdio>
#include<string>
#include<cmath>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<utility>
using namespace std;

#define FOR(I,A,B) for(int I=(A);I<=(B);I++)
#define REP(I,N) for(int I=0;I<(N);I++)
#define ALL(X) (X).begin(),(X).end()
#define PB push_back
#define MP make_pair
#define f first
#define s second

typedef vector<int> VI;
typedef pair<int,int> PII;
typedef long long ll;
typedef vector<string> VS;

void testcase(){
	int n;
	string s;

	cin >> n >> s;

	int res = 0;
	int acc = 0;

	REP(i,s.length()){
		int howMany = s[i] - '0';
		res += max(i - acc - res, 0) * min(howMany, 1);
		acc += howMany;
	}

	cout << res << endl;
}

int main(){
	ios_base::sync_with_stdio(0);

	int t;
	cin >> t;

	REP(i,t){
		cout << "Case #" << (i+1) << ": ";
		testcase();
	}
	
	return 0;
}
