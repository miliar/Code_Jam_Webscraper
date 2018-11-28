#include <iostream>
#include <vector>
#include <fstream>
#include <cmath>
using namespace std;

int main()
{
	ifstream in("B-large.in");
	ofstream out("out.txt");
	int caseCount;
	vector<double> answers;
	in>>caseCount;
	
	for(int i=0;i<caseCount;i++)
	{
		double X, C, F;
		in>>C>>F>>X;
		double currentSpeed = 2.0;
		double sum = 0.0;
		double minn = X/currentSpeed, minn2;
		double bonuse = 0.0;
		do
		{
			minn2 = minn;
			bonuse = C/currentSpeed;
			currentSpeed += F;
			minn = X/currentSpeed + bonuse + sum;
			sum+=bonuse;
			bonuse = 0;	
		}while(minn < minn2);
		answers.push_back(min(minn, minn2));
	}

	for(int i=0;i<answers.size();i++)
	{
		char buf[100];
		sprintf_s (buf, "%.7lf", answers[i]);
		out<<"Case #"<<i+1<<": "<<buf<<endl;
	}
	return 0;
}