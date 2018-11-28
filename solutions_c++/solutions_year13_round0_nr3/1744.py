#include<iostream>
#include<fstream>
#include<string>
#include<math.h>
#include<sstream>

using namespace std;

string NumberToString(unsigned long long number)
{
	stringstream ss;//create a stringstream
	ss << number;//add number to the stream
	return ss.str();//return a string with the contents of the stream
}

string getReverse(string strOrigNumber)
{
	int leng = strOrigNumber.length();
	char temp;
	
	for (int i=0; i<leng/2; ++i) {
		temp = strOrigNumber[i];
		strOrigNumber[i] = strOrigNumber[leng-i-1];
		strOrigNumber[leng-i-1]=temp;
	}
	return strOrigNumber;
	
}
string getLeftHalf(string x)
{
	return x.substr(0,(x.length()/2));
}

string getMiddle(string x)
{
	return x.substr(((x.length()-1)/2),1);
}

unsigned long long roundUp(unsigned long long number)
{
	string strNumber = NumberToString(number);
	//string strNumber = to_string(number);
	int leng = strNumber.length();
	long long increment=pow(10,((leng/2)+1));
	return ((number/increment)+1)*increment;
}

unsigned long long getNextPalindrome(unsigned long long x)
{
	unsigned long long newNum,increment;
	string strNumber = NumberToString(x);
	int leng = strNumber.length();
	bool oddDigits = false;
	string leftHalf,middle;
	if (leng%2 != 0) {
		oddDigits = true;
	}
	leftHalf=getLeftHalf(strNumber);
	//cout << "\nleftHalf = " << leftHalf;
    middle=getMiddle(strNumber);
	//cout << "\nmiddle = " << middle;
	
	if (oddDigits) {
		increment=pow(10, leng/2);
		stringstream(leftHalf.append(middle.append(getReverse(leftHalf)))) >> newNum;
		//cout << "\nnewNum = " << newNum;
	}else {
		increment=1.1*pow(10, leng/2);
		stringstream(leftHalf.append(getReverse(leftHalf))) >> newNum;
	}
	if (newNum>x) {
		return newNum;
	}
	if (middle[0] != '9') {
		//cout << "Entered middle = " << middle;
		return newNum+increment;
	}else {
		//cout << "roundUp(x) = " << roundUp(x);
		return getNextPalindrome(roundUp(x));
	}
	
}

bool isPalindrome(unsigned long long num)
{
	unsigned long long n,digit,rev=0;
	n=num;
	do{
		digit = num%10;
		rev = (rev*10) + digit;
		num = num/10;
	}while (num!=0);

	if (n==rev) {
		return true;
	}else {
		return false;
	}
}


int main(int argc, char *argv[])
{
	ifstream file;
	ofstream outputFile;
	string strFinalOutput;
	stringstream ss;
	
	int intTestCases=0, intCounter=0;
	unsigned long long intA=0, intB=0, intSqrRootA=0, intSqrRootB=0 ;
	string strNumber,strSquareNumber;
	
	outputFile.open(argv[2]);

	file.open(argv[1]);

	if(!file.eof())
	{
		file >> intTestCases;
		unsigned long long j=0;
	
		for(int i=0; i<intTestCases; ++i){
			file >> intA;
			file >> intB;
			intCounter=0;
		
			intSqrRootA = ceil(sqrt(intA));
			intSqrRootB = floor(sqrt(intB));
			
			for (j=intSqrRootA; j<=intSqrRootB; ++j) {
				//string strNumber = NumberToString(j);
				if (isPalindrome(j)) {
					//strSquareNumber = NumberToString(j*j);
					if (isPalindrome(j*j)) {
						intCounter++;
					}
					
					//cout << "\nValue of j = " << j << endl;
					j = getNextPalindrome(j) -1;
					//cout << "\nNext Palindrome : " << getNextPalindrome(j) << endl;
				}
			}
			
			j=0;
			if (i!=0) {
				ss << "\nCase #" << i+1 << ": " << intCounter;
				//strFinalOutput.append(ss.str());
			}
			else {
				ss << "Case #" << i+1 << ": " << intCounter;
				//strFinalOutput.append(ss.str());
			}
			//strNumber="";
			//cout << "\nstrFinalOutput = " << strFinalOutput;
		}

	
	
	}
	
	outputFile << ss.str();
	outputFile.close();
	file.close();
	
	return 0;

}


