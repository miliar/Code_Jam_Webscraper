#include <iostream>
#include <cstdio>
#include <math.h>
#include <vector>
#include <stdlib.h>     /* abs */
#include <string.h>
#include <unordered_map>
#include <list>
#include <algorithm>
#include <sstream>
using namespace std;

vector<string> createWords(vector<string> liste,string letter){
	vector<string> result;

	for(int i=0;i<liste.size();i++){
		string temp;
		temp.append(liste.at(i));

		temp.append(letter);
		result.push_back(temp);
		temp="";
		temp.append(liste.at(i));
		temp = letter + temp;
		result.push_back(temp);

	}
	return result;
}


int main() {

	FILE *fileInput = freopen("A-small-attempt0.in","r",stdin);
	FILE *fileOutput = freopen("A-small-attempt0.out","w",stdout);

	std::vector<char> listDigits;
	std::vector<char>::iterator it;

		string N;
		int k=2;
		int numberOfEntries;
		cin >> numberOfEntries; // there are numberOfEntries +1 ligne inside the text
		string S;
		for(int i=1;i<=numberOfEntries;i++ ){
			cout << "Case #" << i << ": ";
			cin >> S;
			vector<string> letters;
			for(int i=0;i<S.size();i++){
				std::stringstream ss;
				string str;
				ss << S.at(i);
				ss >> str;
				letters.push_back(str);
			}

			vector<string> solutions;
			solutions.clear();
			solutions.push_back(letters.at(0));
			vector<string> tempSolutions;
			for(int i=1;i<letters.size();i++){

				tempSolutions = createWords(solutions,letters.at(i));
				solutions.clear();
				solutions=tempSolutions;
				tempSolutions.clear();

			}

			vector<string> testS,testSC;
			testSC.push_back("C");
			testS.push_back("A");
			//testS.push_back("B");

			vector<string> listeSolution = createWords(testSC,testS.at(0));

			   sort(solutions.begin(),solutions.end());

			  // for(int i=0;i<solutions.size();i++){
				//   cout << "solutions item : " << solutions.at(i) << endl;

			   //}

			   cout << solutions.at(solutions.size()-1) <<endl;

		}
	std::fclose(stdout);
	return 0;
}
