#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include <stdio.h>
#include <fstream>
using namespace std;



int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, arr[4][4], arr2[4][4],r1,r2,counter,num;
	cin >> t;
	for(int i = 1; i <= t; i++)
	{
		counter = 0;
		cin >> r1; r1 -= 1;
		for(int o = 0; o < 4; o++)
		{
			for(int j = 0; j < 4; j++)
			{
				cin >> arr[o][j];

			}
		}
		cin >> r2; r2 -= 1;

		for(int o = 0; o < 4; o++)
		{
			for(int j = 0; j < 4; j++)
			{
				cin >> arr2[o][j];

			}
		}

		for(int o = 0; o < 4; o++)
		{
			for(int j = 0; j < 4; j++)
			{
				if(arr[r1][o] == arr2[r2][j])
				{
					counter++; 
					num = arr2[r2][j];
				}

			}
		}

		if(counter == 0) cout << "Case #" << i << ": Volunteer cheated!" << endl;
		if(counter == 1) cout << "Case #" << i << ": "<<num << endl;
		if(counter >1) cout << "Case #" << i << ": Bad magician!" << endl;















	}fclose(stdout);
	
	return 0;



}