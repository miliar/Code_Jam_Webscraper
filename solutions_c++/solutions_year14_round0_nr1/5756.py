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

int nTest, cases, firstQuestion, secondQuestion, cntAns, ans;
bool ok[20];

int gcd(int a, int b){return (a * b ? gcd(min(a, b), max(a, b) % min(a, b)) : max(a, b));}

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);

    cin >> nTest;

    while(nTest--) {
        memset(ok, false, sizeof(ok));
        cntAns = 0;
        cin >> firstQuestion;
        for(int i = 1; i <= 4; i++)
            for(int j = 1, card; j <= 4; j++) {
                cin >> card;
                if(i == firstQuestion) ok[card] = true;
            }
        cin >> secondQuestion;
        for(int i = 1; i <= 4; i++)
            for(int j = 1, card; j <= 4; j++) {
                cin >> card;
                if(i == secondQuestion && ok[card]) ans = card, cntAns++;
            }
        cout << "Case #" << ++cases << ": ";
        if(!cntAns) cout << "Volunteer cheated!" << endl;
        else if(cntAns == 1) cout << ans << endl;
        else cout << "Bad magician!" << endl;
    }

	return 0;
}
