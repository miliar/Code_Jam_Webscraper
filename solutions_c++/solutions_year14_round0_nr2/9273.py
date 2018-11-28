#include <iostream>
#include <fstream>

using namespace std;
double cookieRate = 2.0;
double elapsedTime = 0.0;
double currentProspectiveTime;
double nextProspectiveTime;
double goal;
double cost;
double farmRate;
 void calculate();
int main()
{

    int cases;
	ofstream output;
    output.precision(7);
    output.setf(ios::fixed);

	output.open("answers.txt");
	ifstream stream;
	stream.open("input.txt");
	stream >> cases;
	for(int casenum = 1; casenum <= cases; casenum++)
    {
        stream >> cost >> farmRate >> goal;
        calculate();
        //analyze();
        output << "Case #" << casenum << ": " << currentProspectiveTime << endl;
    }
}

void calculate()
{

     currentProspectiveTime = elapsedTime + (goal / cookieRate);
                    nextProspectiveTime = elapsedTime + (cost / cookieRate) + (goal / (cookieRate + farmRate));
                    while (currentProspectiveTime > nextProspectiveTime)
                    {
                        elapsedTime += cost / cookieRate;
                        currentProspectiveTime = nextProspectiveTime;
                        cookieRate += farmRate;
                        nextProspectiveTime = elapsedTime + (cost / cookieRate) + (goal / (cookieRate + farmRate));
                    }
 cookieRate = 2.0;
 elapsedTime = 0;
}



