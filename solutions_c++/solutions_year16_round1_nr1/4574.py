#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

string process(string in){
	vector<string> words;
	vector<string> temp;
	words.push_back(string(1,in[0]));
	for(auto i = in.begin()+1;i < in.end(); i++) {
		temp.clear();
		for(string s : words) {
			temp.push_back(s+*i);
			temp.push_back(*i+s);
		}
		words = temp;
	}
	sort(words.begin(), words.end());
	return words.back();
}

int main() {
	ofstream out;
	ifstream in;

	const string name = "small";

	out.open(name+".out");
	in.open(name+".in");

	int T;
	in >> T;
	
	for(int i = 1; i <= T;i++) {
		string word;
		in >> word;
		string result = process(word);
		out << "Case #" << i << ": " << result << endl;
		cout << "Case #" << i << ": " << result << endl;
	}
}
