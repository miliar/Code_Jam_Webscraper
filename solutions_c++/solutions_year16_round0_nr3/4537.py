#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;


long long toBase(string str, int base){
	long long res = 0;
	long long plus;

	for(int i = 0; i < str.size(); i++){

		plus = ((long long)str[i] - 48) * (long)pow(base, str.size()-i-1);
		//cout << "STR: " << str << " :"<< plus << endl;
		res = res + plus;
	}
	//cout << "base " << base << ": " << res << " "; 
	return res;
}

vector<long long> jamcoin(string str){
	vector<long long> res;
	bool isPrime = true;
	
	for(int i = 2; i<=10; i++) {
		long long val = toBase(str, i);
		isPrime = true;

		for(long long j = 2; j*j<=val; j++){
			if(val%j == 0) {
				res.push_back(j);
				isPrime = false;
				break;
			}
		}
		if(isPrime == true){
			vector<long long> r;
			return r;
		}
	}
	return res;
}


void returnNumber(int N, int J){
	int jcntr = 0;

	for(int i = 0; i < pow(2,N-2); i++) {
		string str = "1";
		for(int j = N-3; j >= 0; j--) {
			str = str + to_string(i/(long long)pow(2,j)%2);
		}
		str = str + "1";
    		//str = str + to_string(i/4%2) + to_string(i/2%2) + to_string(i%2) + "1";
		//cout << str << endl;

		if(jcntr < J) {
			vector<long long> r = jamcoin(str);
			if(r.size() != 0){
				jcntr++;	
				cout << str << " ";
				for(int p = 0; p<9; p++){
					//cout << "(" << toBase(str, p+2) << ")" << r[p] << " ";
					cout << r[p] << " ";
				}
				cout << endl;
			}
		} else {
			return;	
		}
	}

}

int main(){
	int T;
	int N;
	int J;
	cin >> T;
	//T = 1;

	for(int i = 0; i<T; i++) {
		cin >> N;
		cin >> J;
		cout << "Case #" << i+1 << ":" << endl;
		returnNumber(N, J);	
	}	
	return 0;
	
}
