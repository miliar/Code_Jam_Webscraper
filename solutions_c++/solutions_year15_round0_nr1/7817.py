#include <iostream>
#include <stdlib.h>

using namespace std;

int main(){
	int T,s_max,stand;
	string str_s;
	int invite;
	cin >> T;
	for(int i = 1; i <= T ; ++i){
		cin >> s_max >> str_s;
		stand = str_s[0]-48;
		invite = 0;
		
		for(int j = 1 ; j < s_max+1 ; ++j){
			if((str_s[j]-48) != 0){
				if(stand > j){
					stand += (str_s[j]-48);
				}else{
					invite += abs(stand - j);					
					stand += abs(stand - j);
					stand += (str_s[j]-48);
				}
			}
			//cout << invite << " " << stand << endl;
		}
		cout << "Case #" << i << ": " << invite << endl;
	}
	return 0;
}
