#include <iostream>
#include <array>
#include <vector>
#include <stdio.h>
#include <algorithm>

using namespace std;

#define ull unsigned long long


#define dfor(i,n) for(ull i = 0; i < n; i++)
#define rfor(i,n) for(ull i = n-1;i >=0; i--)
#define all(k) k.begin(),k.end()
#define ifor(i,b,n) for(auto i=b, i!=n, i++)



template<typename it>
int bbsort(it first, it last)
{
	it i, j;
	if (first ==last) return 0;
	int count = 0;
	for (i = first; i != last; i++) {
		for(j = i; j != last-1; j++) {
			if (*(j+1) < *j) {
				swap(*j,*(j+1));
				count++;
			}
		}
	}
	return count;
}

template<typename it>
int bbsort2(it first, it last)
{
	it i, j;
	if (first ==last) return 0;
	int count = 0;
	for (i = first; i != last; i++) {
		for(j = i; j != last-1; j++) {
			if (*(j+1) > *j) {
				swap(*j,*(j+1));
				count++;
			}
		}
	}
	return count;
}


void solv()
{
	int N;
	int K;

	cin >> N >> K;

	vector <int> v;
	bool b[10000];

	memset(b, 0, sizeof b);
	
	dfor(i, N) {
		int tmp;
		cin >> tmp;
		v.push_back(tmp);
	}
	
	sort(all(v));
	reverse(all(v));

	int count = 0;
	int ans = 0;

	for (int count = 0; count < N;) {
		int limit = 2;
		int cap = K;
		ans++;
		dfor(i, N) {
			if (cap >= v[i] && b[i] ==false) {
				cap -= v[i];
				b[i] = true;
				limit --;
				count++;
			} 
			if (limit ==0) break;
		}
	}
	cout << ans;

}


int main () {

	int T, cases = 0;
	cin >> T;
	while (T--) {
		cout << "case #" << ++cases << ": " ;
		solv();
		cout << endl;
	}
	
	return 0;
}
