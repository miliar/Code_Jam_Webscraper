#include<iostream>
#include<cstdio>
using namespace std;

typedef double D;
typedef long long ll;

int main(){
	int T;
	D c, f, x;
	scanf("%d", &T);
	for(int i = 1; i <= T; i++){
		scanf("%lf %lf %lf", &c, &f, &x);
		printf("Case #%d: ", i);
		D previousRate = 2.0;
		D previousT = x / previousRate;
		D newT, newRate;
		D bufferT = 0.0;
		bool ans;

		do{
			ans  = 0; 
			newRate = previousRate + f;
			bufferT += c / previousRate;
			newT = bufferT + (x / newRate);
			if(newT < previousT){
				previousRate = newRate;
				previousT = newT;
				ans = 1;
			}
		}
		while(ans);
		printf("%0.7lf\n",previousT);
	}
	return 0;
}