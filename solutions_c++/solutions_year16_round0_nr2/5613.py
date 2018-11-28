#include<iostream>
#include<algorithm>
#include<vector>
#include<set>

using namespace std;

int returnNumber(string inp){
	int res = 0;

	int i = 0;
	
	while(i < inp.size()){
		char c = inp[0];
		for(i = 0; i<inp.size(); i++){
			if(c != inp[i]) {
				res++;
				break;
			} 
		}

		if(i == inp.size() && inp[0] == '+'){
			return res;
		} else if(i == inp.size() && inp[0] == '-'){
			res++;
			return res;
		} 
	
		c = inp[0];
		for(int j = 0; j<i; j++){
			if(c == '+'){
				inp[j] = '-';
			} else {
				inp[j] = '+';
			}
		}
	}
	if(inp[0] == '-')
		res = res +1;
	return res;
}

int main(){
	int T;
	long val;
	string inp;

	cin >> T;
	//T = 1;

	for(int i = 0; i<T; i++) {
		cin >> inp;
		int y = returnNumber(inp);
		cout << "Case #" << i+1 << ": " << y << endl;
	}
	
	return 0;
	
}
