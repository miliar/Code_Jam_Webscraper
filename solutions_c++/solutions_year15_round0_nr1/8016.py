//
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;


int main () {	
	freopen("A-large.in", "r", stdin);
	freopen("A-large-out.txt", "w", stdout);
	int T;
	cin>>T;
	for(int t=1; t<=T; t++){
		int N;
		cin>> N;
		string s;
		cin >> s;
		int counts=0, needs=0;		
		for(int i=0; i<=N; i++){
			int k= s[i] - '0';			
			if(counts<i) {
				needs+= (i-counts);
				counts = i;
			}
			counts+= k;
		}		
		cout << "Case #" << t << ": " << needs << "\n";		
	}

return 0;
}
