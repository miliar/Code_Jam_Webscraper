/*************************************************************************
    > File Name: A.cpp
    > Author: Hu Pengxiang
    > Mail: hpxiangsky@gmail.com 
    > Created Time: Sat 12 Apr 2014 06:07:47 PM CST
 *************************************************************************
 Function:
		1. 
 History:
		1. Created by Hu Pengxiang on Sat 12 Apr 2014 06:07:47 PM CST
 ************************************************************************/

#include<iostream>
using namespace std;

int main()
{
	// >> A
	// >> B

	//A[a] intersect B[b]
	
	
	int N;
	cin >> N;

	for(int i = 0;i < N;++i)
	{
		//a case
		int a, b;
		int A[16], B[16];

		cin >> a;
		for(int j = 0;j < 16;++j)
			cin >> A[j];
		cin >> b;
		for(int j = 0;j < 16;++j)
			cin >> B[j];

		int sameNum = 0;
		int savedAnswer;
		for(int j = 0;j < 4;++j)
			for (int k = 0;k < 4;++k)
				if(A[4*(a-1)+j] == B[4*(b-1)+k])
				{
					sameNum ++;
					savedAnswer = A[4*(a-1)+j];
					break;
				}
		
		// output
		cout << "Case #" << (i+1) << ": ";
		if(sameNum == 1)
			cout << savedAnswer << endl;
		else
			if(sameNum > 1)
				cout << "Bad magician!" << endl;
			else
				cout << "Volunteer cheated!" << endl;
	}
}
