#include<iostream>
#include<fstream>
#include<sstream>
#include<string>
#include<math.h>

using namespace std;

string convertInt(int number)
{
   stringstream ss;//create a stringstream
   ss << number;//add number to the stream
   return ss.str();//return a string with the contents of the stream
}

bool isPalindrome(int a){
	string s = convertInt(a);
	bool val = true;
	int size = s.size();
	int i=0;
	while(i<size/2){
		if(s[i] != s[size-i-1]){
			val = false;
		}
		i++;
	}
	return val;
}

int main(){
	int num, n, m, numberOf, temp;
	double sq;
	double intpart;
	ifstream inFile;
	ofstream outFile;
	inFile.open("input.in");
    outFile.open("output.out");
    if(!inFile){
        cerr << "Unable to DIE";
    }
    inFile >> num;
	
	for(int i=0; i<num; i++){
		inFile >> n;
		inFile >> m;
		numberOf = 0;
		outFile << "Case #" << convertInt(i+1) + ": ";
		cout << "Case #" << convertInt(i+1) + ": ";
		for(int j=n; j<=m; j++){
			if(isPalindrome(j)){
				sq = sqrt(j);
				if(modf(sq, &intpart) == 0.0){
					temp = (int)intpart;
					if(isPalindrome(temp)){
						numberOf++;
					}
				}
			}
		}
		outFile << numberOf << "\n";
		cout << numberOf << "\n";
	}
}