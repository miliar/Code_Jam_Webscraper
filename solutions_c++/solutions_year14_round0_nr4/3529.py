// http://github.com/lvv
#include <scc/cj.h>	       
//#include <scc/tuple_hash.h>	       
#include <lvv/lvv.h>



int main() {
	int cases(in);  NL;
	FOR(case_, 1, cases+1)  {

		// INPUT 

		int       N (in); 
		ddouble   O  = in(N);     
		ddouble   K0 = in(N);  K0  | sort;
		ddouble   K;

		//  WAR

                int  war_wins=0; 
		K = K0;
		O  | sort | reverse;       
		

		for (double o : O) { 
			auto ki = find_if(+K, -K, [=](double k){return  k > o;});
			if (ki == -K)   ki = +K;
			war_wins += o > *ki ? 1 : 0;
			K - ki;
		};


		// DWAR
	       
                int  dwar_wins = 0; 
		K = K0;
		O  | sort;       


		for(auto o: O) {
			if (o < ++K) {
				continue;
			} else {
				++dwar_wins;
				--K;
			}
			
		}

		__  "Case #",  case_,  ": ",  dwar_wins,  war_wins; 
	}                                                                        
}                                                                                
