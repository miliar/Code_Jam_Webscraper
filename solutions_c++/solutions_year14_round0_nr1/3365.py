
#include <math.h>
#include <iostream>
#include <vector>
#include <set>
#include <fstream>
#include <string>
#include <algorithm>
#include <iterator>

using namespace std;

const int kBadMagician = -1;
const int kVolunteerCheated = -2;

struct InputData 
{
	int row;
	int m[4][4];
};

int solve(const InputData& first, const InputData& second)
{
	std::set<int> s1, s2;
	
	for(int i = 0; i < 4; ++i)	
	{
		s1.insert(first.m[i][first.row-1]);
		s2.insert(second.m[i][second.row-1]);
	}

	std::vector<int> intersect;
	set_intersection(s1.begin(),s1.end(),s2.begin(),s2.end(),  std::back_inserter(intersect));

	if (intersect.size() == 1)
		return intersect[0];
	else if(intersect.size() > 1)
		return kBadMagician;
	else
		return kVolunteerCheated;
}

void InputAttempt(ifstream& inFile, InputData& data)
{
	inFile >> data.row;
	for (int y = 0; y < 4; ++y)
		for (int x = 0; x < 4; ++x)
			inFile >> data.m[x][y];
}


int main()
{
	ifstream inFile ("input.txt");

	if (!inFile.is_open())
		return 1;

	int numCases;
	inFile>>numCases;

	vector<std::pair<InputData,InputData>> inputDataVec;
	inputDataVec.resize(numCases);

	for (int i = 0; i < numCases; ++i)
	{
		InputData& first = inputDataVec[i].first;
		InputData& second = inputDataVec[i].second;
		InputAttempt(inFile, first);
		InputAttempt(inFile, second);
	}

	ofstream outFile;
	outFile.open("output.txt");

	outFile.setf( std::ios::fixed, std:: ios::floatfield );
	outFile.precision(7);

	for (int i = 0; i < numCases; ++i)
	{
		InputData& first = inputDataVec[i].first;
		InputData& second = inputDataVec[i].second;
		
		int res = solve(first, second);
		
		if (res == kBadMagician)
			outFile << "Case #" << i+1 << ": Bad magician!" << endl;
		else if(res == kVolunteerCheated)
			outFile << "Case #" << i+1 << ": Volunteer cheated!" << endl;
		else
			outFile << "Case #" << i+1 << ": " << res << endl;
	}

	outFile.close();

	return 0;
}