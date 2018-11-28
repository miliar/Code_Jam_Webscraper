 // http://github.com/lvv
#include <scc/cj.h>	       
#include <lvv/lvv.h>
#include <scc/matrix.h>



int main() {
	int cases(in);  NL;
	FOR(case_, 1, cases+1)  {
		int M(in), N(in);
		matrix<int> X(M,N); cin >> X;
		_  "Case #",  case_, ": ";
							//__ N,M; __ X;
		vint max_row(M,0);
		vint max_col(N,0);

		jFOR(M) iFOR(N) {
			max_row[j] = std::max(max_row[j], X(i,j));
			max_col[i] = std::max(max_col[i], X(i,j));
		}

		jFOR(M) iFOR(N) {
			if (X(i,j) == max_row[j]  ||  X(i,j) == max_col[i])  continue;
			else  goto  print_no;
		}

		__ "YES";
		continue;

		print_no: __ "NO";
	}                                                                        
}                                                                                
