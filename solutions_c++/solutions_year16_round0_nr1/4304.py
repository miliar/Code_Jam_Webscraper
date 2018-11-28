#include <iostream>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <fstream>
#include <algorithm>
using namespace std;

int main(){
	ofstream output;
	output.open("output.txt");
	int t;
	cin >> t;
	for(int i=1;i<=t;i++){
		output << "Case #" << i << ": ";
		int input;
		cin >> input;
		if(input==0) 
			output << "INSOMNIA" << endl;
		else{
			//cout << "jai shree shyam " << endl;
			vector<int> array(10);	
			int p = 1;
			int input1 = 0;
			while(find(array.begin(),array.end(),0)!=array.end()){
				//cout << "in loop " << endl;
				input1 = input*p;
				//cout << "in loop input1 " << input1 << endl;
				int checkNumber = input1;
				while(checkNumber)
				{
					array[checkNumber%10]++;				
					//cout << endl;
					checkNumber = checkNumber/10;
				}
				p++;
			}
			output << input1 << endl;
			//cout << "input value " << input1 << endl;
		 }
	}
	return 0;
}