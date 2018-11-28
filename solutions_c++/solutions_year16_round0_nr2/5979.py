#include <iostream>
#include <sstream>
#include <string>
#include <math.h>
#include <string.h>

#define mp(a, b) make_pair(a, b)
typedef long long ll;
using namespace std;



int main(){
	int  in;
	char inc[10000];
	int st,end;
	int num;
	char reverse;
	int revnum;
	cin >> num;
	int s[100];//0:- 1:+

	for (int i = 0; i < num; i++){//++- +--
		
		cin >> inc;
		//init
		for (int j = 0; j < 100; j++){
			s[j] = 0;
		}
		
		st = 0;
		end = strlen(inc);
		reverse = inc[0];//+ or -

		
		revnum = 0;
		for (int j = 0; j < strlen(inc); j++){
			if (inc[j] != reverse){
				revnum++;
				if (reverse == '+'){
					reverse = '-';
				}
				else{
					reverse = '+';
				}
			}
		}
		if (reverse == '-'){
			revnum++;
		}
		cout << "Case #" << i + 1 << ": " << revnum << endl;

	}


	return 0;
}