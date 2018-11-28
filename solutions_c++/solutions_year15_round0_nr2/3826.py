#include <iostream>
#include <set>
#include <algorithm>

using namespace std;

int currentMin;

int recr(const multiset<int, greater<int>> &plates, int steps) {
    if (steps >= currentMin) return currentMin;
    
    int max = *plates.begin();
    
    if (max <= 2) return max + steps;
    
    int half = max/2;
    currentMin = min(currentMin, max + steps);
    for (int i = half; i >= 1; --i) {
        // cout << i << endl;
        auto p2 = plates;
        p2.erase(p2.begin());
        p2.insert(i);
        p2.insert(max - i);
        currentMin = min(currentMin, recr(p2, steps + 1));
    }
    return currentMin;
}

void solve(int count) {
    int n;
    cin >> n;
    
    multiset<int, greater<int>> plates;
    for (int i = 0; i < n; ++i) {
        int tmp;
        cin >> tmp;
        plates.insert(tmp);
    }
    
    currentMin = *plates.begin();
    int steps = recr(plates, 0);
    cout << "Case #" << count << ": " << steps << endl;
}

int main(int argc, const char * argv[]) {
	int numCases = 0;
    cin >> numCases;
    
    for (int count = 1; count <= numCases; ++count) {
        solve(count);
    }
    return 0;
}

