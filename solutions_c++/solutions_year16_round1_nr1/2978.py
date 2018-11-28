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
	ifstream ifs("A-large (8).in");
    ofstream ofs("answer_A_large");
	int T;
	ifs >> T; cout << "T= " << T <<endl;
   
   for(int t=0;t<T;t++){  // test cases
	string S;
    ifs >> S; cout << "S= " << S << endl; 

	string cand1,cand2;

	string ans="";
	for(int i=0;i<int(S.size());i++){
         cand1=S.substr(i,1)+ans;
		 cand2=ans+S.substr(i,1);

		 if(cand1<cand2){ans=cand2;}
		 else{ans=cand1;}
	}

	cout << "Case #" <<t+1<<": "<<ans <<endl;
    ofs << "Case #" <<t+1<<": " <<ans <<endl;

   } // end of test cases

 return 0;
}