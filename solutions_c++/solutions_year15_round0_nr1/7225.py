#include <stdio.h>
#include <string>
#include <iostream>
#include <sstream>

using namespace std;
int fungsi();
int main(void) {
    /* number of test cases */
    unsigned short int t;
	int hasil[110];
    cin >> t;
    for(int i=0; i < t; i++) { //loops for each case
		hasil[i] = fungsi();
    }
	for(int c = 0 ; c < t ; c++){
		cout << "Case #"  << c+1 << ": " << hasil[c] << endl;
	}
    return 0;
}
int fungsi(){
	string input;
	int max_s;
	int tepuk_tangan=0,kekurangan = 0;
	cin >> max_s;
	cin >> input;

	int number[1010];
	for(int i = 0 ; i<=max_s ; i++){
		number[i] = std::stoi(input.substr(i,1));
	}
	if(max_s == 0){
		return 0;
	}else{
		tepuk_tangan = number[0];
		for(int i = 1 ; i <= max_s ;i++){
			//if(number[i]>0){
				if((tepuk_tangan - i) >=0){
					tepuk_tangan += number[i];
				}else{
					kekurangan += (i - tepuk_tangan);
					tepuk_tangan += number[i] + (i - tepuk_tangan);
				}
			//}
		}
		return kekurangan;
	}

}