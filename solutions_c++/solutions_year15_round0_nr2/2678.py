#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n;
int maxi = 0;

void qwe(int cs) {
	int wyn;
	cin >> n;
	vector<int> nalesniki(n);
	for(int i = 0; i < n; ++i) {
		cin >> nalesniki[i];
	} 
	sort(nalesniki.begin(), nalesniki.end());
	reverse(nalesniki.begin(), nalesniki.end());
	maxi = nalesniki[0];
	wyn = maxi;
	for(int i = 1; i < maxi+1; ++i) {
		int lwyn = i;
		for(int x = 0;(x < nalesniki.size()) && nalesniki[x] > i; ++x) {
			int k = nalesniki[x];
			if(k % i == 0) 
				lwyn += k/i-1;
			else 	
				lwyn += k/i;
		}
		wyn = min(wyn,lwyn);
	}
	cout << "Case #" << cs << ": " << wyn << endl;
}

int main()
{
	ios_base::sync_with_stdio(0);
	int z;
	cin >> z;
	for(int i = 1;i<=z; ++i)
		qwe(i);
	return 0;
}
