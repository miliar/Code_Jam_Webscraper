#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;

int main(){
	ofstream fout("s1.out", ofstream::out);
	int T;
	double c, f, x;
	
	cin >> T;
	double *p = new double[T];
	for (int i = 0; i < T; i++){
		double time = 0, grow = 2, ctime = 0,ptime=0;
	
		cin >> c >> f >> x;
		time = x / grow;
		while (1){
			ptime = ptime + c / grow;
			ctime = time;
			time = ptime + x / (grow + f);
			if (ctime < time){
				break;
			}
			grow += f;

		}
		p[i] = ctime;
	}
	for (int i = 0; i < T; i++){
		fout << "Case #" << i + 1 << ": "<<fixed<<setprecision(7) << p[i]<<endl;
	}
	return 0;
}