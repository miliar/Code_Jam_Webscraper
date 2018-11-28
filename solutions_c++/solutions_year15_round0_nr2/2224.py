#include<cstdio>
#include<iostream>
#include<string>
#include<cmath>
#include<vector>
#include<algorithm>

#define REP(i,N) for(int (i) = 0; (i)<(N); (i)++)
using namespace std;

int solve(vector<int>plates){
	sort(plates.rbegin(),plates.rend());
	int minimum = 10000;
	for(int a= 1; a<= minimum;a++){
		int akt = a;
		REP(b,plates.size()){
			if(plates[b] > a){
				if(plates[b] %a == 0) akt--;
				akt += plates[b]/a;
			}
		}
		if(akt<minimum) minimum = akt;
	}
	return minimum;
}



int main()
{
	int test;
	scanf("%i",&test);
	REP(a,test){
		int d;
		scanf("%i",&d);
		vector<int>plates;
		int pr;
		REP(b,d){
			scanf("%i",&pr);
			plates.push_back(pr);
		}
		int min = solve(plates);
		printf("Case #%i: %i\n",a+1,min);
	}


	return 0;
}
