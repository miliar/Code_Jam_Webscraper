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
	int d;

	cin >> d;

	int p[1001];

	int maxi = 0;

	REP(i,d){
		cin >> p[i];
		maxi = max(maxi, p[i]);
	}

	int res = 1001;

	FOR(i,1,maxi){
		int tmp = 0;
		REP(j,d) tmp += ((p[j] + i - 1) / i - 1);
		res = min(res, i + tmp);
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
