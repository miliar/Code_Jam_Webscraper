//by Naciraa
#include <iostream>
#include <queue>
#include <string>
#include <map>

using namespace std;

string flip(string str,int i){
	string res = str;
	for(int j = 0; j<=i; j++){
		if(str[j] == '-'){
			res[i-j] = '+';
		}else{
			res[i-j] = '-';
		}
	}
	return res;
}


int main(){
	int t;
	cin >> t;
	int curr_case = 1;
	while(curr_case <= t){
		string s;
		cin >> s;
		
		
		queue< string> q;
		map< string, int> dists;
		dists[s] = 0;
		q.push(s);
		while(!q.empty()){
			string curr = q.front();
			q.pop();
			for(int i =0 ; i<curr.length(); i++){
				string fliped = flip(curr, i);
				//cout << fliped << endl;
				if(dists.find(fliped) == dists.end()){ // si es distinto al  .end() del map es que esta definido, sino no esta definido en el map.
					dists[fliped] = dists[curr] + 1;
					q.push(fliped);
				}
			}
		}
		
		string res = "";
		for(int i =0 ; i < s.length(); i++){
			res = res + "+";
		}
		//cout << res << endl;
		cout << "Case #" << curr_case << ": " << dists[res] << endl;
		curr_case++;
	}
	
	return 0;
}