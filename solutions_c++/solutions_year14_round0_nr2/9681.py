#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <math.h>
#include <iomanip>
using namespace std;

void setNum(string s, double &x, double &y, double &z){
	int l = s.length();
	string s1 = "";
	int count = 0;
	for (int i = 0; i < l; i++){
		if (s[i] != ' '){
			s1 = s1 + s[i];
		}else if(s[i] == ' '){
			count++;
			if (count == 1){
				//cout<<s1<<endl;
				istringstream(s1) >> x;
				s1 = "";
			}else if (count == 2){
				//cout<<s1<<endl;
				istringstream(s1) >> y;
				s1 = "";
			}
		}
		if (i == l -1){
			//cout<<s1<<endl;
			istringstream(s1) >> z;
			s1 = "";
		}
	}
	 
}

void process(double &time, double c, double f, double x, double per){
	if (x/per > (c/per + x/(f+per))){
		cout<<"per is "<<per<<endl;
		cout<<"time is "<<time;
		time = time + c/per;
		cout<<" + "<<c/per<<" = "<<time<<endl;
		per = per + f;
		process(time, c, f, x, per);
	}else{
		cout<<"las per is "<<per + f<<endl;
		cout<<"time is "<<time;
		time = time + x/per;
		cout<<" + "<<c/per<<" = "<<time<<endl;
		return;
	}
}

double getResult(string line){
	double r = 0.0000000;
	double c = 0.0;
	double f = 0.0;
	double x = 0.0;
	double per = 2.00000;
	setNum(line, c, f, x);
	//outFile<<fixed<<setprecision(2)<<a<<endl<<b<<endl;
	//cout<<"xyz "/*<<fixed<<setprecision(7)*/<<c<<" "<<f<<" "<<x<<endl;
	if (x <= c){
		r = x/per;
		return r;
	}
	process(r, c, f, x, per);

	return r;
}

int main()
{
    std::ifstream infile("B-small-attempt0.in");
	//std::ifstream infile("2.txt");
    std::string line;
    string num;
    std::getline(infile, num);
    int nums = atoi(num.c_str());
    ofstream outfile;
    outfile.open("output.txt");
    int counter = 0;
	while (std::getline(infile, line)){
		double output = getResult(line);
		counter++;
		cout<<"Case #"<<counter<<": "<<fixed<<setprecision(7)<<output<<endl;
		outfile<<"Case #"<<counter<<": "<<fixed<<setprecision(7)<<output<<endl;
	}
	
    system("pause");
   // return 0;
}