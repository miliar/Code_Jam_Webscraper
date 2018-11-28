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

const string gabriel = "GABRIEL\n";
const string richard = "RICHARD\n";

void testcase(){
	int x,r,c;

	cin >> x >> r >> c;

	if(r*c % x != 0){
		cout << richard;
		return;
	}

	switch(x){
		case 1:
			cout << gabriel;
			break;
		case 2:
			cout << gabriel;
			break;
		case 3:
			if(min(r,c) == 1) cout << richard;
			else
				cout << gabriel;
			break;	
		case 4:
			if(max(r,c) < 4) cout << richard;
			else
				switch(min(r,c)){
					case 1:
						cout << richard;
						break;
					case 2:
						cout << richard;
						break;
					case 3:
						cout << gabriel;
						break;
					case 4:
						cout << gabriel;
				}
	}
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
