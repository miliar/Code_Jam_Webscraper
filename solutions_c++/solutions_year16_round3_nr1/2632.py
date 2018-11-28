#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <stdlib.h>
using namespace std;

typedef long long ll;

#define STOP {cin.sync();cin.get();}
#define f0(i, n) for(int i=0; i<(int)(n);i++)
#define f1(i, n) for(int i=1; i<=(int)(n);i++)
#define all(itr, a) for(auto itr = a.begin(); itr != a.end(); itr++)

ifstream fin("A-large.in");
ofstream fout("output.txt");

char AL[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
int N;
int sum;

int comp(const pair<int, char> &x, const pair<int, char> &y){
	pair<int, char> a = x;
	pair<int, char> b = y;

	return	b.first - a.first;
}

//key = 0:"AA", 1:"AB", 2:"A"
bool C(pair<int, char> P[], int key){
	int a = 0, b = 0, c = 0;

	if (key == 0){
		a = 2;
		c = 2;
	}
	else if (key == 1){
		a = 1;
		b = 1;
		c = 2;
	}
	else{
		a = 1;
		c = 1;
	}

	return max(max(P[0].first - a, P[1].first - b), P[2].first) <= ((sum - c) / 2);
}

void solve(int num){
	fin >> N;

	pair<int, char> P[26];

	f0(i, N){
		int temp;
		fin >> temp;
		P[i] = make_pair(temp, AL[i]);
	}

	char ans[2001] = "\0";
	char space = ' ';

	sum = 0;
	f0(i, N)	sum += P[i].first;
	
	while (sum > 0){
		qsort(P, N, sizeof(pair<int, char>), (int(*)(const void*, const void*))comp);

		if (P[0].first >= 2 && C(P, 0)){
			strncat_s(ans, &P[0].second, 1);
			strncat_s(ans, &P[0].second, 1); 
			P[0].first -= 2;
			sum -= 2; 
		}
		else if (sum != 3 && P[0].first >= 1 && P[1].first >= 1 && C(P, 1)){
			strncat_s(ans, &P[0].second, 1);
			strncat_s(ans, &P[1].second, 1);
			P[0].first -= 1;
			P[1].first -= 1;
			sum -= 2;
		}
		else if(P[0].first >= 1 && (P, 1)){
			strncat_s(ans, &P[0].second, 1);
			P[0].first -= 1;
			sum -= 1;
		}
		strncat_s(ans, &space, 1);
	}

	fout << "Case #" << num << ": " << ans << endl;
}

int main(){
	int T;
	fin >> T;

	f1(num, T){
		solve(num);
	}

	//STOP;

	return 0;
}