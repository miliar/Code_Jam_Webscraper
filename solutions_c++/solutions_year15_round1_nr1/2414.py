#include <iostream>
#include <sstream>
#include <vector>
using namespace std;

int mushroomsEaten1(vector<int> m) {
	int total = 0;
	//mushrooms eaten per 10 seconds
	int eaten;
	for (int i = 1; i < m.size(); ++i) {
		eaten = m[i-1]-m[i];
		if (eaten > 0) total += eaten;
	}
	return total;
}

int mushroomsEaten2(vector<int> m) {
	int len = m.size();
	int total = 0;
	//find max eaten over a 10 second interval
	int diff = 0;
	int maxDiff = 0;
	for (int i = 1; i < len; ++i) {
		diff = m[i-1]-m[i];
		if (diff > maxDiff) maxDiff = diff;
	}
	//eat max or however many mushrooms are on plate;
	for (int i = 0; i < len-1; ++i) {
		if (m[i] < maxDiff) total += m[i];
		else total += maxDiff;
	}
	return total;
}

string mushroomsEaten(vector<int> m) {
	int total1 = mushroomsEaten1(m);
	int total2 = mushroomsEaten2(m);

	ostringstream t1, t2;
	t1 << total1;
	t2 << total2;
	return t1.str()+" "+t2.str();
}
int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i) {
		int plates;
		vector<int> shrooms;
		cin >> plates;
		for (int j = 0; j < plates; ++j) {
			int m;
			cin >> m;
			shrooms.push_back(m);
		}
		cout << "Case #" << i+1 << ": " << mushroomsEaten(shrooms) << endl;
	}
}