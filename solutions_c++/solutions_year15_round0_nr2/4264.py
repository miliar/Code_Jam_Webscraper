#include <iostream>
#include <vector>
#include <string>
#include <stdlib.h>
#include <fstream>


using namespace std;

int find_max (vector<int> & pi) {
	int max = pi[0]; 
	for (int i = 1; i < pi.size(); ++i)
	{
		if (pi[i] > max) {
			max = pi[i];
		}
	}
	return max;
}

int min_sec(vector<int> & pi) {
	int count = 2;
	int sec = find_max(pi);
	if (sec < 4) return sec;
	while (count < sec) {
		int sum = 0;
		for (int i = 0; i < pi.size(); ++i)
		{
			sum += (pi[i] - 1) / count;
		}
		sec = min(sec, sum + count);
		count++;
	}
	return sec;
}




int main() {
	
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t = 0, d = 0, sec = 0;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cin >> d;
		vector<int> pi(d);

		for (int j = 0; j < pi.size(); j++) {
			cin >> pi[j];
		}
		cout << "Case #" << i << ": " << min_sec(pi) << endl;
	}

 	return 0;
}