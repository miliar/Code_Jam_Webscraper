#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int t;
	cin >> t;
	for (int tcs = 1; tcs <= t; tcs++) {
		int n;
		cin >> n;
		vector <pair <int, char> > vet; 
		int total = 0;
		for (int i = 0; i < n; i++) {
			int n;
			cin >> n;
			total += n;
			char ch = 'A' + i;
			pair <int, char> temp;
			temp = make_pair(n, ch);
			vet.push_back(temp);
		}
		sort(vet.begin(), vet.end());
		//for (int i = 0; i < n; i ++)
			//cout << vet[i].first << " " << vet[i].second << endl;
		printf("Case #%d: ", tcs);
		while (total != 0) {
			if ( (vet[n-2].first) * 2 <= total - 2 && total - 2 >= 0 ) {
				cout << vet[n-1].second << vet[n-1].second << " ";
				vet[n-1].first -= 2;
				total -= 2;
			}
			else if ( (vet[n-2].first) * 2 <= total - 1 ) {
				cout << vet[n-1].second << " ";
				vet[n-1].first--;
				total --;
			}  
			else  {
				cout << vet[n-1].second << vet[n-2].second << " ";
				vet[n-1].first--;
				vet[n-2].first--;
				total -= 2;
				
			}
			//cout << "total >>> " << total << endl;
			sort(vet.begin(), vet.end());
			
		}
		cout << endl;
		
		
	}
	
	return 0;
}
