#include <iostream>
#include <iomanip>

struct state {
	int n_farms;
	double farm_cost, farm_rate, target;
	
	double insertion_time; // we have 0 cookies after purchasing  new farm
	double rate;
};

double calc_ttc(const state &s)
{
	return s.insertion_time + s.target/s.rate;
}

double add_farm(state &s)
{
	s.insertion_time += s.farm_cost/s.rate;
	s.rate += s.farm_rate;
	return calc_ttc(s);
}

int main()
{
	using namespace std;

	int n_cases;
	
	cin >> n_cases;
	for (int case_no=1; case_no<=n_cases; ++case_no) {
		state s;
		
		cin >> s.farm_cost >> s.farm_rate >> s.target;
		s.n_farms = 0;
		s.insertion_time = 0.0;
		s.rate = 2.0;
		
		double ttc = calc_ttc(s);
		double new_ttc = add_farm(s);
		while (new_ttc < ttc) {
			ttc = new_ttc;
			new_ttc = add_farm(s);
		}
		
		cout << "Case #" << case_no << ": " << fixed << setprecision(7) << ttc << endl;
	}
}

