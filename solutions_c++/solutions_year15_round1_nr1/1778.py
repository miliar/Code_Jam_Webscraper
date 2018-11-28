#include <iostream>
#include <string>
#include <vector>

#define f(i,N) for(int i = 0; i != N; i++)
#define fl(i,N) for(int i = 1; i <= N; i++)

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vii;
#define pb(x) push_back(x)

int main() {
	int T;
	cin >> T;
	for(int i = 1; i <= T; i++) {
		int N;
		cin >> N;
		int A[N],eats=0,Max = 0,E = 0;
		f(j,N)
			cin >> A[j];
		f(j,N-1) {
			int diff = A[j] - A[j+1]; 
			if(diff >= 0)
				eats+=diff;
			Max = max(diff,Max);
		}
		f(j,N-1) {
			if(Max > A[j])
				E+=A[j];
			else
				E+=Max;
		}
		cout << "Case #"<< i << ": " << eats << ' ' << E << endl;
	}
	return 0;
}
