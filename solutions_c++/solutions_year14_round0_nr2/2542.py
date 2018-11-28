#include <fstream>
#include <sstream>
#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <algorithm>
#include <iomanip>
#include <map>
#include <set>
#include <queue>

using namespace std;

int main()
{
	ifstream ifs("B-large (3).in");
    ofstream ofs("answer");
	int T;
	ifs >> T; cout << "T= " << T <<endl;
   
   for(int t=0;t<T;t++){  // test cases
	double C;
	ifs >>C;  cout << fixed <<setprecision(7) <<C<<endl;

	double F;
	ifs >>F; cout <<F<<endl;

	double X;
	ifs >>X; cout <<X<<endl;

	double time=0.0;
	double a=2.0;

	double tl,t1,t2;

	for(;;){
     tl=C/a;
	 time+=tl;
	 t1=(X-C)/a;
	 t2=X/(a+F);
	 if(t1<t2){time+=t1; break;}
	 else{a=a+F;}
	}

	cout << "Case #" <<t+1<<": " <<time <<endl;
    ofs << "Case #" <<t+1<<": " <<fixed << setprecision(7) <<time <<endl;

   } // end of test cases

 return 0;
}