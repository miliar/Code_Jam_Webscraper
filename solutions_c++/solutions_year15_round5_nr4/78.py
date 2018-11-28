#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;


int T, p, e[100000];
long long f[100000], comb[100000];






int main() {
	cin.sync_with_stdio(false);
	cin >> T;
	
	
	for(int TCASE = 1; TCASE <= T; TCASE++) {
		cin >> p;
		
		for(int i=0;i<p;i++)
			cin >> e[i];
			
		for(int i=0;i<p;i++)
			cin >> f[i];
			
		fill(comb, comb + 100000, 0);
		
		
		//Next we construct the initial set
		
		vector<int> initial;
		
		comb[0] = 1;
		
		
		for(int i=0;i<p;i++) {
			while(comb[i] < f[i]) {
				initial.push_back(e[i]);
				
				for(int j=p-1;j>=0;j--)
					for(int k=j;  k<p && e[k] <= e[j] + e[i]  ; k++)
						if(e[k] == e[j] + e[i])
							comb[k] += comb[j];
			}
			
		}
		
		
		cout << "Case #" << TCASE << ":";
		
		for(int i=0;i<initial.size();i++)
			cout << ' ' << initial[i];
		
		cout << '\n';
	}
	
	
	return 0;
}
