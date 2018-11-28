// Fair and Square.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <math.h>
#include <iostream>

using namespace std;

bool isPalindrome(double x) {
    int palindrome = 0;
	int originalNumber = (int) x;
    int origin = originalNumber;

    // get the palindrome
    while(originalNumber != 0) {
        palindrome = palindrome * 10 + originalNumber % 10;
        originalNumber /= 10;
    }

    return palindrome == origin ;
}

int _tmain(int argc, _TCHAR* argv[])
{
	freopen("E:/google code jam/Fair and Square/c.in", "r", stdin);
    freopen("E:/google code jam/Fair and Square/c.out", "w", stdout);
	int caseNo = 0;
	int num;//��fair and square
	int Isqrt = 0;//��ƽ������������
	double Dsqrt = 0.0;
	cin>>caseNo;
	int a=0,b=0;//����[a,b]
	for(int cno = 0;cno < caseNo;cno++)
	{
		num = 0;
		cin>>a;
		cin>>b;
		for(double i = a; i <= b; i++)
		{
			Dsqrt = sqrt(i);
			Isqrt = (int)Dsqrt;
			if(Dsqrt - Isqrt == 0 && isPalindrome(i) && isPalindrome(Isqrt))
			{
				num++;
				//cout<<i<<endl;
			}
		
		}
		cout<<"Case #"<<cno+1<<": "<<num<<endl;

	}
	return 0;
}

