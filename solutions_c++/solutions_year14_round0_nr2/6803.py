#include <iostream>
#include <fstream>
#include <vector>
#include <array>
using namespace std;
void CookieClicker();


int main(){
	CookieClicker();

	return 0;
}

void CookieClicker(){
	fstream in;
	ofstream out;
	out.open("Text.out");
	in.open("1.txt");
	int n;
	in >> n;
	int pwrTen = 10000000;
	double c, f, x, rate;
	long double tempTime, nextTime, tmp2, rt, time;
	for (int i = 0; i < n; i++){
		rate = 2;
		in >> c;
		in >> f;
		in >> x;
		bool flag = false;
		time = 0;
		tempTime = x / rate;
		while (flag == false){
			nextTime = x / (rate + f);
			rt = c / rate;
			tmp2 = nextTime + rt;
			if (tempTime > tmp2){
				rate += f;
				time += rt;
				tempTime = nextTime;
			}
			else{
				time += tempTime;
				flag = true;
			}
		}
		time = trunc(pwrTen*time) / pwrTen;
		out.precision(15);
		out << "Case #" << i + 1 << ": " << time << endl;
	}
}
