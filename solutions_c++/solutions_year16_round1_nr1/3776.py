#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int main () {
	ifstream in("A-large.in");
	ofstream out("A-large.out");
	int t;
	in>>t;
	for(int i=0;i<t;i++){
		string s;
		in>>s;
		vector<char> v;
		v.push_back(s[0]);
		for(int j=1;j<s.length();++j){
			if(s[j]>=v[0]){
				vector<char>::iterator it;
				it = v.begin();
				v.insert(it,s[j]);
			}else
				v.push_back(s[j]);
		}
		out<<"Case #"<<i+1<<": ";
		for(vector<char>::iterator it=v.begin();it!=v.end();++it)
			out<<*it;
		out<<endl;
	}
	return 0;
}

