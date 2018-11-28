#include <iostream>
#include <string>
#include <vector>
using namespace std;


int max(int a, int b){
	return a>b?a:b;
}

int toInt(char c){
	return c - '0';
}


int main(){
	int T;
    cin >> T;
    for(int i = 1; i<= T; i++){
		int smax;
		string str;
		cin >> smax; 
		cin >> str;
		int res = 0, sum = toInt(str[0]);
		for (int j=1; j<smax+1; j++){
			if (toInt(str[j]!=0)  && res + sum < j)
				res = j - sum;
			sum += toInt(str[j]);
		}
		
		cout << "Case #" << i << ": " << res << endl;

	}

}
