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
int I[1001];
double D[101];

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
	for (int i = 1; i<= 2000; i++)
	{
		 pos = s.find(" ",last+1);
		 if (pos == std::string::npos)
		 {
			 I[i] = atoi(s.substr(last+1).c_str());
			 return;
		 }
		 I[i] = atoi(s.substr(last+1,pos-last-1).c_str());
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
int findrev (int SS, int dist)
{
	int totalcost = 0;
	for (int i = 1; i<= dist; i++)
	{
		totalcost+= SS +1 - i;
	}
	return(totalcost);
}

	double a_even[1000][1000];
	double a_odd[1000][1000];

void heart()
{
	int l;
	int X = 1000;


	int k,p;
	
	int N = X;



	for (k = 0; k < N; k++)
	{
		for (l = 0; l < N; l++)
		{
			if (k==l)
				a_even[k][l] = 1;
			else
				a_even[k][l] = 0;
		}
	}
	// for each time
	for (int q = 0; q < N; q++){
		// for each place to switch to
		for (k = 0; k< N; k++)
		{
			// for each number
			for (l = 0; l < N; l++)
			{
				a_odd[l][k] = a_even[l][k] * (N-1)/N + a_even[l][q]/N;
			}
			// for 0 row 

		}
			for (l = 0; l < N; l++)
			{
				a_odd[l][q] = 1.0/N;
			}
		// swap

		for (k = 0; k< N; k++)
		{
			// for each number
			for (l = 0; l < N; l++)
			{
				a_even[l][k] = a_odd[l][k];
			}

		}
	
	}

}


void main2(int t)
{
	int N, k;
	int l;
	string temp2;
	getline (infile, temp2);
	AN(temp2);

	int X = I[1];
	N = X;
	getline (infile, temp2);
	AN(temp2);


	// find prob
	double prob = 1.0;

		for (k = 0; k< N; k++)
		{
			prob = prob * a_even[I[k+1]][k]*N;
		}
		if (prob > 1)
		{
				cout << "Case #" << t << ": " << "BAD" ;
				cout << endl;
		}
		else
		{
				cout << "Case #" << t << ": " << "GOOD" ;
				cout << endl;
		}





}



int main(void){

	heart();
	int T, t;
	string temp;
	for (int qqqq = 0; qqqq < 20 ; qqqq++)
{	
	infile.open("inputhere2.txt");
	getline (infile, temp);
	T = atoi(temp.c_str());
	for (int t = 1; t<= T; t++)
		main2(t);
	
	infile.close();
	}

	return(0);

}
