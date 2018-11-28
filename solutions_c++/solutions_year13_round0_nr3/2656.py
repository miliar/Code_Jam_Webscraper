#include <iostream>
#include <string>
#include <fstream>
#include <cmath>

using namespace std;


bool isPalindrome(int a){


	string temp = to_string(a);

	int length = temp.length();
	
	if(length % 2 == 0){

		int half = length/2;


		for(int i=0;i<half;i++){

			if(temp[i] != temp[length-i-1]) return false;
			
		}


	}
	else
	{


		int half = (length-1)/2;


		for(int i=0;i<half;i++){

			if(temp[i] != temp[length-i-1]) return false;
			
		}



	}


	return true;

}


bool isPerfectSquare(int a){

	
	int sqr1 = ceil(sqrt(a));
	int sqr2 = floor(sqrt(a));
	
	if(sqr1 == sqr2) return true;

	return false;	
	

}


int main(){
	
	
	ifstream file("C-small-attempt0.in");
	ofstream outfile("output.txt");


	int total;
	file >> total;



	for(int i=0;i<total;i++){


		int a;
		file >> a;

		int b;
		file >> b;


		int count = 0;

		for(int j=a;j<=b;j++){

			if(isPerfectSquare(j)){
				

				if(isPalindrome(j) && isPalindrome(sqrt(j))){
					count++;
				}


			}

			
			
		}


		outfile << "Case #" << (i+1) << ": " << count << endl;


	}

	


}