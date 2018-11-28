#include <iostream>
#include <string>
using namespace std;


int main(){
	int cases;
	char letter;
	string word;
	int letterval;
	int currLetter;
	string input;

	cin>>cases;

	for(int i=0;  i<cases ;i++){
		cin>>input;
		//cout<<input;
		letterval = (int)input[0];
		currLetter = letterval;
		word = "";
		for(int j=0; j<input.size(); j++){
			letter = input[j];
			letterval = (int)letter;
			if(letterval<currLetter)
				word = word + letter;
			else 
				word = letter + word;
			currLetter = (int)word[0];
			}
			cout<<"Case #"<<i+1<<": "<<word<<endl;
	}	 
	return 0;
}