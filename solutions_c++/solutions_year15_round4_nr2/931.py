#include<iostream>
#include<iomanip>
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
	long double v,c,r1,r2,c1,c2;

	cin >> n >> v >> c;

	cin >> r1 >> c1;

	if(n==1){
		if(c == c1) cout << fixed << setprecision(9) << (v / r1);
		else
			cout << "IMPOSSIBLE";
	} else{
		cin >> r2 >> c2;
		if(c1 > c && c2 > c) cout << "IMPOSSIBLE";
		else
			if(c1 < c && c2 < c) cout << "IMPOSSIBLE";
			else
				if(c1 == c2 && c1 == c) cout << fixed << showpoint << setprecision(9) << (v / (r1+r2));
				else{
					auto v1 = c*v - c2*v;
		//			cout << "v1" << v1 << endl;
					v1 /= (c1-c2);
					auto v2 = v - v1;
			//		cout << "v1" << c1-c2 << endl;
//cout << "v1" << setprecision(9) << v1 << endl;

	//				cout << v1 << " " << v2 << endl;
					cout << fixed << setprecision(9) << max(v1/r1,v2/r2);
	//				printf("%.9Le\n",max(v1/r1,v2/r2));
				}
		}
}

int main(){
	ios_base::sync_with_stdio(0);

	int t;
	cin >> t;

	FOR(i,1,t){
		cout << "Case #" << i << ": ";
		testcase();
		cout << endl;
	}

	return 0;
}
