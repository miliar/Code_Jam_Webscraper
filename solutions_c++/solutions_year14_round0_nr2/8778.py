/**********************
 * Viktor Kvaternjak
 * Google Code Jam 2014
 ***********************/
 

#include <iostream>
#include <iomanip>

using namespace std;
void solve(int test_case){
	long double c, f, x, total_cps, best_time = 1E10, t_before = 0, with_factory, without_factory;
	cin >> c >> f >> x;
	
	t_before = 0;
	total_cps = 2.0;
	
	for (int i = 0; i < 110000; ++i){
		without_factory = t_before + x/total_cps;	
		with_factory = t_before + c/total_cps + x/(total_cps + f);
		//cout << " Bez : "<< without_factory << " Sa : " <<with_factory <<endl;
		if (best_time > with_factory) {
			best_time = with_factory;
			t_before += c/total_cps;
			total_cps += f;
		}
		if (best_time > without_factory){
			best_time = without_factory;
			break;
		}
	}
	// TODO trick if required quantity lower than cost of factory
	if (x < c) best_time = x/2.0;
	cout << "Case #"<< test_case <<": "<< setprecision(15)<< best_time;
	cout << endl;
}

int main(void){
	int n;
	cin >> n;
	for (int i = 0; i < n; i++){
		solve(i+1);
	}
	return 0;
}
