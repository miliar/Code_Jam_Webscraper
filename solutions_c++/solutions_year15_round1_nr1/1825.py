#include<cstdio>
#include<iostream>
#include<string>
#include<cmath>
#include<vector>
#include<algorithm>

#define REP(i,N) for(int (i) = 0; (i)<(N); (i)++)
using namespace std;

int solve1(vector<int>pocty){
	int mini = 0;
	for(int a = 0; a<pocty.size()-1; a++){
		if(pocty[a] > pocty[a+1])
			mini += pocty[a] - pocty[a+1];
	}
	return mini;
}
int solve2(vector<int>pocty){
	int maxi = -1;
	int mini = 0;
	for(int a = 0; a<pocty.size()-1; a++){
		if(pocty[a] - pocty[a+1]> maxi)
			maxi = pocty[a] - pocty[a+1];
	}
	for(int a = 0; a<pocty.size()-1; a++){
		if(pocty[a] >= maxi)
			mini += maxi;
		else
			mini+= pocty[a];
	}

	return mini;
}



int main()
{
	int test;
	scanf("%i",&test);
	REP(a,test){
		int d;
		scanf("%i",&d);
		vector<int>poct;
		int pr;
		REP(b,d){
			scanf("%i",&pr);
			poct.push_back(pr);
		}
		int min1 = solve1(poct);
		int min2 = solve2(poct);
		printf("Case #%i: %i %i\n",a+1,min1, min2);
	}


	return 0;
}
