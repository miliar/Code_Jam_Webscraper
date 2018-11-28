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
	ifstream ifs("A-small-attempt1 (4).in");
    ofstream ofs("answer");
	int T;
	ifs >> T; cout << "T= " << T <<endl;
   
   for(int t=0;t<T;t++){  // test cases
	int N;
    ifs >> N; cout << "N= " << N << endl; 

	vector<string> S;
	for(int i=0;i<N;i++){
        string dummy;
		ifs>>dummy;
		S.push_back(dummy); cout<<dummy<<endl;
	}

	string base="";

	string str,save;
	str=S[0];
    save=S[0].substr(0,1);
	base+=S[0].substr(0,1);
	for(int j=1;j<int(str.size());j++){
		if(str.substr(j,1)!=save){save=str.substr(j,1); base+=save;   }
	}

	cout<<"base=" <<base<<endl;

	int impossible=0;

	int minimum=0;
	

	for(int i=1;i<N;i++){
      
    save=S[i].substr(0,1);
	string check="";
	check+=S[i].substr(0,1);
	for(int j=1;j<int(S[i].size());j++){
		if(S[i].substr(j,1)!=save){save=S[i].substr(j,1); check+=save;   }
	}

	if(check!=base){impossible=1; break;}

	}

	if(impossible!=1){
	  int C[101][101];

	  for(int i=0;i<N;i++){
		  for(int j=0;j<int(base.size());j++){
               C[i][j]=0;
		  }
	  }

	 

	  for(int i=0;i<N;i++){
		  int j=0;
		  for(int k=0;k<int(S[i].size());k++){
			  if(S[i].substr(k,1)==base.substr(j,1)){C[i][j]++;}
			  else{j++; C[i][j]++;}
		  }//k-loop
	  }

/*	  for(int i=0;i<N;i++){
		  for(int j=0;j<int(base.size());j++){
            cout << " " <<C[i][j];
		  }
		  cout<<endl;
	  }*/


	  for(int j=0;j<int(base.size());j++){
		  int M_min=101;
		  for(int m=0;m<=100;m++){int sum=0;
		  for(int i=0;i<N;i++){
             sum+=abs(C[i][j]-m);
		   }//i-loop
		  if(sum<M_min){M_min=sum;}
		  }//m-loop
		  minimum+=M_min;
	  }//j-loop
	}

	cout << "Case #" <<t+1<<": " ;
	if(impossible==1){cout<<"Fegla Won"<<endl;}
	else{cout<<minimum<<endl;}

    ofs << "Case #" <<t+1<<": " ;
	if(impossible==1){ofs<<"Fegla Won"<<endl;}
	else{ofs<<minimum<<endl;}
    

   } // end of test cases

 return 0;
}