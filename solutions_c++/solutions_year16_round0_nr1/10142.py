#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <set>
using namespace std;


void divide(vector<bool> &mp, int N){
	if(N == 0){
		mp[0] = true;
		return;
	}
	while(N != 0){
		int t = N % 10;
		N = N / 10;
		mp[t] = true;
	}
}

bool check(vector<bool>& mp){
	bool result = 1;
	for(auto c : mp){
		result = result & c;
	}
	return result;
}



int main(){
	
	int T;
	ifstream in ("A-large.in");
	in >> T;
	ofstream out ("A-large.txt");
	for(int i = 1; i <= T; ++i){
		int N;
		in >> N;
		vector<bool> mp(10, false);
		int temp = N;
		set<int> record; 
		bool flag = 0;
		while(record.find(N) == record.end()){
			record.insert(N);
			divide(mp, N);
			if(check(mp)){
				out << "Case #" << i << ": " << N << endl ;
				flag = 1;
				break;
			}
			N += temp;
		}
		if(!flag){
			out << "Case #" << i << ": INSOMNIA" << endl ;
		}
	}
}
