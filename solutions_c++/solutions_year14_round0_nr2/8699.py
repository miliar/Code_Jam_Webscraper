#include<iostream>
#include<fstream>
#include <iomanip>
using namespace std;
int main(){
	int i,num;
	long double C, F, X,X_time,C_time,split_time,total_time;
	bool isRun;
	ifstream fin("B-large.in");
	ofstream fout("Output2.txt");
	fin >> num;
	for (i = 0; i < num; i++){
		isRun = false;
		split_time = 2;
		total_time = 0;
		fin >> C;
		fin >> F;
		fin >> X;
		X_time = X / split_time;
		C_time = (C / split_time) + (X / (F + split_time));
		while (X_time>C_time){
			isRun = true;
			total_time += C/ split_time;
			split_time += F;
			X_time = X / split_time;
			C_time = (C / split_time) + (X / (F + split_time));
		}
		if (isRun)
			total_time += X_time = X / split_time;
		else
			total_time = X / split_time;
		fout << "Case #" << i + 1 << ": " <<fixed<<setprecision(10)<<total_time << endl;
	}
	system("pause");
	return 0;
}