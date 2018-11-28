// http://github.com/lvv
#include <scc/cj.h>	       
//#include <scc/tuple_hash.h>	       
#include <lvv/lvv.h>



int main() {
	int cases(in);  NL;
	FOR(case_, 1, cases+1)  {

		// INPUT 

		int  			N(in);
		vector<string> 		S(N);  
		vector<vector<int>> 	CNT(N, vector<int>());  
		int 			steps = 0;
		vector<int> 		AVG(100,0);  
		string	  s1, prev_s1;

		iFOR(N)   {
			char	  prev='-';
			s1.clear();

			cin >> S[i];

			for(auto c : S[i]) {
				if (c==prev)	++CNT[i].back();
				else   		{ CNT[i].push_back(1);  prev=c;  s1.push_back(c);}
			}

			//if (i  &&  CNT[i].size() != CNT[i-1].size())   {
			if (i  &&  prev_s1 != s1)  {
				goto felga;
			}

			prev_s1 = s1;


			prev_s1 = s1;

			jFOR(CNT[0].size()) 	AVG[j] += CNT[i][j];
		}

		jFOR(CNT[0].size()) 	AVG[j] = (AVG[j] + 0.5) / N;


		/*
		// find best string
		int     best_i=0;
		int    	min_steps=999999999;
		for(size_t i=0;  i<N;  ++i)   {
			int steps = 0;
			jFOR(CNT[0].size()) {
				steps += std::abs(CNT[i][j]*N - AVG[j]);
			}
			if (steps <= min_steps) {
				min_steps = steps;
				best_i = i;
			}
		}*/

		iFOR(N)   {
			jFOR(CNT[0].size()) {
				steps += std::abs(CNT[i][j] - AVG[j]);
			}
		}

		
		__  "Case #",  case_,  ": ",  steps;
		continue;
			
		felga:
		__  "Case #",  case_,  ": Fegla Won";  
									//__ N, S;

	}                                                                        
}                                                                                
