#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <utility>
#include <climits>

#define PB push_back
#define MP make_pair
#define MAX 1e10
#define all(v) v.begin(),v.end()

using namespace std;

int nTest, N, cases;

int gcd(int a, int b){return (a * b ? gcd(min(a, b), max(a, b) % min(a, b)) : max(a, b));}

int main() {
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);

    cin >> nTest;

    while(nTest--) {
        cin >> N;
        vector<double> v1, v2;
        int illegalAns = 0, legalAns = 0;
        double x;
        for(int i = 0; i < N; i++) cin >> x, v1.PB(x);
        for(int i = 0; i < N; i++) cin >> x, v2.PB(x);
        sort(v1.begin(), v1.end());
        sort(v2.begin(), v2.end());
        int i, j;
        i = j = 0;
        while(i < N && j < N) {
            if(v1[i] < v2[j]) legalAns++, i++, j++;
            else j++;
        }
        legalAns = N - legalAns;
        i = j = 0;
        while(i < N && j < N) {
            if(v2[j] < v1[i]) illegalAns++, i++, j++;
            else i++;
        }
        cout << "Case #" << ++cases << ": " << illegalAns << " " << legalAns << endl;
    }

	return 0;

}
