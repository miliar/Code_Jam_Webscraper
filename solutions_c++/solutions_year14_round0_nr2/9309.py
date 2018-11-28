#include <iostream>
#include <fstream>
#include <string>


#define str std::string


int main()
{

	str input_loc;
	std::ifstream inp;
	std::ofstream otp;


	std::cin>>input_loc;

	inp.open(input_loc);
	otp.open("output.out");
	otp.precision(50);

	int case_no_m = 0; inp>>case_no_m;


	for (int case_no_c = 1; case_no_c <= case_no_m; case_no_c++){

		double c,f,x; inp>>c;inp>>f;inp>>x;
		double old_t=-1.f,next_t=-1.f,sum_t=0.f;
		int n = 0;

		next_t=(x/2);
		old_t=(next_t+1);
		while (next_t < old_t){

			old_t = next_t;
			next_t = (sum_t + c/(2+n*f) + x/(2+(n+1)*f)); 

			/**build new**/
			sum_t += (c/(2+n*f));
			n++;


		};

		otp<<"Case #"<<case_no_c<<": "<<(old_t)<<"\n";

	};
};
