#include <fstream>
#include <string>
#include <vector>
#include <math.h>
using namespace std;

struct Character {
	Character(char ch,int num=1)
		: num(num), ch(ch) {};
	int num;
	char ch;
};

struct Str {
	Str() {};

	Str(const string & word) {
		Character current(word.at(0));
		for (int i=1;i<word.size();i++) {
			if (current.ch==word.at(i)) current.num++;
			else {
				chars.push_back(current);
				current.ch=word.at(i);
				current.num=1;
			}
		}
		chars.push_back(current);
	}
	vector<Character> chars;
};

bool CompareStr(const Str & str1, const Str & str2) {
	if (str1.chars.size()!=str2.chars.size()) return false;
	for (int i=0;i<str1.chars.size();i++)
		if (str1.chars[i].ch!=str2.chars[i].ch) return false;
	return true;
}

int FindAverage(const string & common_word, const vector<Str> & words) {
	Str average(common_word);
	int change=0;
	for (int i=0;i<average.chars.size();i++) average.chars[i].num=0;
	for (int i=0;i<words.size();i++) {
		for (int j=0;j<words[0].chars.size();j++) {
			average.chars[j].num += words[i].chars[j].num;
		}
	}
	for (int i=0;i<average.chars.size();i++) {
		double remain = fmod((double)average.chars[i].num/words.size(),1.0);
		double avg;
		bool up=true;
		if (remain <= 0.5) up=false;
		if (up) 
			average.chars[i].num =  ceil((double)average.chars[i].num/words.size());
		else
			average.chars[i].num =  floor((double)average.chars[i].num/words.size());
	}

	for (int i=0;i<words.size();i++) {
		for (int j=0;j<words[0].chars.size();j++) {
			change += abs(words[i].chars[j].num - average.chars[j].num);
		}
	}
	return change;
}

int main() {

	ifstream input("input.txt");
	ofstream out("out.txt");
	int t;
	input >> t;
	for (int i=0;i<t;i++) {
		int n;
		input >> n;
		vector<Str> words;
		string word;
		input >> word;
		Str first_word(word);
		words.push_back(first_word);
		bool solution=true;
		string temp;
		for (int j=1;j<n;j++) {
			input >> temp;
			Str new_word(temp);
			if (!CompareStr(first_word,new_word)) {solution=false; break;}
			words.push_back(new_word);
		}
		if (!solution) out << "Case #" << (i+1) << ": " << "Fegla Won" << endl;
		else {
			int a = FindAverage(word,words);
			out << "Case #" << (i+1) << ": " << a << endl;
		}
	}
	out.close();
	return 0;
}