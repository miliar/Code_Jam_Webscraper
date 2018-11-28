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
#include<list>
#include<bitset>
#include<algorithm>
#include<cassert>
#include<ctime>
#include<queue>
#include <iostream>
#include <fstream>
#include <Windows.h>

const double Pi = acos(-1.0);

#define li long int 

using namespace std;

const std::string inputPath = "C:\\Users\\Rayee\\Dropbox\\Google Code Jam\\2014\\Round1b 2014\\B New Lottery Game\\B-small-attempt0.in";
const std::string outPath = "C:\\Users\\Rayee\\Dropbox\\Google Code Jam\\2014\\Round1b 2014\\B New Lottery Game\\B-small-attempt0.out";

//Globals



/************************************************************************/
/* solves the case
*/
/************************************************************************/

int solveCase(ifstream& myfile){
	int A,B,K;
	myfile >> A;
	myfile >> B;
	myfile >> K;

	long long int res=0;

	long long int num;
	for (int i=0; i<A ;++i){
		for (int j=0 ; j<B ; ++j){
			num=i&j;
			if (num<K){
				res++;
			}
		}
	}
	return res;
}

/*
Main
*/

int main() {

	int numCases, caseNum = 1;
	
	ifstream myfile(inputPath.c_str());
	ofstream resFile(outPath.c_str());

	//first line : number of cases
	myfile >> numCases;

	//vars for that question
	long long int  res;

	//read all cases
	for (int i = 1; i <= numCases; ++i){
				
		res=solveCase(myfile);

		resFile << "Case #" << i << ": " <<res<< endl;

		//zero globals if needed
		


	}//end for

	myfile.close();
	resFile.close();

	return 0;

}


