#include<bits/stdc++.h>
using namespace std;
#define mp make_pair
pair<char, bool> product(char first, char second){ // positive: 0 negative: 1
	if(first == '1' && second == '1') return mp('1', 0);
	if(first == '1' && second == 'i') return mp('i', 0);
	if(first == '1' && second == 'j') return mp('j', 0);
	if(first == '1' && second == 'k') return mp('k', 0);
	if(first == 'i' && second == '1') return mp('i', 0);
	if(first == 'i' && second == 'i') return mp('1', 1);
	if(first == 'i' && second == 'j') return mp('k', 0);
	if(first == 'i' && second == 'k') return mp('j', 1);
	if(first == 'j' && second == '1') return mp('j', 0);
	if(first == 'j' && second == 'i') return mp('k', 1); 
	if(first == 'j' && second == 'j') return mp('1', 1);
	if(first == 'j' && second == 'k') return mp('i', 0);
	if(first == 'k' && second == '1') return mp('k', 0);
	if(first == 'k' && second == 'i') return mp('j', 0);
	if(first == 'k' && second == 'j') return mp('i', 1);
	if(first == 'k' && second == 'k') return mp('1', 1);
}


int main(){
	freopen("fuckyeah.in", "r", stdin);
	freopen("fuckyeah.o", "w", stdout);
	int tc; cin >> tc;
	for(int a = 1; a <= tc; a++){
		int L, X; cin >> L >> X;
		string s = ""; char temp;
		for(int i = 0; i < L; i++){
			cin >> temp;
			s += temp;
		}
		string tot = "";
		for(int i = 0; i < X; i++){
			tot += s;
		}
		int sign = 0;
		bool failed = false;
		while(true){
			
			if(tot.size()==0){
				failed = true;
				break;
			}
			if(tot[tot.size()-1]=='k'){
				tot.pop_back();
				break;
			}
			if(tot.size() < 2){
				failed = true;
				break;
			}
			pair<char, bool> res = product(tot[tot.size()-2], tot[tot.size()-1]);
			tot.pop_back();
			tot[tot.size()-1] = res.first;
			sign += res.second;
		}

		while(true){
			if(tot.size()==0){
				failed = true;
				break;
			}
			if(tot[tot.size()-1]=='j'){
				tot.pop_back();
				break;
			}
			if(tot.size() < 2 && tot != "ij"){
				failed = true;
				break;
			}
			pair<char, bool> res = product(tot[tot.size()-2], tot[tot.size()-1]);
			tot.pop_back();
			tot[tot.size()-1] = res.first;
			sign += res.second;
		}
		
		while(true){
			if(tot.size()==0){
				failed = true;
				break;
			}
			if(tot[tot.size()-1]=='i'){
				tot.pop_back();
				break;
			}
			if(tot.size()==1){
				failed = true;
				break;
			}
			pair<char, bool> res = product(tot[tot.size()-2], tot[tot.size()-1]);
			tot.pop_back();
			tot[tot.size()-1] = res.first;
			sign += res.second;
		}
		if(tot.size() != 0){
			while(true){
			
				if(tot[tot.size()-1]=='1' && tot.size()==1 && sign % 2 == 0){
					break;
				}
				if(tot.size()==1 && (tot[0] != '1' || sign % 2 != 0) ){
					failed = true;
					break;
				}
				pair<char, bool> res = product(tot[tot.size()-2], tot[tot.size()-1]);
				tot.pop_back();
				tot[tot.size()-1] = res.first;
				sign += res.second;
			}
		}
		if(failed==false && sign % 2 == 0) cout << "Case #" << a << ": YES\n";
		else cout << "Case #" << a << ": NO\n";
	}
}
