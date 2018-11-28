#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <cfloat>
#include <cstdint> 

using namespace std;

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define REP1(i,n) for((i)=1;(i)<=(int)(n);(i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)

#define INF 1.0E+15

ifstream infile;

string S[101];
long long I[201];
double D[101];



#define M_LOG2E 1.44269504088896340736 //log2(e)

inline long double log2(const long double x){
    return  log(x) * M_LOG2E;
}

void binary(long long int number) {
	long long int remainder;

	if(number <= 1) {
		cout << number;
		return;
	}

	remainder = number%2;
	binary(number / 2);    
	cout << remainder;
}

void AN(string s){
	unsigned pos;
	int last = -1;
	for (int i = 1; i<= 200; i++)
	{
		 pos = s.find(" ",last+1);
		 if (pos == std::string::npos)
		 {
			 I[i] = _atoi64(s.substr(last+1).c_str());
			 return;
		 }
		 I[i] = _atoi64(s.substr(last+1,pos-last-1).c_str());
		 last = pos;
	}
	return;
}

void AS(string s){
	unsigned pos;
	int last = -1;
	for (int i = 1; i<= 100; i++)
	{
		 pos = s.find(" ",last+1);
		 if (pos == std::string::npos)
		 {
			 S[i] = s.substr(last+1);
			 return;
		 }
		 S[i] = s.substr(last+1,pos-last-1);
		 last = pos;
	}
	return;
}

void AD(string s){
	unsigned pos;
	int last = -1;
	for (int i = 1; i<= 100; i++)
	{
		 pos = s.find(" ",last+1);
		 if (pos == std::string::npos)
		 {
			 D[i] = atof(s.substr(last+1).c_str());
			 return;
		 }
		 D[i] = atof(s.substr(last+1,pos-last-1).c_str());
		 last = pos;
	}
	return;
}


long long findloss (long long players, long long prizes)
{
	if (players == 1 && prizes == 1)
		return 1;

	if (2*prizes <= players)
		return 1;
	else
		return 2*findloss(players/2,prizes-players/2)+1;
}

long long findwins (long long players, long long prizes)
{
	if (players == 1 && prizes == 1)
		return 1;
	if (2*prizes >= players)
		return 1;
	else
		return 2*findwins(players/2,prizes)+1;

}

void main2(int t)
{

	long long h,l,i,j,k,m,n,y,z,worst;
	string temp;

	getline (infile, temp,'\n');	
	AN(temp);

	long long x = pow(2,I[1]);


	l = findloss(x,I[2])-1;

	h= x - findwins(x,I[2])-1;
	//h = findloss(x,x - I[2])-1;

	if (x == I[2])
	{	l = x-1;
	h = x-1;}

	cout << "Case #" << t << ": " << l << " " << h;
	cout << endl;



}



int main(void){
	int T, t;
	string temp;
	infile.open("new  3.txt");
	getline (infile, temp);
	T = atoi(temp.c_str());
	for (int t = 1; t<= T; t++)
		main2(t);
	return(0);
}
