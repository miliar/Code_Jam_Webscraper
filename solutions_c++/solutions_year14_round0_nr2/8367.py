#include<iostream>
#include<string>
#include<sstream>
#include<fstream>
#include<vector>
#include <iomanip>

using namespace std;



double caseProcess(double c, double f, double x)
{
	double result = 0;
	double r_cur = 2;
	double r_next = 0;

	if(x<=c)
		result = x/r_cur;
	else
	{
		result += c/r_cur;
		r_next = r_cur + f;
		while((x-c)/r_cur > x/r_next)
		{
			r_cur = r_next;
			result += c/r_cur;
			r_next = r_cur + f;
		}

		result += (x-c)/r_cur;
	}



	return result;
}

void main()
{
	string filename = "input.in";
	unsigned int numCases = 0;


	fstream fin(filename.c_str(), ios::in);
	string templine;

	//get the number of test cases
	getline(fin, templine);
	numCases = atoi(templine.c_str());

	fstream fout("result.out", ios::out);

	double c, f, x;

	for(unsigned int caseInd=1; caseInd<=numCases; caseInd++)
	{
		double caseResult;
		string tempNum;

		//read current case
		getline(fin, templine);
		stringstream ss;
		ss << templine;
		ss >> tempNum;
		c = atof(tempNum.c_str());
		ss >> tempNum;
		f = atof(tempNum.c_str());
		ss >> tempNum;
		x = atof(tempNum.c_str());

		//processing
		caseResult = caseProcess(c, f, x);

		//write the result of current case into the output file
		fout<<"Case #"<<caseInd<<": "<<std::fixed<<setprecision(7)<<caseResult<<endl;
		//cout<<"Case #"<<caseInd<<": "<<std::fixed<<setprecision(7)<<caseResult<<endl;
	}

	fin.close();
	fout.close();

}
