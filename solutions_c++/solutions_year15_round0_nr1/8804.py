#include <iostream>
#include <stdio.h>

using namespace std;


int main(){
	std::ios::sync_with_stdio(false);
	int test, smax;
	int currpos, answer;
	int currval, protect;
	string sarray;

	cin >> test;

	for(int i=0; i<test; i++){
		currpos = 0; answer = 0; protect = 0;
		cin >> smax >> sarray;
		//cout << "sarray: " << sarray << endl;
		while(currpos < smax){
			currval =(int) (sarray[currpos] - '0');
			//cout << "Currvale: " << currval << endl;
			if(currval == 0 && protect == 0){
				answer++;
				//cout << "answer increased" << endl;
			} else{
				protect += currval;
					//cout << "protector changed" << endl;
				
				if(protect > 0){
					protect--;
				}
			}
			currpos++;
		}
		cout << "Case #" << i+1 << ": " << answer << '\n';
	}
	return 0;
}