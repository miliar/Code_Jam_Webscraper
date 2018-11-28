#include <iostream>
#include <algorithm>
using namespace std;

int cases;
int capacity, files, file[10000];
bool used[10000];

int main() {
	cin>>cases;
	for (int c = 1; c <= cases; c++) {
		cin>>files>>capacity;

		for (int i = 0; i < files; i++) {
			cin>>file[i];
			used[i] = false;
		}
		int disks = 0;
		sort (file, file + files);

		for (int i = files-1; i >= 0; i--) {
			if (used[i]) continue;
			// find largest to party with us
			for (int j = i-1; j >= 0; j--) {
				if (used[j]) continue;
				if (file[j] + file[i] > capacity) continue;
				used[j] = true;
				break;
			}
			used[i] = true;
			disks++;
		}
		cout<<"Case #"<<c<<": "<<disks<<"\n";
	}
}