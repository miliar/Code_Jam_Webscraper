#include <iostream>
using namespace std;
#include <string>
#include <cmath>
#include <fstream>


int nSquare(int number);
int nFair( int number);

int main()
{
	ifstream openFile;
	ofstream outFile;
	string tempStr, tempI;

	int numCases, low, high, fairSquare=0, nSqr;
	openFile.open("C-small-attempt0.in",ifstream::in);
	outFile.open("C-small-result.in", ofstream::out);
	
	openFile>> numCases;
	//cout<<"numCases = "<<numCases<<endl;

	for(int a=0; a<numCases; a++){
		fairSquare=0;

		openFile>>low>>high;
		//cout<<"low = "<<low<<endl;
		//cout<<"high = "<<high<<endl;

		for( int i=low ; i<=high ; i++){
			nSqr= nSquare(i);
			if( pow(nSqr, 2) == i ){
				//cout<<i<<" is a perfect square of "<< nSqr<<endl;
				if( (nFair(nSqr) == nSqr) && (nFair(i)==i)){
					fairSquare++;
				}
			}
		}
		outFile<<"Case #"<<a+1<<": "<<fairSquare<<endl;
	}
}

int nSquare(int number){
	int temp = (int) sqrt(number);
	if( int(pow( temp, 2)) == number) 
		return temp;
	else
		return NULL;
}

int nFair( int number){
	char first, second;
	bool palindrome = false;
	if(number<10)//if number<10, palindrome 
		return number;
	else if(number <=100 && (number%11==0))//if number<100 and divisibly by 11, palindrome
		return number;
	else {
		string temp= to_string(number);
		int tempLength = temp.length();
		
		for(int b=0; b<tempLength/2; b++){
			first = temp.substr(b,b+1).c_str()[0];
			second = temp.substr(tempLength-b-1,1).c_str()[0];
			//cout<<"First Slice = "<< first << "\nSecond Slice= "<< second<<endl;

			if( first == second )
			{
				palindrome= true;
			}
			else 
				palindrome= false;
		}
	}

	if(palindrome)
		return number;
	else  
		return NULL;
	
}