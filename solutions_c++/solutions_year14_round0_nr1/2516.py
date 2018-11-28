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
	ifstream ifs("A-small-attempt0 (5).in");
    ofstream ofs("answer");
	int T;
	ifs >> T; cout << "T= " << T <<endl;
   
   for(int t=0;t<T;t++){  // test cases
	int row1;
    ifs >> row1; cout << "row1= " << row1 << endl; 

	int M1[5][5];
	for(int i=1; i<=4;i++){
		for(int j=1; j<=4;j++){
          ifs >> M1[i][j];  //cout <<" " << M1[i][j];
		}
		//cout << endl;
	}

    int row2;
    ifs >> row2; cout << "row2= " << row2 << endl; 

	int M2[5][5];
	for(int i=1; i<=4;i++){
		for(int j=1; j<=4;j++){
          ifs >> M2[i][j];    //cout << " " << M2[i][j];
		}
		//cout <<endl;
	}

	int A[5];
	for(int i=1;i<=4;i++){
         A[i]=M1[row1][i]; //cout << " " << M1[row1][i];
	}

	//cout <<endl;

    int B[5];
	for(int i=1;i<=4;i++){
         B[i]=M2[row2][i]; //cout << " " << M2[row2][i];
	}
  //cout <<endl;

	int num=0; int W=-1;

	for(int i=1;i<=4;i++){
		for(int j=1;j<=4;j++){
			if(A[i]==B[j]){num++;W=A[i]; }
		}
	}

	cout << "Case #" <<t+1<<": ";

	if(num==0){ cout <<"Volunteer cheated!"<<endl;
	}else if( num==1){  cout << W<<endl;
	}else{   cout<< "Bad magician!"<<endl;
	}

    ofs << "Case #" <<t+1<<": ";

	if(num==0){ ofs <<"Volunteer cheated!"<<endl;
	}else if( num==1){  ofs << W<<endl;
	}else{   ofs << "Bad magician!"<<endl;
	}

   } // end of test cases

 return 0;
}