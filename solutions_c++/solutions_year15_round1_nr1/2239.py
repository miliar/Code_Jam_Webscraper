#include<iostream>
#include<vector>
#include<fstream>
using namespace std;

int main() {
	int t, n, min1, min2, rate;
	fstream f,o;
	o.open("A.in");
	f.open("ansA.txt");
	o >> t;
	for(int k = 1; k <= t; ++k) {
		min1 = min2 = rate= 0;
		o >> n;
		vector<int> mush(n);
		for(int i = 0; i < n; ++i)
			o >> mush[i];
		for(int i = 1; i < n; ++i)
			if(mush[i] < mush[i-1])
				min1 += mush[i-1]-mush[i];
		for(int i = 0; i < n-1; ++i)
			if(mush[i]-mush[i+1] > rate)
				rate = mush[i]-mush[i+1];
		for(int i = 0; i < n-1; ++i) {
			if(mush[i] < rate)
				min2 += mush[i];
			else
				min2 += rate;
		}
		f << "Case #" << k << ": " << min1 << " " << min2 << endl;
	}
	return 0;
}
