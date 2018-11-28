#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
#include <sstream>
using namespace std;



bool smallerthan(string s1,string s2){
	if(s1.size()!=s2.size()) return (s1.size()<s2.size());
	else return (s1<s2);
}

int main(){
	int cnt = 0;
	ifstream fin2("fileout.txt");
	string s;
	getline(fin2,s);
	vector<string> vs;
	while(!fin2.fail()){
		vs.push_back(s);
		getline(fin2,s);
	}
	cout << "Please download data and press any key when ready" << endl;
	char c;
	cin >> c;

	ifstream fin("C-Large-2.in");
	ofstream fout("C-Large-2.out");
	int T;
	fin >> T;
	for(int t=0;t<T;t++){
		string A,B;
		fin >> A >> B;
		int i1 = lower_bound(vs.begin(),vs.end(), A,smallerthan)-vs.begin();
		int i2 = lower_bound(vs.begin(),vs.end(),B,smallerthan)-vs.begin();
		if(i2<vs.size() && vs[i2] == B) i2++;
		
		fout <<"Case #"<< t+1<< ": " << i2-i1 << endl;

	}
	
	return 0;
}

