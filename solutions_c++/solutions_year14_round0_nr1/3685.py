// http://github.com/lvv
#include <scc/cj.h>	       
//#include <scc/tuple_hash.h>	       
#include <lvv/lvv.h>



int main() {
	int cases(in);  NL;
	FOR(case_, 1, cases+1)  {

		// INPUT 

		int x;
		int n1(in);  sint R1;
		for(int r=1;  r<=4;  ++r)  {
			for(int c=1;  c<=4;  ++c)  {
				cin >> x; 
				if (n1==r)   R1.insert(x);
			}
		}

		int n2(in);  sint R2;

		for(int r=1;  r<=4;  ++r)  {
			for(int c=1;  c<=4;  ++c)  {
				cin >> x; 
				if (n2==r)   R2.insert(x);
			}
		}



		/////  RESULT
		vint RES; 
		set_intersection(+R1, -R1,  +R2,  -R2,  back_inserter(RES));
			      
		_  "Case #",  case_, ": "; 
		if (RES.size()==1)   		__ RES.front();
		else if (RES.size() > 1) 	__ "Bad magician!";
		else /*if (RES.size() < 1)*/ 	__ "Volunteer cheated!";
	}                                                                        
}                                                                                
