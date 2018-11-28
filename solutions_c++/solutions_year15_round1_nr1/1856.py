#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <utility>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cstdio>

#define INF 1000000000

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef pair<int, ii> iii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<iii> viii;

int main() {
	int nCases;
	cin >> nCases;
	for (int cnum = 1; cnum <= nCases; cnum++) {
        int total = 0;
        int maxdiff = 0;
        int N;
        cin >> N;
        int last;
        cin >> last;
        vi nums;
        nums.push_back(last);
        for (int i = 1; i < N; i++)
        {
            int cur;
            cin >> cur;
            int diff = last - cur;
            if (diff > 0)
            {
                total += diff;
            }
            if (diff > maxdiff)
            {
                maxdiff = diff;
            }
            nums.push_back(cur);
            last = cur;
        }
        int othertotal = 0;
        last = nums[0];
        for (int i = 1; i < N; i++)
        {
            int cur = nums[i];
            if (last >= maxdiff)
            {
                othertotal += maxdiff;
                //printf("%d\n",maxdiff);
            }
            else
            {
                othertotal += last;
                //printf("%d\n",last);
            }
            last = cur;
        }
        cout << "Case #" << cnum << ": " << total << " " << othertotal << endl;
	}
}
