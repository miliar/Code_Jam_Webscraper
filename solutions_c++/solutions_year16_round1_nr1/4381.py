#include <iostream>
#include <vector>
#include <list>
#include <utility>

using namespace std;

string lastWord(string &word){
	list<char> final;
	final.push_back(word[0]);
	for(int i=1; i<word.size();i++){
		if(word[i]>=final.front()){
			final.push_front(word[i]);
		}else{
			final.push_back(word[i]);
		}
	}

	string res;
	res.resize(word.size());
	int i = 0;
	for(list<char>::iterator it=final.begin(); it!=final.end(); it++){
		res[i] = *it;
		i++;
	}
	return res;
}

int main(){
	int T;
	cin >> T;
	vector<string> res(T);
	string aux;
	getline(cin, aux, '\n');
	for(int i=0; i<T; i++){
		string word;
		getline(cin, word, '\n');
		res[i] = lastWord(word);
	}

	for(int i=0; i<T; i++){
		cout << "Case #" << i+1 << ": " << res[i] << endl;
	}
	return 0;
}