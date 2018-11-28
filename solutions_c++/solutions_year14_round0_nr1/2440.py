#include<cstdio>
#include<iostream>
#include<iomanip>
#include<cmath>
#include<cstring>
#include<cstdlib>
#include<string>
#include<sstream>
#include<vector>
#include<map>
#include<set>
#include<bitset>
#include<algorithm>
#include<cassert>
#include<ctime>
#include<queue>
#include <iostream>
#include <fstream>
#include <Windows.h>

const double Pi = acos(-1.0);

using namespace std;

const std::string inputPath = "C:\\Users\\Rayee\\Dropbox\\Google Code Jam\\qualification round 2014\\A Magic Trick\\A-small-attempt0.in";
const std::string outPath = "C:\\Users\\Rayee\\Dropbox\\Google Code Jam\\qualification round 2014\\A Magic Trick\\A-small-attempt0.out";

//Globals
int firstArr[4];
int secondArr[4];


bool firstArrContains(int num){
	for(int i=0 ; i<4 ;++i){
		if (firstArr[i]==num){
			return true;
		}
	}

	return false;
}


/************************************************************************/
/* solves the case
*/
/************************************************************************/
//res 1 - 16 are actual results
//17 is Bad magician! (more than 1 in the second row)
//18 is Volunteer cheated! (no matches)
void solveCase (int& res){
	int num, repeates=0, tmpRes;
	for(int i=0 ; i<4 ;++i){
		num=secondArr[i];
		if (firstArrContains(num)){
			repeates++;
			tmpRes=num;
		}
	}

	//cal the result
	if (repeates==1){
		res=tmpRes;
	}
	else if(repeates>1)	{
		res=17;
	}
	else if(repeates==0){
		res=18;
	}

	return;	
}

/*
Main
*/

int main() {

	int numCases, caseNum = 1,result=1;

	ifstream myfile(inputPath.c_str());
	ofstream resFile(outPath.c_str());
	
	//first line : number of cases
	myfile >> numCases;
	
	//vars for that question
	int firstRow, secondRow, num;

	//read all cases
	for (int i = 1; i <= numCases; ++i){
		
		myfile >>firstRow;
		firstRow--;

		//fill the case data: the first sekected row
		for (int k=0; k<4; ++k) {
			for (int j=0 ; j<4 ; ++j){
				 myfile >>num;
				 if(firstRow==k){
					 firstArr[j]=num;
				 }
			 }
		}

		myfile >>secondRow;
		secondRow--;

		//gets the second row
		for (int k=0; k<4; ++k) {
			for (int j=0 ; j<4 ; ++j){
				 myfile >>num;
				 if(secondRow==k){
					 secondArr[j]=num;
				 }
			 }
		}

		solveCase(result);
		//res 1 - 16 are actual results
		//17 is Bad magician! (more than 1 in the second row)
		//18 is Volunteer cheated! (no matches)
		if (result<=16){
			resFile << "Case #" << i << ": " << result << endl;
		}
		else if (result==17){
			resFile << "Case #" << i << ": Bad magician!" << endl;
		}
		else if (result==18){
			resFile << "Case #" << i << ": Volunteer cheated!" << endl;
		}

		
		//zero globals if needed

	}//end for

	myfile.close();
	resFile.close();

	return 0;

}

