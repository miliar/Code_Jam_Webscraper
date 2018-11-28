#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool myfunction (int i,int j) { return (i>j); }

int FindSmalestMinite(vector<int>);

int main(int argc, char*argv[]){

	fstream fcin(argv[1], fstream::in);
	fstream fcout(argv[2], fstream::out);


	int totalCase;
	fcin >> totalCase;
	
	for(int caseIdx=1; caseIdx <= totalCase; caseIdx++){
		int nonEmptyPlate;
		fcin >> nonEmptyPlate;
		//fcout << nonEmptyPlate <<endl;

		// save the plate count on dinerlist
		vector<int> dinerList;
		for(int plateIdx=0; plateIdx < nonEmptyPlate; plateIdx ++){
			int plateCnt;
			fcin >> plateCnt;
		//	fcout << plateCnt<< " ";
			dinerList.push_back(plateCnt);
		}
		//fcout <<endl;
		sort(dinerList.begin(), dinerList.end(), myfunction);	

		int smallestMinite = 0;

		smallestMinite = FindSmalestMinite( dinerList );


		fcout << "Case #" << caseIdx << ": " << smallestMinite <<endl;
		cout << "Case #" << caseIdx << ": " << smallestMinite <<endl;

	}


	return 0;
}


int FindSmalestMinite( vector<int> dinerList){
	if( dinerList[0] <= 2 ){
		return dinerList[0];
	}
	else if(dinerList.size() == 0){
		return 0;
	}
	else{
		int small_a =0;
		// recude 1
		vector<int> subdinerList;
		for(int i=0; i < dinerList.size(); i++){
			if(dinerList[i] > 1){
				subdinerList.push_back(dinerList[i] -1);
			}
		}
		small_a = FindSmalestMinite( subdinerList )+1;

		int small_b;
		// divide max item
		subdinerList.clear();
		for(int i=1; i< dinerList.size(); i++){
			subdinerList.push_back(dinerList[i]);
		}
		
		int pushed_a = dinerList[0] / 2;
		int pushed_b = dinerList[0] - pushed_a;

		subdinerList.push_back( pushed_a );
		subdinerList.push_back( pushed_b );
		sort( subdinerList.begin(), subdinerList.end(), myfunction);	
		small_b = FindSmalestMinite( subdinerList )+1;
		
		if(dinerList[0] == 9){
			// divide max item
			subdinerList.clear();
			for(int i=1; i< dinerList.size(); i++){
				subdinerList.push_back(dinerList[i]);
			}
		
			pushed_a = dinerList[0] / 3;
			pushed_b = dinerList[0] - pushed_a;

			subdinerList.push_back( pushed_a );
			subdinerList.push_back( pushed_b );
			sort( subdinerList.begin(), subdinerList.end(), myfunction);	
			int small_c = FindSmalestMinite( subdinerList )+1;

			if(small_c < small_b){
				small_b = small_c;
			}
		}
/*
		for(int pushed_a = 1; pushed_a <= (dinerList[0] / 2); pushed_a++){
			int pushed_b = dinerList[0] - pushed_a;

			subdinerList.clear();
			for(int i=1; i< dinerList.size(); i++){
				subdinerList.push_back(dinerList[i]);
			}
			
			subdinerList.push_back( pushed_a );
			subdinerList.push_back( pushed_b );
			sort( subdinerList.begin(), subdinerList.end(), myfunction);	
			int tmp = FindSmalestMinite( subdinerList )+1;
			if( tmp < small_b ){
				small_b = tmp;
			}
		}
*/

		if( small_a < small_b){
			return (small_a);
		}
		else{
			return (small_b);
		}
	}
}

