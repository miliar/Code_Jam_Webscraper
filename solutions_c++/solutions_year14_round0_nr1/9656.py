// Magic_Trick.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <string.h>
#include <cmath> 
#include<iomanip>
#include <cstring>
#include <ctype.h>
#include <stdio.h> 
#include<sstream>
#include<map>
#include<vector>
#include<queue>
using namespace std;
int _tmain(int argc, _TCHAR* argv[])
{
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	int t, n1, n2;
	cin >> t;
	int arr1[4][4];
	int arr2[4][4];
	for (int i = 0; i<t; i++)
	{
		cin >> n1;
		for (int j = 0; j<4; j++)
		for (int k = 0; k<4; k++)
			cin >> arr1[j][k];


		cin >> n2;
		for (int j = 0; j<4; j++)
		for (int k = 0; k<4; k++)
			cin >> arr2[j][k];
		int x, z = 0;
		for (int j = 0; j<4; j++)
		for (int k = 0; k<4; k++)
		if (arr1[n1 - 1][j] == arr2[n2 - 1][k])
		{
			z++;
			x = arr1[n1 - 1][j];

		}

		if (z == 0)
			printf("Case #%d: Volunteer cheated!\n", i + 1);
		else if (z>1)
			printf("Case #%d: Bad magician!\n", i + 1);
		else
			printf("Case #%d: %d\n", i + 1, x);
	}
	return 0;

}