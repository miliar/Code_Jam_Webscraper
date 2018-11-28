#include<cstdio>
#include<cmath>
#include<iostream>
#include<string>
#include<sstream>

using namespace std;

#define MAXT 1024


int main(){
	int T;
	cin >> T;
	for(int k=0; k<T; k++){
		string cake;
		cin >> cake;
		
		cout << "Case #" << (k+1) << ": "; 

		int seg=1;
		for(int i=1; i<cake.size(); i++)
			if(cake[i]!=cake[i-1])
					seg++;
		if(cake[cake.size()-1] == '+')
			cout << (seg - 1) << "\n";
		else cout << seg << "\n";
	}
}
