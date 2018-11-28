#include <iostream>
using namespace std;

//find a in b
bool find(string &a, string &b){
	int i = 0, j = 0;
		for(; j < b.size(); ++j){
			if(a[i] == b[j]){
				++i;
			}
		}
		if(i < a.size()) return false;
		//remove a in b
		for(int o = 0; o < a.size(); o++){
			b.erase(b.begin()+b.find(a[o]));
		}
		return true;
}

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	string digits[10] = {"EORZ","ENO", "OTW", "EEHRT", "FORU", "EFIV", "ISX", "EENSV", "EGHIT", "EINN"};
	int seq[10] = {0, 2, 6, 8, 7, 5, 9, 3, 4, 1};
	int tt = 1;
	int tn; cin >> tn;
	string line;
	
	for(; tt <= tn; tt++) {
		string result;
		cin>>line;
		sort(line.begin(), line.end());
		for(int i = 0; i < 10; ){
			if(find(digits[seq[i]], line)){
				result += to_string(seq[i]);
			}else{
				++i;
			}
		}
		sort(result.begin(), result.end());
		cout<<"Case #"<<tt<<": "<<result<<endl;
		
	}
	
}