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
int I[201];
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
	for (int i = 1; i<= 200; i++)
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


void main2(int t)
{

	string temp;
	getline (infile, temp);
	AN(temp);

	int i;
	int X = I[1];

	double N[11];
	double K[11];
	getline (infile, temp);
	AD(temp);
	for (i = 1; i<= 10; i++)
		N[i] = D[i];

	std::sort (N+1, N +X+1);

	getline (infile, temp);
	AD(temp);
	for (i = 1; i<= 10; i++)
		K[i] = D[i];

	std::sort (K+1, K +X+1);

	int cheat = 0;
	int ken = 0;

	int Nloc = X;

	for (i = X; i>=1, Nloc >=1; i--)
	{
		if (K[i] > N[Nloc])
		{
			ken++;
			Nloc--;
		}
		else
		{
			i++;
			Nloc--;
		}



		//if (N[X-i+1] > K[i])
		//	cheat++;
		//else
		//	break;
	}
	Nloc = X;
	for (i = X; i>=1, Nloc >=1; i--)
	{
		if (N[i] > K[Nloc])
		{
			cheat++;
			Nloc--;
		}
		else
		{
			i++;
			Nloc--;
		}



		//if (N[X-i+1] > K[i])
		//	cheat++;
		//else
		//	break;
	}

		cout << "Case #" << t << ": " << cheat << " " << X-ken;
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
