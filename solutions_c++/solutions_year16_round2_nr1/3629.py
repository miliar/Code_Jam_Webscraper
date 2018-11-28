#include<bits/stdc++.h>

using namespace std;

int t;
string s;
map<char,int> f;

vector<int> ans;

int main(){
	ofstream cout ("A.txt");
	cin.sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	cin >> t;
	int T = 1;
	while(t--){
		f.clear(), ans.clear();
		cin >> s;
		for(auto i: s) f[i]++;
		
		while(f['Z'] > 0 && f['E'] > 0 && f['R'] > 0 && f['O'] > 0){
			f['Z']--, f['E']--, f['R']--, f['O']--;
			ans.push_back(0);
		}
		
		while(f['W'] > 0 && f['T'] > 0 && f['O'] > 0){
			f['W']--, f['T']--, f['O']--;
			ans.push_back(2);
		}
		
		while(f['G'] > 0 && f['E'] > 0 && f['I'] > 0 && f['H'] > 0 && f['T'] > 0){
			f['E']--, f['I']--, f['G']--, f['H']--, f['T']--;
			ans.push_back(8);
		}
		
		while(f['X']  > 0 && f['S'] > 0 && f['I'] > 0){
			f['S']--, f['I']--, f['X']--;
			ans.push_back(6);
		}
		
		while(f['T'] > 0 && f['H'] > 0 && f['R'] > 0 && f['E'] > 1){
			f['H']--, f['T']--, f['R']--, f['E']--, f['E']--;
			ans.push_back(3);
		}
		
		while(f['F'] > 0 && f['O'] > 0 && f['U'] > 0 && f['R'] > 0){
			f['F']--, f['O']--, f['U']--, f['R']--;
			ans.push_back(4);
		}
		
		while(f['F'] > 0 && f['I'] > 0 && f['V'] > 0 && f['E'] > 0){
			f['F']--, f['I']--, f['V']--, f['E']--;
			ans.push_back(5);
		}

        	
		while(f['S'] > 0 && f['E'] > 1 && f['V'] > 0 && f['N'] > 0){
			f['S']--, f['E']--, f['V']--, f['E']--, f['N']--;
			ans.push_back(7);
		}
		
		while(f['O'] > 0 && f['N'] > 0 && f['E'] > 0){
			f['O']--, f['N']--, f['E']--;
			ans.push_back(1);
		}
		
		while(f['N'] > 1 && f['I'] > 0 && f['E'] > 0){
			f['N']--, f['I']--, f['N']--, f['E']--;
			ans.push_back(9);
		}
		
		for(auto i: f)
		 assert(i.second == 0);
		
		sort(ans.begin(),ans.end());
		cout << "Case #" << T++ << ": ";
		for(auto i: ans) cout << i;
		cout << '\n';
	}
  return 0;
}
