#include <iostream>
#include <unordered_set>
#include <unordered_map>


using namespace std;


int main(){

	int tc,n;
	cin>>tc;
	for(int i = 0; i < tc; i++){
		cin>>n;
		int curr = n;
		unordered_set<int> set;
		unordered_map<int,bool> map;
		string res;
		int k = 2;
		while(1){
		string s = to_string(curr);
		for(int i = 0; i < s.length(); i++){
			set.insert(s[i] - '0');
		}

		if(set.size() == 10){
			res = "Case #" + to_string(i+1) +": " + to_string(curr);
			cout<<res<<endl;
			break;
		}
		else{
			if(map[curr]){
				res = "Case #" + to_string(i+1)+": INSOMNIA";
				cout<<res<<endl;
				break;
			}
			map[curr] = true;
			curr = k*n;
			k++;
		}
	}

	}

}