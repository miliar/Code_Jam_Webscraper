#include <iostream>
#include <fstream>
using namespace std;
struct input{
	double C;
	double F;
	double X;
};
void process(){
	ifstream file("B-large.in");
	int input_number;
	input *input1;
	file >> input_number;
	input1 = new input[input_number];
	for (int i = 0; i < input_number; i++){
		file >> input1[i].C >> input1[i].F >> input1[i].X;
	}
	file.close();
	ofstream fileout("B-large.out");
	fileout.precision(12);
	for (int i = 0; i < input_number; i++){
		double time=0;
		double cookie;
		double rate = 2;
		double timecok;
		double time_switch;
		while (true){
			timecok = input1[i].C / rate;
			if (input1[i].X/rate<=(timecok+input1[i].X/(rate+input1[i].F))){
				time += input1[i].X / rate;
				break;
			}
			time += timecok;
			rate += input1[i].F;
		}
		fileout << "Case #" << i + 1 << ": " << time;
		if (i != (input_number - 1))
			fileout << "\n";
	}
	fileout.close();
}
int main(){
	process();
	return 0;
}