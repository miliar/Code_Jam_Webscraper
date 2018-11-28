// http://github.com/lvv
#include <scc/cj.h>	       
//#include <scc/tuple_hash.h>	       
#include <lvv/lvv.h>



int main() {
	int cases(in);  NL;
	FOR(case_, 1, cases+1)  {

		// INPUT 

		double C(in), F(in),  X(in);
							//PR4(case_, C, F, X);
		double f=2;


		double no_buy_s = 0;
		double c_buy_s  = 0;
		double buy_s    = 0;

		while(1) {
			no_buy_s = X/f;
			buy_s    = C/f +  X/(f+F); 

							//PR2(no_buy_s, buy_s);

			if (buy_s  >  no_buy_s)  break;

			c_buy_s += C/f;
			f       += F;
							//PR2(c_buy_s, f);
		}
			
		double time = c_buy_s + no_buy_s;



		/////  RESULT
		cout.precision(8);
		__  "Case #",  case_, ": ", time; 
	}                                                                        
}                                                                                
