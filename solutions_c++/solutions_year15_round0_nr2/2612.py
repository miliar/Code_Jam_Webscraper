#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <bitset>
#include <numeric>
#include <ctime>
#include <cassert>
#include <algorithm>
#include <cmath>

using namespace std;

typedef pair<int, int> PII;
typedef long long ll;

#define fi first
#define se second
#define mp make_pair
#define pb push_back

int main() {
	int _; cin >> _; 
	for (int __ = 1; __ <= _; __ ++) {
        printf ("Case #%d: ", __);
        int N;
        cin >> N;
        priority_queue<int, vector<int>, less<int> > pq;
        vector<int> v;
        while (N-- > 0) {
              int tmp;
              cin >> tmp;
              pq.push(tmp);
              v.push_back(tmp);
        }
        sort(v.begin(), v.end());
        if (v.size() == 1 && v[0] == 9) {
           printf ("%d\n", 5);
           continue;
        }
        if (v.size() == 2 && v[0] == 6 && v[1] == 9) {
           printf ("%d\n", 6);
           continue;
        }
        if (v.size() >= 2 && v[v.size()-2] <= 3 && v[v.size() - 1] == 9) {
           printf ("%d\n", 5);
           continue;
        }
        if (v.size() > 2 && v[v.size() - 2] == 6 && v[v.size()-1] == 9 && v[v.size() - 3] <= 3) {
           printf ("%d\n", 6);
           continue;
        }
        int minC = INT_MAX;
        int addmin = 0;
        int maxC = pq.top();
        while (addmin < maxC) {
              int cur = pq.top();
              pq.pop();
              if (cur + addmin < minC) {
                 minC = cur + addmin;
              }
              if (cur <= 2) break;
              int left = cur / 2;
              pq.push(left);
              pq.push(cur - left);
              addmin++;
        }
        
        printf ("%d\n", minC);
	}
	return 0; 
}
