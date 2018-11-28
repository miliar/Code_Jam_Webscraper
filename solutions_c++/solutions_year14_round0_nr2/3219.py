#include <iostream>
#include <cstdio>

using namespace std;

int main(){
	//freopen("in_jam.txt","r",stdin);
	//freopen("out_jam1.txt","w",stdout);
	int T;
	float C,F,X;
	cin >> T;
	for(int i = 0;i < T;i++){
		cin >> C >> F >> X;
		float F_temp = 2,Time_taken = 0;
		while(((C/F_temp) + (X/(F_temp + F))) < (X/F_temp)){
			Time_taken += C/F_temp;
			F_temp += F;
		}
		Time_taken += X/F_temp;
		printf("Case #%d: %.7lf\n",i + 1,Time_taken);
	}
	return 0;
}
