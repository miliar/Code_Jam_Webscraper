#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

int main (){
	
	int N, Smax, S, Friend;
	string Pshyness;
	
	
	cin >> N;
	for (int i =0; i < N; i++){
		S = 0;
		Friend = 0;
		cin >> Smax;
		cin >> Pshyness;
		for (int j = 0; j <= Smax; j++){
			if (S < j)
				if (Friend < j-S) 
					Friend = j - S;
			S += ((int)(Pshyness[j]-'0'));
		}
		cout << "Case #" << (i + 1) << ": " << Friend <<  '\n';
	}
	return 0;			
}

