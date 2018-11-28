#include<iostream>
#include<string>

using namespace std;

string lastNum(string inp){
	string ret;
	
	ret = inp.at(0);

	for(int i = 1; i<inp.size(); i++){
		if(ret[0] > inp.at(i)){
			ret = ret + inp[i];
		} else {
			ret = inp[i] + ret;
		}
	}

	return ret;
}

int main(){
	int T;
	string inp;

	cin >> T;
	//T = 1;

	for(int i = 0; i<T; i++) {
		cin >> inp;
		string y = lastNum(inp);
		cout << "Case #" << i+1 << ": " << y << endl;
	}

}
