/*
Google Code Jam
Qualification Round
4-11-14
Name: Robert Gonzalez
email: rob.d.gonz@gmail.com
Problem: B. Cookie Clicker Alpha
*/

#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <sstream>
#include <iomanip>

using namespace std;

vector<string> result;

double findFastestTime(double C, double F, double X, int caseNum);
void print_to_file();

int main(){

	int numTestCases=0;
	int testCaseNum = 1;

	ifstream input;
	input.open("input_large.txt");
	string buff;

	if(input.is_open()){
		input >> buff;
		numTestCases = atoi(buff.c_str());
		while(numTestCases > 0){

			input >> buff;
			double C = atof(buff.c_str());		//Cost of new farm

			input >> buff;
			double F = atof(buff.c_str());		//Additional cookies per second

			input >> buff;
			double X = atof(buff.c_str());		//Cookies to win

			findFastestTime(C, F, X, testCaseNum);

			testCaseNum++;
			numTestCases--;
		}
	}
	input.close();

	// print Result
	print_to_file();
	return 0;
}


 double findFastestTime(double C, double F, double X, int caseNum){
	 double rate = 0.0;
	double curr_cps = 2.0;  //Current cookies per second earned
	double total_time = 0.0;
	
	while(true){

		//Find time to win at current rate
		double t_cur = X / (curr_cps);

		//Find time to win if we buy one more farm
		double t_buy = (C / curr_cps) + (X / (curr_cps + F));

		//if time to win at current is higher then buying then your done
		if((total_time + t_cur) <= (total_time + t_buy)){
			total_time += t_cur;
			ostringstream tmp;
			tmp << "Case #" << caseNum << ": " << setprecision(7) << fixed << total_time;
			result.push_back(tmp.str());
			cout << total_time << endl;
			break;
		}
		else{
			total_time += (C / (curr_cps));
			curr_cps += F;
		}
	}

	 return 1;

 }


 void print_to_file(){

	ofstream output;
	output.open("result_large.txt");

	if(output.is_open()){
		for(int i = 0; i < result.size(); i++){
			output << result[i] << endl;
			cout << result[i] << endl;
		}
	}
	else
		cout << "ERROR: could not print result" << endl;


	output.close();


 }