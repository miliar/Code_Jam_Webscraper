#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;
string analyze(int r10, int r11, int r12, int r13, int r20, int r21, int r22, int r23, int casenum);
int main()
{
	int firstrow, secondrow;
	int arr1[4][4];
	int arr2[4][4];
	string answer;

	int cases;
	ofstream output;
	output.open("answers.txt");
	ifstream stream;
	stream.open("input.txt");
	stream >> cases;
	for (int n = 0; n < cases; n++)
	{
		stream >> firstrow;
		for (int i = 0; i < 4; i++)
		{
			stream >> arr1[i][0] >> arr1[i][1] >> arr1[i][2] >> arr1[i][3];
		}
		stream >> secondrow;

		for (int i = 0; i < 4; i++)
		{
			stream >> arr2[i][0] >> arr2[i][1] >> arr2[i][2] >> arr2[i][3];
		}
		firstrow--;
		secondrow--;
		answer = analyze(arr1[firstrow][0], arr1[firstrow][1], arr1[firstrow][2], arr1[firstrow][3], arr2[secondrow][0], arr2[secondrow][1], arr2[secondrow][2], arr2[secondrow][3], n);
		//output answer
		output << answer << endl;
	}
}

string analyze(int r10, int r11, int r12, int r13, int r20, int r21, int r22, int r23, int casenum)
{
	int answers[2];
	answers[0] = 0;
	if ((r10 == r20) || (r10 == r21) || (r10 == r22) || (r10 == r23))
	{
		answers[0]++;
		answers[1] = r10;
	}
	if ((r11 == r20) || (r11 == r21) || (r11 == r22) || (r11 == r23))
	{
		answers[0]++;
		answers[1] = r11;
	}
	if ((r12 == r20) || (r12 == r21) || (r12 == r22) || (r12 == r23))
	{
		answers[0]++;
		answers[1] = r12;
	}
	if ((r13 == r20) || (r13 == r21) || (r13 == r22) || (r13 == r23))
	{
		answers[0]++;
		answers[1] = r13;
	}

	//convert to string
	string possibilities[2];
	possibilities[0] = "Bad magician!";
	possibilities[1] = "Volunteer cheated!";
	string final;
	stringstream sstream;
	if (answers[0] == 1)
	{
		sstream << "Case #" << casenum+1 << ": " << answers[1];
		final = sstream.str();
	}


	if (answers[0] == 0)
	{
		sstream << "Case #" << casenum+1 << ": " << possibilities[1];
		final = sstream.str();
	}
	//final = "Case #" + casenum +": " + possibilities[1];
	if (answers[0] > 1)
	{
		sstream << "Case #" << casenum+1 << ": " << possibilities[0];
		final = sstream.str();
	}
	sstream.str("");
	//final = "Case #" + casenum +": " + possibilities[0];
	return final;
}

