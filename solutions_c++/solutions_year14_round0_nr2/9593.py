// Problem B. Cookie Clicker Alpha 

#include <iostream>    

double TimeToCookie(double initial_rate, const double cookie_farm, const double extra_rate, const double cookie_target) {

	double 	ti(cookie_target/initial_rate), 
			tf(cookie_farm/initial_rate), new_rate(initial_rate + extra_rate), 
			tn(cookie_target/new_rate), t2(tf + tn);
	if(t2 < ti)
		return (tf + TimeToCookie(new_rate, cookie_farm, extra_rate, cookie_target));
	else
		return ti;
}

int
main ()
{
	std::ios_base::sync_with_stdio(false);

    int test_cases;
	std::cin >> test_cases;

	for (int i(0); i < test_cases; ++i) {
	
		double cookie_farm, extra_rate, cookie_target;
		std::cin >> cookie_farm >> extra_rate >> cookie_target;

		// outputting to 7 decimal places
		std::cout.precision(7);//same as std::cout << std::setprecision(7);
		std::cout << std::fixed;
		
		std::cout << "Case #" << (i+1) << ": ";
		std::cout << TimeToCookie(2, cookie_farm, extra_rate, cookie_target) << std::endl;
	}
	
	return 0;
}
