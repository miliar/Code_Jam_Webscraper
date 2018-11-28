#include <iomanip>
# include <iostream>
# include <vector>
using namespace std;

double min(double a, double b){
	if (a < b) return a;
	return b;
}
//cout.precision(10);
int main(){
	int T;
	cin >> T;
	for(int u = 0; u < T; u++){
		double C,F,X;
		cin >> C >> F >> X;
		if (X > C){
			int k = 0;
			double t = 2;
			while((X-C)/(t) > X/(t+F)){ k++; t += F;}

			double total_time = 0;
			for (int q = 0; q < k; q++) total_time += C/(2+q*F);
			total_time += (X)/(2+k*F);
			
			/*double total_time_1 = 0;
			for (int q = 0; q < k-1; q++) total_time_1 += C/(2+q*F);
			total_time_1 += (X)/(2+(k-1)*F);
			
			double total_time_2 = 0;
			for (int q = 0; q < k+1; q++) total_time_2 += C/(2+q*F);
			total_time_2 += (X)/(2+(k+1)*F);
			total_time = min(total_time_1, min(total_time,total_time_2));*/
			cout << "Case #" << u+1 <<": " << setprecision(10) << total_time << /*"..." << total_time_1 << "..." << total_time_2 << */ endl;
		}
		else cout << "Case #" << u+1 <<": " << setprecision(10) << X/2 << endl;
	}
}
