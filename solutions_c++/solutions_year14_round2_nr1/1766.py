#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

struct letter{
	char c;
	vector<int> occurances;
};

bool possible(const vector<string> & word){
	//check if possible
	for(int p = 0; p <= word.size()-2; p++){
		vector<char> one, two;

		for(int x = 0; x < word.at(p).length(); x++){
			if(one.size() == 0 || word.at(p).at(x) != one.back()){one.push_back(word.at(p).at(x));}
		}
		for(int y = 0; y < word.at(p+1).length(); y++){
			if(two.size() == 0 || word.at(p+1).at(y) != two.back()){two.push_back(word.at(p+1).at(y));}
		}

		if(one.size() != two.size()){return false;}
		else{
			for(int j = 0; j < one.size(); j++){if(one.at(j) != two.at(j)){return false;}}
		}
	}
	return true;
}

int abV(int num){
	if(num >= 0){return num;}
	else{return -1*num;}
}

int actions(vector<string> & words){
	vector<letter*> letters;

	for(int k = 0; k < words.at(0).length(); k++){
		if(letters.size() == 0 || letters.back()->c != words.at(0).at(k)){
			letter * l = new letter;
			l->c = words.at(0).at(k);
			l->occurances.push_back(1);
			letters.push_back(l);
		}
		else{
			letters.back()->occurances.back()++;
		}
	}

	for(int i = 1; i < words.size(); i++){
		int curL = -1;

		for(int j = 0; j < words.at(i).length(); j++){
			if(j == 0 || letters.at(curL)->c != words.at(i).at(j)){
				curL++;
				letters.at(curL)->occurances.push_back(1);
			}
			else{letters.at(curL)->occurances.back()++;}
		}
	}

	int numAction = 0;

	for(int z = 0; z < letters.size(); z++){
		sort(letters.at(z)->occurances.begin(), letters.at(z)->occurances.end());
		
		int median = letters.at(z)->occurances.at( words.size()/2 );

		for(int f = 0; f < words.size(); f++){
			numAction += ( abV( median - letters.at(z)->occurances.at(f) ) );
		}
	}

	return numAction;
}

int main(int argc, char* argv[]){
	ifstream data(argv[1]);
	if(!data){cerr << "Couldn't open file." << endl; return -1;}

	ofstream output("problemA.out");

	int cases;
	data >> cases;

	for(int c = 1; c <= cases; c++){
		int n;
		data >> n;

		vector<string> wordsM;
		for(int a = 0; a <= n-1; a++){
			string t;
			data >> t;
			wordsM.push_back(t);
		}
		
		if(!possible(wordsM)){output << "Case #" << c << ": Fegla Won" << endl;}
		else{
			output << "Case #" << c << ": " << actions(wordsM) << endl;
		}
	}
	
	data.close();
	output.close();
}
