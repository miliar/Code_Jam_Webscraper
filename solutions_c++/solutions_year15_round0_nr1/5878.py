/*
 * ovation.cpp
 *
 *  Created on: 11-Apr-2015
 *      Author: porichar
 */

#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;
int main ()
{
	int loop = 1;
//	printf("test cases - ");
	scanf("%d",&loop);
	FILE *f = fopen("/home2/porichar/pop/g/out/l_ocation.txt", "a+");
	for(int i=1 ;i <=loop ; i++)
	{
		int audi_count = 0;
		int retVal=0;
		int maxshyness;
		string audi;
		cin >> maxshyness >> audi;
//		printf("%s", audi.c_str());
		for(int j=0;j<audi.length();j++)
		{
			char c = audi[j];
			int curr_audi = c - '0';
			audi_count += curr_audi;
			if (audi_count<(j+1))
			{
				retVal += ((j+1)-audi_count);
				audi_count += ((j+1)-audi_count);
			}
//			printf("curr = %d, audi_tot = %d, ret - %d , j = %d \n", curr_audi, audi_count, retVal, j);
		}
		fprintf(f,"case #%d: %d\n", i, retVal);
	}
	fclose(f);
	return 0;
}

