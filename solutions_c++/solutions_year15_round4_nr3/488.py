#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;

int n;
map<string, int> mappa;
vector<int> frase[300];
int eng[5000];
int fra[5000];


int acc;
int ris(int de){
	if(de == n) return acc;
	if(de == 0){
		for(int s:frase[de]){if(eng[s]==0 && fra[s]>0) acc++; eng[s]++;}
		int r1 = ris(de+1);
		for(int s:frase[de]){if(eng[s]==1 && fra[s]>0) acc--; eng[s]--;}
		return r1;
	}
	if(de == 1){
		for(int s:frase[de]){if(fra[s]==0 && eng[s]>0) acc++; fra[s]++;}
		int r1 = ris(de+1);
		for(int s:frase[de]){if(fra[s]==1 && eng[s]>0) acc--; fra[s]--;}
		return r1;
	}
	
	for(int s:frase[de]){if(eng[s]==0 && fra[s]>0) acc++; eng[s]++;}
	int r1 = ris(de+1);
	for(int s:frase[de]){if(eng[s]==1 && fra[s]>0) acc--; eng[s]--;}
	for(int s:frase[de]){if(fra[s]==0 && eng[s]>0) acc++; fra[s]++;}
	int r2 = ris(de+1);
	for(int s:frase[de]){if(fra[s]==1 && eng[s]>0) acc--; fra[s]--;}
	return min(r1, r2);
}

void solve(){
	mappa.clear();
	int ind = 0;
	
	cin >> n;
	for(int i=0; i<n; i++){
		frase[i].clear();
		string line;
		getline(cin, line);
		if(line.size() == 0) getline(cin, line);
		istringstream ss(line);
		while(!ss.eof()){
			string s; ss >> s;
			if(mappa[s] == 0) mappa[s] = ++ind;
			frase[i].push_back(mappa[s]);
		}
	}
	for(int i=0; i<ind; i++) fra[i] = eng[i] = 0;
	acc = 0;
	//~ for(int i=0; i<n; i++){
		//~ cerr << i << ": ";
		//~ for(string s:frase[i]) cerr << s << ';';
		//~ cerr << endl;
	//~ }
	cout << ris(0);
	
}

int main(){
	int t; cin >> t;
	for(int i=1; i<=t; i++){
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}
	
	return 0;
}
