//#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_WARNINGS
//#include <cstdio>
//#include <cstdlib>
//#include <cmath>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <list>
#include <queue>
#include <set>
using namespace std;

int main(void){

	int T, N;
	// char ;
	
	cin >> T;
	
	int i;
	for(i = 1;i<=T;i++){
		cin >> N;
		if(N == 0) cout << "Case #"<< i << ": " << "INSOMNIA" <<endl;
		else{
			long long int result;
			bool check[20] = { false };
			int checknum = 0;
			long long int buff;
			for(int j = 1;checknum != 55; j++){
				buff = j * N;
				result = buff;
				do{
					int buff2 = buff % 10;
					if(check[buff2] == false){
						check[buff2] = true;
						checknum += (buff2 + 1);
					}
					
					buff /= 10;
				}while(buff != 0);
			}
			
			cout << "Case #"<< i << ": " << result <<endl;
		}
	}

	return 0;
}


