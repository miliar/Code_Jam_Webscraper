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
	int here[200];
	int bridge[200];

	for (int i = 0; i<= 199; i++){
		here[i] = 0;bridge[i] = 0;
	}

	int i,j,k,l,m,n,x,y,z,worst;
	string temp;

		getline (infile, temp,'\n');	
		AN(temp);
		int SS = I[1];
		int LINES = I[2];

		int min = 0;
		int max = 100;

		long long realrev = 0;

		for (i = 1; i<= LINES; i++)
		{
			getline (infile, temp,'\n');	
			AN(temp);
			int dist = I[2] - I[1];
			realrev += findrev(SS,dist) * I[3];
			
			for (j = I[1] ; j<= I[2]; j++)
			{
				here[j]+= I[3];
			}
			for (j = I[1]+1 ; j<= I[2]; j++)
			{
				bridge[j]+= I[3];
			}
		}

		int cheat = 0;

		for (i = 1; i<= SS; i++)
		{
			while (here[i] > 0)
			{
				here[i]--;
				int advance = 0;
				j = i+1;
				while ( here[j] >= 1 && bridge[j] > 0)
				{
					here[j]--;
					bridge[j] --;
					advance++;
					j++;
				}
				int dist = j-i-1;
				cheat += findrev(SS,dist);
			}

		
		}
		worst = realrev-cheat;
	
	worst = worst % 1000002013;

	cout << "Case #" << t << ": " << worst;
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
