// http://github.com/lvv
#include <scc/cj.h>	       
//#include <scc/tuple_hash.h>	       
#include <lvv/lvv.h>


int main() {
	int cases(in);  NL;
	FOR(case_, 1, cases+1)  {

		// INPUT 

		int a(in);
		unsigned n(in);
		vint V = in(n);
		vint S(n,0); // add steps

		V | sort;
					//PR2(a,n)
					//PR(V);


		///////////////


		// only add op
		int S_sum = 0;
		for(int i=0;  i<V.size();  ++i) {
			int b = V[i];

			if (a==1) {  S[i] = V.size()+99;   break; }

			while (!(a>b)) {
				a += a-1;
				++S[i];
			}

			a += b;
		}

		// how many we can cut from the tail 
		for(int i=V.size()-1;  i>=0;  --i) {
			if (S_sum + S[i] < (V.size()-i)) 	S_sum += S[i];
			else					S_sum  = V.size()-i;
		}




			//if (xx < V.size()-i) 	x+=xx;
			//else                   	{ x+=V.size()-i;  goto finish; }  




		/////  RESULT
			      
		__  "Case #",  case_, ": ", S_sum; 
			      
	}                                                                        
}                                                                                
