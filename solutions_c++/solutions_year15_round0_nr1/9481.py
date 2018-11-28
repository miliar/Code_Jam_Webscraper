#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

class solver{
	vector<string> lines;
	string result;
	int count;
public:
	solver(){
		count = 1;
	}

	void AddInput(string line){
		lines.push_back(line);
		count--;
	}

	bool NeedMoreInput(){
		return count > 0;
	}

	void Process(){
		//result = lines[0];

		string current = lines[0];

		std::stringstream stream(current);
		size_t highestShyness;
		stream >> highestShyness;		
		size_t begin = to_string(highestShyness).size() + 1;

		size_t sumOfStandingPeople = 0;
		size_t currentShynessLevel = 0;
		size_t numOfFriendsNeeded = 0;

		for (string::iterator i = current.begin() + begin; i != current.end(); ++i)
		{
			char c = *i;
			int numberOfPeopleOnThisShynessLevel = atoi(&c);
			
			if (numberOfPeopleOnThisShynessLevel != 0 && (sumOfStandingPeople + numOfFriendsNeeded < currentShynessLevel)){
				numOfFriendsNeeded += (currentShynessLevel - (sumOfStandingPeople + numOfFriendsNeeded));
			}

			sumOfStandingPeople += numberOfPeopleOnThisShynessLevel;
			currentShynessLevel++;
		}

		result = to_string(numOfFriendsNeeded);
	}

	string GetResults(){
		return result;
	}
};

class InOut{
	bool print2Console;
public:
	InOut(bool b) :print2Console(b){}

	void Read(string& inputFileName, vector<solver>& s){

		string line;
		ifstream inputFile(inputFileName);
		s.push_back(solver());

		if (inputFile.is_open()){
			getline(inputFile, line);
			int numberOfTestCases = atoi(line.c_str());

			while (getline(inputFile, line) && numberOfTestCases){
				s.back().AddInput(line);

				if (s.back().NeedMoreInput() == false){
					numberOfTestCases--;

					if (numberOfTestCases > 0)
						s.push_back(solver());
				}
			}

			inputFile.close();
		}
		else{
			cout << "Unable to open input file!" << endl;
		}
	}

	void Write(string& outputFileName, vector<solver>& s){

		ofstream outputFile(outputFileName);
		if (outputFile.is_open())
		{
			for (size_t i = 0; i < s.size(); i++)
			{
				outputFile << "Case #" << i + 1 << ": ";
				outputFile << s[i].GetResults();
				
				if(i < s.size() - 1)
					outputFile << "\n";

				if (print2Console){
					cout << "Case #" << i + 1 << ": ";
					cout << s[i].GetResults();
					cout << "\n";
				}
			}

			outputFile.close();
		}
		else{
			cout << "Unable to open output file!" << endl;
		}
	}
};

int main(){
	vector<solver> solvers;
	InOut inOut(true);

	string in = "A-large.in";
	string out = "A-large.out";

	inOut.Read(in, solvers);

	for (vector<solver>::iterator i = solvers.begin(); i != solvers.end(); ++i){
		i->Process();
	}

	inOut.Write(out, solvers);

	int read;
	cin >> read;
	return 0;
}