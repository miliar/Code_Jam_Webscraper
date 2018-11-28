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

const std::string inputPath = "C:\\Users\\Rayee\\Dropbox\\Google Code Jam\\2014\\Round1b 2014\\A The Repeater\\A-small-attempt0.in";
const std::string outPath = "C:\\Users\\Rayee\\Dropbox\\Google Code Jam\\2014\\Round1b 2014\\A The Repeater\\A-small-attempt0.out";

//Globals



pair<char,int> readString(string str, int pos){
	pair<char,int> resPair;
	int res=1;
	char curChar=str[pos];
	pos++;
	while (str[pos]==curChar){
		res++;
		pos++;
	}

	resPair.first=str[pos];
	resPair.second=res;
	return resPair;

}


/************************************************************************/
/* solves the case
*/
/************************************************************************/

int solveCase(ifstream& myfile){
	int N;
	myfile >> N;

	string strA,strB;
	myfile >> strA;
	myfile >> strB;
	int res=0;

	char ch1=' ', ch2=' ';
	bool toFinish=false;
	int posA=0, posB=0;
	
	while (!toFinish){
		if (ch1 !=ch2){
			return -1;
		}

		 pair <char,int> res1=readString(strA,posA); 
		 posA+=res1.second;
		 ch1= res1.first;

		 pair <char,int> res2=readString(strB,posB); 
		 posB+=res2.second;
		 ch2= res2.first;

		 res+=abs(res1.second- res2.second);

		 if (ch1 == '\0'){
			 if (ch2 != '\0'){
				return -1;
			 }
			 toFinish=true;
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
		if (res==-1){
			resFile << "Case #" << i << ": Fegla Won"<< endl;
		}
		else{
			resFile << "Case #" << i << ": " <<res<< endl;
		}
		

		//zero globals if needed
		


	}//end for

	myfile.close();
	resFile.close();

	return 0;

}


