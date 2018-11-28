#include<cstdio>
#include<iostream>
#include<string>
#include<cmath>

#define REP(i,N) for(int (i) = 0; (i)<(N); (i)++)
using namespace std;

int mapNum(char c){
	int a = c-'0';
	return a;
}

int solve(string shy, int del){
	int jeLid = 0;
	int kam = 0;
	REP(a,del+1){
		if(jeLid < a){
			kam++;
			jeLid++;
		}
		jeLid += mapNum(shy[a]);
	}
	return kam;

}

int main()
{
	int test;
	cin>>test;
	REP(a,test){
		int del;
		cin>>del;
		string shy;
		cin>>shy;
		int kol = solve(shy,del);
		printf("Case #%i: %i\n",a+1,kol);
	}



	return 0;
}
