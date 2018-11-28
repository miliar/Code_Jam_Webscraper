#include <iostream>
#include <utility>
#include <queue>
using namespace std;

int cases;
int buildings;
int building[1000][4];
bool seen[1000];
int width, height;

// d infinite dist between these two.
int distof (int a, int b) {
	int xdif = max(building[a][0] - building[b][2], building[b][0] - building[a][2]);

	int ydif =  max(building[a][1] - building[b][3], building[b][1] - building[a][3]);

	return max(xdif, ydif) - 1;
}	

int main() {
	cin>>cases;
	for (int c = 1; c <= cases; c++) {
		cin>>width>>height>>buildings;
		for (int i = 0; i < buildings; i++) {
			cin>>building[i][0]>>building[i][1]>>building[i][2]>>building[i][3];
			seen[i] = false;
		}
		

		int bestDist = width;
		priority_queue<pair<int, int> > proc;

		// add initials. We go left to right.
		for (int i = 0; i < buildings; i++) {
			proc.push(make_pair(-building[i][0], i));
		}

		while (proc.size()) {
			int b = proc.top().second;
			int d = -proc.top().first;
			proc.pop();

			if (seen[b]) continue;
			seen[b] = true;

			bestDist = min(bestDist, d + width - building[b][2] - 1);

			// neighbours
			for (int i = 0; i < buildings; i++) {
				proc.push(make_pair(-d - distof (b, i), i));
			}
		}

		cout<<"Case #"<<c<<": "<<bestDist<<"\n";
	}
}