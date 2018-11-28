#include <leetcode>
#include <iostream>
#include <vector>
using namespace std;
#define MXLOOP 1000
bool all_visited(vector<bool>& v) {
    bool all = true;
    for(const auto& ele:v) {
	if(ele == false) all = false;
    }
    return all;
}

void set_visited(int n, vector<bool>& v) {
    while(n > 0) {
	v[(n - n / 10 * 10)] = true;
	n /= 10;
    }
}

int count(int n) {
    if(n == 0) return -1;
    vector<bool> visited(10, false);
    int loop = 0, new_n = 0;
    while(!all_visited(visited) && loop < MXLOOP) {
	new_n += n;
	set_visited(new_n, visited);
	loop++;
    }
    return loop >= MXLOOP ? -1 : new_n;
}

int main() {
    int T = 0, N = 0;
    cin >> T;
    for(int i = 1; i <= T; ++i) {
	cin >> N;
	int ret = count(N);
	if(ret == -1) {
	    cout << "Case #" << i << ": " << "INSOMNIA\n";
	}else {
	    cout << "Case #" << i << ": " << ret << "\n";
	}
    }
}
