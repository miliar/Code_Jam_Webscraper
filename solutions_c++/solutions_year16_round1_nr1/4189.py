#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

void calculate_last_words(const string &S, string& current, int start, vector<string>& last_words, map<string, bool>& searched){
	string s1;
	string s2;
	if(searched.find(current) != searched.end())
		return;
	s1 = current + S[start];
	s2 = S[start] + current;
	if(start + 1 >= S.size()){
		last_words.push_back(s1);
		last_words.push_back(s2);
		return;
	}
	calculate_last_words(S, s1, start + 1, last_words, searched);
	searched[s1] = true;
	calculate_last_words(S, s2, start + 1, last_words, searched);
	searched[s2] = true;
}


void calculate_last_words_fast(string &S, string biggest, int start, vector<string>& last_words){
	string s1 = biggest + S[start];
	string s2 = S[start] + biggest;
	if(start + 1 >= S.size()){
		last_words.push_back(s1);
		last_words.push_back(s2);
		return;
	}
	if(s1 > s2){
		calculate_last_words_fast(S, s1, start + 1, last_words);
	}else{
		calculate_last_words_fast(S, s2, start + 1, last_words);
	}
}



int main(){
	int T;
	cin >> T;
	for(int i = 1; i <= T; ++i){
		map<string, bool> searched;
		vector<string> last_words;
		string S;
		cin >> S;
		string str("");
		// calculate_last_words(S, str, 0, last_words, searched);
		calculate_last_words_fast(S, str, 0, last_words);
		sort(last_words.begin(), last_words.end());
		cout << "Case #" << i << ": " << last_words[last_words.size() - 1] << endl;
	}
	return 0;
}

