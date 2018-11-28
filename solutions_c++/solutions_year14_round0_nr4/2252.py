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

const std::string inputPath = "C:\\Users\\rayee\\Dropbox\\Google Code Jam\\qualification round 2014\\D Deceitful War\\D-small-attempt0.in";
const std::string outPath = "C:\\Users\\rayee\\Dropbox\\Google Code Jam\\qualification round 2014\\D Deceitful War\\D-small-attempt0.out";

//Globals
list<double> gNaomiNums;
list<double> gKenNums;

//Func: ken chooses his best number: eitehr bigger then naomi if he has (but as samll as possible)
//or the smallest he has
double getKenNum(list<double>& kenNums, double chosenNaomi){
	double res;
	
	//search for a num that is bigger
	for (std::list<double>::iterator it = kenNums.begin(); it != kenNums.end(); ++it){
		if (*it > chosenNaomi){
			res= *it;
			kenNums.erase(it);
			return res;
		}
	}

	//if didnt fint just return the samllest
	res = kenNums.front();
	kenNums.pop_front();
	return res;
}//end ken choice fun


//Func: getToldNaomi(kenNums)
//she wil tell that the number is big, but samller then ken's max
//or she may tell the truth if she is about to win
double getToldNaomi(const list<double>& kenNums, double chosenNaomi){


	double kenSmallest = kenNums.front();
	double kenBiggest = kenNums.back();
	double res;
	//if she is gonna win
	if (chosenNaomi > kenSmallest){
		res = kenBiggest+0.0000001;
	}
	else{ //she is gonna lose, just tell the turth
		res = chosenNaomi;
	}
	return res;
}

//Func
//Namoi should choose smart
//it is possible for her to win if she has something that is bigger then the smallest of Ken.
//she wil choose it. (bigger, but as small as possible)
//if not, she will just choose her smallest num
//remove it from here nums
double getChoiceNaomi(list<double>& naomiNums, const list<double>& kenNums){
	double kenSmallest = kenNums.front();
	double res;
	for (std::list<double>::iterator it = naomiNums.begin(); it != naomiNums.end(); ++it){
		if (*it > kenSmallest){
			res = *it;
			naomiNums.erase(it);
			return res;
		}
	}

	//if reached her, naomi doesnt have anything that is bigger then the smallest of ken
	res = naomiNums.front();
	naomiNums.pop_front();
	return res;

}

//Func: playDeceitfulWar 
int playDeceitfulWar(){
	int naomiRes = 0;

	list<double> naomiNums = gNaomiNums;
	list<double> kenNums = gKenNums;

	//i assume here the lists are sorted
	//so perhaps i can remove this
	//naomiNums.sort();
	//kenNums.sort();

	double chosenNaomi, toldNaomi, chosenKen;
	while (naomiNums.size()>0){
		
		//Namoi should choose smart
		//it is possible for her to win if she has something that is bigger then the smallest of Ken.
		//she wil choose it. (bigger, but as small as possible)
		//if not, she will just choose her smallest num
		//remove it from here nums
		chosenNaomi = getChoiceNaomi(naomiNums, kenNums);
		
		//she will tell it is very big, to make ken play his big nums first
		//or she may tell the truth if she is about to win
		toldNaomi = getToldNaomi(kenNums, chosenNaomi);

		//now ken will choose something bigger (if he has), but samllest as possible anywas
		//the fun will remove his chosen num
		chosenKen = getKenNum(kenNums, toldNaomi);

		if (chosenNaomi > chosenKen){
			naomiRes++;
		}
	}

	return naomiRes;
}


//Func to play real war. returns naomi result
int playRealWar(){
	int naomiRes = 0;

	list<double> naomiNums = gNaomiNums;
	list<double> kenNums = gKenNums;

	//i assume here the lists are sorted
	//so perhaps i can remove this
	//naomiNums.sort();
	//kenNums.sort();

	double chosenNaomi, chosenKen;
	while (naomiNums.size()>0){
		//naomi will just choose a block (doesnt matter for strategy of Ken)
		//i go for the largest
		chosenNaomi = naomiNums.back();
		//remove it from here nums
		naomiNums.pop_back();

		//now ken will choose something bigger (if he has), but samllest as possible anywas
		chosenKen = getKenNum(kenNums, chosenNaomi);

		if (chosenNaomi > chosenKen){
			naomiRes++;
		}
	}
	
	return naomiRes;
}

/************************************************************************/
/* solves the case
*/
/************************************************************************/

pair<int,int> solveCase(){

	int resRealWar = playRealWar();
	int resDeceitfulWar = playDeceitfulWar();
	return make_pair(resRealWar, resDeceitfulWar);
}

/*
Main
*/

int main() {

	int numCases, caseNum = 1;
	pair<int,int> result;
	
	ifstream myfile(inputPath.c_str());
	ofstream resFile(outPath.c_str());

	//first line : number of cases
	myfile >> numCases;

	//vars for that question
	int N;
	double num;

	//read all cases
	for (int i = 1; i <= numCases; ++i){

		myfile >> N;
		for (int j = 0; j < N; ++j){
			myfile >> num;
			gNaomiNums.push_back(num);
		}
		for (int j = 0; j < N; ++j){
			myfile >> num;
			gKenNums.push_back(num);
		}

		//sorting the lists is good here
		gNaomiNums.sort();
		gKenNums.sort();

		result = solveCase();

		resFile << "Case #" << i << ": " << result.second << " " << result.first<< endl;

		//zero globals if needed
		gNaomiNums.clear();
		gKenNums.clear();


	}//end for

	myfile.close();
	resFile.close();

	return 0;

}


