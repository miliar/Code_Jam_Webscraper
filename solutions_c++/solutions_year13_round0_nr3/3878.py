#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cstring>
using namespace std;

bool isPalindrome(char* str, int len)
{
	for(int i=0; i<=len/2; i++) {
		int j = len-1 - i;
		if( str[i] != str[j] )
			return false;
	}
	return true;
}

int main()
{
	int nTests;
	cin>>nTests;
	for(int tc=1; tc<=nTests; tc++) {

		int firstNum, lastNum;
		cin>>firstNum>>lastNum;

		int cnt = 0;
		for(int num=firstNum; num<=lastNum; num++) {

			int sqrtNum = (int)sqrt((double)num);
			if( sqrtNum * sqrtNum != num )
				continue;

			char strNum[5], strSqrtNum[5];
			int lenNum, lenSqrtNum;
			itoa(num, strNum, 10);
			itoa(sqrtNum, strSqrtNum, 10);
			lenNum = strlen(strNum);
			lenSqrtNum = strlen(strSqrtNum);

			if( isPalindrome(strNum, lenNum) && isPalindrome(strSqrtNum, lenSqrtNum) )
				cnt++;

		}

		cout<<"Case #"<<tc<<": "<<cnt<<endl;
	}
	return 0;
}