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
#define FORD(I,A,B) for(int I=(A);I>=(B);I--)
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

const int MAX = 10001;

int t[MAX];
bool used[MAX];

void testcase(){
	int n,x;
	
	cin >> n >> x;
	REP(i,n) cin >> t[i];

	sort(t,t+n);

	int j = 0;

	int counter = 0;
	FORD(i,n-1,0){
		if(i < j) break;
		++counter;
		if(t[i]+t[j] <= x) ++j;
	}	

	cout << counter;
}

int main(){
	ios_base::sync_with_stdio(false);
	int t;
	cin >> t;

	FOR(i,1,t){
		cout << "Case #" << i << ": ";
		testcase();
		cout << endl;
	}

	return 0;
}
