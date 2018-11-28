#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int N,M[1000];
	
int main() {
	int T; 
	cin >> T;
	for(int Z = 1; Z <= T; Z++) {
		cin >> N;
		for(int i = 0; i < N; i++)
			cin >> M[i];
		
		int ans1 = 0, ans2 = 0, maxdrop = 0;
		for(int i = 1; i < N; i++)
			if(M[i] < M[i-1]) {
				ans1 += M[i-1] - M[i];
				maxdrop = max(maxdrop, M[i-1] - M[i]);
			}
		
		ans2 = 0;
		for(int i = 1; i < N; i++)
			if(M[i-1] <= maxdrop)
				ans2 += M[i-1];
			else 
				ans2 += maxdrop;
		
		cout << "Case #" << Z << ": " << ans1 << " " << ans2 << endl;
	}
}