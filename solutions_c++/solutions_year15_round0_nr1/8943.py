// http://github.com/lvv
#include <scc/cj.h>	       
//#include <scc/tuple_hash.h>	       
//#include <lvv/lvv.h>



int main() {
	int cases(in);  NL;
	FOR1(test_case, cases)  {

		// INPUT 

		int       sh_max = in;
		string    D      = in;

				       //__ D;
				       //assert((unsigned)sh_max == D.size()-1);
		
		int sh_lvl = 0; 
		int ppl = 0;
		int friends = 0;
		for (char d : D) { 
			int n = d - '0';

		       	ppl += n;
			if (sh_lvl > sh_max)   		break;
			if (sh_lvl+1 > ppl + friends)	++friends; 

					//__ '-',  n, ppl, friends;
			++sh_lvl; 
		};


		__  "Case #",  test_case,  ": ",   + friends; 
	}                                                                        
}                                                                                
