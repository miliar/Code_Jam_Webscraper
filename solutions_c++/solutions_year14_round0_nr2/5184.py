#include <iostream>
#include <string>
#include<vector>

//using std::string;
//using std::cin;
//using std::cout;
//using std::endl;

using namespace std;

double getMinTime(double C,double originalRate,double X,double time,double F)
{
	//cout << "Time = " << time <<endl;	
	//cout << "Cost1 = " << C/originalRate + X/(originalRate + F)<< endl;
	//cout << "Cost2 = " << X/originalRate << endl; 
	if( (C/originalRate) + X/(originalRate + F) < (X/originalRate) )
	{
		
		time = time + (C/originalRate); 
		originalRate = originalRate + F;
		
	}
	else
	{
		//cout << "Entered else" << endl;
		time = time + X/originalRate;
		return time;
	}
	getMinTime(C,originalRate,X,time,F);





}



int main()
{
 
 int T;
	
 cin >> T;
 std::vector<string> output;
 string str;
 for(int i = 0; i < T; i++)
 {

 	double cookiesToGet, costOfFarm, rate;
 	cin >> costOfFarm >> rate >> cookiesToGet; 
 	double minTime = getMinTime(costOfFarm, 2, cookiesToGet,0,rate);
	str = "Case #" + to_string(i+1) + ": " + to_string(minTime);
	output.push_back(str);	
 	//cout << "Time required is " << minTime << endl;
}

for (std::vector<string>::iterator it = output.begin(); it != output.end(); ++it)
	{
		cout << (*it) << "\n";
		

	}
}
