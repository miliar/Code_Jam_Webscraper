#include<iostream>
#include<sstream>
#include<cstdio>
#include<stack>
#include<queue>
#include<algorithm>
#include<cstring>
#include<string>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<vector>

using namespace std;

bool perfectSquare(int & value){
	int i = 1;
	int powerOfTwo;

	while (true){
		powerOfTwo = i*i;
		if (powerOfTwo == value){
			return true;
		}
		if (powerOfTwo > value){
			return false;
		}
		i++;
	}
}

string reverseString(string & str){
string stringRev = str;
reverse(stringRev.begin(), stringRev.end());
return stringRev;
}

bool palindrome(int& value){
	string result;
	string stringReversed;
    ostringstream convert;
	convert << value;
	result = convert.str();
	stringReversed = reverseString(result);

if (stringReversed == result){
	return true;
}
return false;
}

int main(){


	freopen("square.in", "r", stdin);
	freopen("square.out", "w", stdout);
	
	int T;
	int A;
	int B;
	int lowerB;
	int upperB;
	int numCases;
	int counter = 0;
	scanf("%d", &T);

	numCases = 0;
	while(numCases < T){
		scanf("%d%d", &A,&B);
		lowerB = A;
		upperB = B;

		while (lowerB <= upperB){
			if (perfectSquare(lowerB)){
				if(palindrome(lowerB)){
					double sqrtDouble = sqrt((double)lowerB);
					int sqrtInt = (int)sqrtDouble;
					if (palindrome(sqrtInt)){
						counter++;
					}
				}
			}
			lowerB++;
		}
		numCases++;
		printf("Case #%d: %d\n", numCases, counter);
		counter = 0;
	}
	return 0;
}