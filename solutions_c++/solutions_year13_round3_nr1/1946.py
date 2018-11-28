// http://github.com/lvv
#include <scc/cj.h>	       
//#include <scc/tuple_hash.h>	       
#include <lvv/lvv.h>


int main() {
	int cases(in);  NL;
	FOR(case_, 1, cases+1)  {

		// INPUT 

		string S;   cin >> S;
		unsigned n(in);

		///////////////
		//int L=S.size();
		int M=S.size()-n+1;

                dint V(M, 0);
		string W("aeiou"); 

		int last=0;
		iALL(V) {   
			V[i] = last + (find_first_of(+S+i, +S+i+n,  +W, -W) == +S+i+n);
			last = V[i];
		}
					//PR3(S,n,V)
		0 >> V;

		long sum=0;
		for(int i=1;  i<M+1; ++i)   {
			for (int j=i;  j<M+1;  ++j) {
				if(V[i-1]<V[j])  ++sum;
			}
		}


		/////  RESULT
			      
		__  "Case #",  case_, ": ", sum; 
			      
	}                                                                        
}                                                                                
