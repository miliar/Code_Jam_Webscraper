#include <string>
#include <cstdlib>
#include <vector>
#include <iostream>
#include <algorithm>
#include <iomanip>

#define INF (1 << 30)
using namespace std;
string case_text = "Case #";
double C , F , X;

double Solve(){
	int n = 0;
	double X_time_bef = INF;
	double C_time_bef = 0;
	while(1){
		double curr_vel = 2 + n * F;
		double cand_X_time = C_time_bef + X / curr_vel;
		double cand_C_time = C_time_bef + C / curr_vel;
		
		if( X_time_bef < cand_X_time ) return X_time_bef; 
		
		C_time_bef = cand_C_time;
		X_time_bef = cand_X_time;
		n++;
	}
	return -1;
}

int main(){
	int T;
	cin >> T;
	for (int test_id = 1; test_id <= T; ++test_id ){
		cin >> C >> F >> X;

		cout << case_text << test_id << ": " << setprecision(7) << fixed <<	Solve() << std::endl;
	}
	return 0;
}
