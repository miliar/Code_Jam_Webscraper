#include<iostream>
#include<vector>
#include<fstream>
using namespace std;

int main() {
	int t,n,max,total,min;
	fstream f;
	f.open("ansB.txt");
	cin >> t;
	for(int c = 1; c <= t; ++c) {
		min = 2147483647;
		max = 0;
		cin >> n;
		vector<int> pan(n);
		for(int i = 0; i < n; ++i) {
			cin >> pan[i];
			if(pan[i] > max) max = pan[i];
		}
		for(int eat = 1;eat <= max; ++eat) {
			total = eat;
			for(int i = 0; i < n; ++i)
				if(pan[i] > eat)
					total += (pan[i]-eat-1)/eat+1;
			if(total < min) min = total;
		}
		f << "Case #" << c << ": " << min << endl;
	}
	return 0;
}
