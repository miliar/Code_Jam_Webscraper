#include <iostream>
#include <stdlib.h>
#include <algorithm>

using namespace std;

int map[4][4] = {1, 2, 3, 4, 2, -1, 4, -3, 3, -4, -1, 2, 4, 3, -2, -1};

bool containsDijkstra(int *s, int L, int X, int *suffix){
	int i,j,k;
	int resA = 1;
	int sign;
	for(i = 0 ; i < L*X - 1 ; i++){
		if(resA > 0)
			sign = 1;
		else
			sign = -1;
		resA = sign * map[abs(resA)-1][s[i%L]];
		//cout<<resA;
		if(resA != 2)
			continue;
		int resB = 1;
		for(j = i+1 ; j < L*X -1 ; j++){
			if(resB > 0)
				sign = 1;
			else
				sign = -1;
			resB = sign * map[abs(resB)-1][s[j%L]];
			//cout<<resB;
			if(resB == 3 && suffix[j+1] == 4)
				return true;
		}
	}
	return false;	
}

int main(){
	int i,j,k;
	int X, L;
	int T;
	string str;
	int *s;
	int *suffix;

	cin>>T;
	for(i = 0 ; i < T ; i++){
		cin>>L>>X;
		s = new int[L];
		suffix = new int[L*X];
		cin>>str;
		for(j = 0 ; j < L ; j++){
			s[j] = str[j] - 'i' + 1;
		}
		cout<<"Case #"<<i+1<<": ";
		if(L*X < 3){
			cout<<"NO\n";
			continue;
		}

		suffix[L*X - 1] = s[(L*X - 1)%L]+1;
		suffix[L*X - 2] = map[s[(L*X - 2)%L]][s[(L*X - 1)%L]];
		int signAB;
		int signC;
		for(j = L*X - 3 ; j>=0 ; j--){
			suffix[j] = map[s[j%L]][s[(j+1)%L]];
			signAB = -1;
			if(suffix[j] > 0)
				signAB = 1;

			signC = 1;
			if(suffix[j+2] < 0)
				signC = -1;

			suffix[j] = signAB * signC * map[abs(suffix[j]) - 1 ][abs(suffix[j+2]) - 1];
		}
		
		/*for(j = 0 ; j < L*X ; j++)
			cout<<suffix[j]<<"\t";
		cout<<"\n";*/
		if(containsDijkstra(s, L, X, suffix))
			cout<<"YES\n";
		else
			cout<<"NO\n";
		delete s;
	}
	return 0;
}