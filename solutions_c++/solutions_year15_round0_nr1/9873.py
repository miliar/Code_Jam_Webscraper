#include <stdio.h>
#include <stdlib.h>
#include <iostream>

using namespace std;

int main()
{
	int caseNum;

	cin >> caseNum;

	for(int case_i = 1; case_i <= caseNum; case_i++)
	{
		cout<<"Case #"<<case_i<<": ";
		int result = 0;	//min friend
		int shynessMax;
		int shynessLvString;

		int totalstandup = 0;


		cin>>shynessMax;
		cin>>shynessLvString;

		int *array = new int[shynessMax+1];

		for(int i=0;i<=shynessMax;i++)
		{
			array[shynessMax - i] = shynessLvString%10;
			shynessLvString = shynessLvString /10;
		}

		totalstandup = array[0];
		for(int i=1;i<=shynessMax;i++)
		{
			int add = 0;
			if(i>totalstandup)
				add = i - totalstandup;
			result += add;
			totalstandup += add + array[i];
		}
		cout<<result<<endl;
		delete [] array;
	}

	return 0;
}
