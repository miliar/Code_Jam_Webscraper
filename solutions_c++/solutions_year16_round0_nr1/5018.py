#include <iostream>
#include <cstring>
#include <fstream>
using namespace std;

#define cin fin
#define cout fout

ifstream fin("A-large.in");
ofstream fout("a.out");

long long getResult(long long n) {
	bool visited[10];
	memset(visited, 0, sizeof(visited));
	long long count = 0;
	
	long long curr = 0;
	while (count < 10) {
		curr += n;
		long long curr_cp = curr;
		
		while (curr_cp > 0) {
			long long tmp = curr_cp % 10;
			curr_cp /= 10;
			
			if (!visited[tmp]) {
				visited[tmp] = true;
				count++;
			}
		}
	}
	
	return curr;
}

int main() {
	long long cases;
	cin >> cases;
	
	for (long long cnt = 1; cnt <= cases; cnt++) {
		long long n;
		cin >> n;
		
		cout << "Case #" << cnt << ": ";
		
		if (n == 0) {
			cout << "INSOMNIA" << endl;
		} else {
			cout << getResult(n) << endl;
		}
	}
	
	return 0;
}
