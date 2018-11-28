#include <iostream>
#include <string>
#include <set>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

int solve(int A, int B, int K) {
	int ans=0;
	for (int i=0; i<A; i++)
		for (int j=0; j<B; j++) {
			//cout << i << " " << j << " " << (i&j) << endl;
			if ((i&j)<K) {
				ans++;
			}
		}
    return ans;
}

int main() {
    freopen("B-small-attempt0.in", "rt", stdin);
    //freopen("test.in", "rt", stdin);
    freopen("B-small.out", "wt", stdout);
   
    int N;
    cin>>N;

    for (int i=1; i<=N; i++) {
        int A,B,K;
		cin>>A>>B>>K;
        cout << "Case #" << i << ": " << solve(A,B,K) << endl;
    }
}