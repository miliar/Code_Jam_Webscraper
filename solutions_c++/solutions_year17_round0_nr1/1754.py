#include <iostream>
#include <string>
using namespace std;

int T;
int S;
string cake;

string getAnswer(string cake, int S){
	int len = cake.length();
	int i = 0;
	int count = 0;
	for ( ; i + S - 1 < len; i++){
		if ( cake[i] == '-' ){
			count++;
			for(int j = 0; j < S; j++ ){
				if ( cake[i+j] == '-')
					cake[i+j] = '+';
		 		else
					cake[i+j] = '-'; 		
			}
		}
	}
	string res = "IMPOSSIBLE";
	bool flag = true;
	for (; i < len; i++){
		if ( cake[i] == '-' ){
			flag = false;
			break;
		}
	}
	if ( flag == true )
		res = to_string(count);
	return res;
}


int main( ){
	
	cin >> T;
	for(int i =1; i<= T; i++){
		cin >> cake >> S;
		cout << "Case #" << i << ": " <<  getAnswer(cake, S) << "\n";
	}
	

	return 0;
}

