#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

int T, n;


int main() {
	cin.sync_with_stdio(false);
	
	cin >> T;
	
	for(int TCASE = 1; TCASE <= T; TCASE++) {
		vector<string> words, sentence[20];
	
		cin >> n;
		
		string w;
		
		int l = 0;
		
		while(l < n) {
			cin >> w;
			
			words.push_back(w);
			sentence[l].push_back(w);
			
			if(cin.peek() == '\n')
				l++;
		}
		
		
		sort(words.begin(), words.end());
		words.resize(unique(words.begin(), words.end() )  -  words.begin() );
		
		
		vector<int> *lapp = new vector<int> [words.size()];
		
		
		for(int s=0;s<n;s++)
			for(int i=0;i<sentence[s].size();i++) {
			
				int wind = lower_bound(words.begin(), words.end(), sentence[s][i])  - words.begin();
				
				lapp[wind].push_back(s);
			}
		
		
		//Finally try out all the combinations
		int result = 1000000000;
		
		for(int comb=1; comb < (1 << n); comb += 4) {
			
			int cres = 0;
			
			//check whether word belongs into both languages or not
				
			for(int i=0;i<words.size();i++) {
				
				int belong = 0;
				
				for(int j=0;j<lapp[i].size();j++) {
					
					int cbel = ( 1 << int( (comb & (1 << lapp[i][j]) ) != 0)   );
					
					belong = (belong | cbel);
				}
				
				
				if(belong == 3)
					cres++;
			}
			
			result = min(result, cres);
			
		}
		
		
		
		//Finally output the result
		
		cout << "Case #" << TCASE << ": " << result << '\n';
	}
	
	
	return 0;
	
}



































