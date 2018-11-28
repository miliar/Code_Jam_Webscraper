#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <list>
#include <algorithm>
using namespace std;

bool check_train(vector<string>&sofar) {
  map<char, int> o;
	char prev_char = ' ';
	for (int i =0 ;i < sofar.size(); i++) {
		const char* t = sofar[i].c_str();
		int len = sofar[i].length();
		int j = 0;
		while(j < len) {
						if ( prev_char != ' ') {
							if (prev_char!=t[j]) {
							    o[t[j]]++;	
									if (o[t[j]] > 1) {
										return false;
									}
							}
						} else {
							o[t[j]]++;
							if (o[t[j]] > 1) {
									return false;
							}
						}
						prev_char = t[j];
						j++;
		}
	}
	return true;

}

void printit(const string &i) {
	cout<<i<<" ";
}
void descend(vector<string> & inp, vector<int>& used, vector<string>& sofar, long long int &res) {
	if (used.size() == inp.size()) {
		//for_each(sofar.begin(), sofar.end(), printit);
		//cout<<endl;
		if (check_train(sofar)) {
			res++;
			if (res == 1000000007) {
				res = 0;
			}
		}
		return;
	}
	for (int i = 0; i< inp.size(); i++) {
		if (find(used.begin(), used.end(), i) == used.end())	{
			/*if (sofar.size() >=1) {
			string &t = sofar.back();
			const char* ti = sofar.back().c_str();
			if (ti[t.length() -1] == (inp[i].c_str())[0]) {
				used.push_back(i);
				sofar.push_back(inp[i]);
				descend(inp, used, sofar, res); 
				used.pop_back();
				sofar.pop_back();
			}
			} else {*/
				used.push_back(i);
				sofar.push_back(inp[i]);
				descend(inp, used, sofar, res); 
				used.pop_back();
				sofar.pop_back();
			/*}*/
		}
	}
}
int main() {
	fstream f;
	f.open("a.dat", ios::in);
	if (!f.is_open()) {
		throw "Failed to open";
	}

	int T;

	f>>T;

	for (int i =0;i<T;i++) {
		cout<<"Case #"<<(i+1)<<": ";
	    // your code here
		int N;

		f>>N;

		vector<string> inp;
		vector<int> used;
		vector<string> result;
		long long int res = 0;
		for(int j = 0; j< N; j++) {
			string a;
			f>>a;	
			inp.push_back(a);
	 	}

		descend(inp, used, result, res); 
		cout<<res<<endl;
	}

	return 0;
}
