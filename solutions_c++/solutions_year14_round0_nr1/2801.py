/*
 * mt.cpp
 *
 *  Created on: Apr 12, 2014
 *      Author: prakhar
 */
#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <stdio.h>
#include <vector>
int main(int a, char** v)
{
	int numTestCases;
	scanf("%d",&numTestCases);
	int i,j,k;
	for ( i = 0;  i < numTestCases; i++) {
		int ans1=0,ans2=0,ans=-1;
		int arr1[4][4];int arr2[4][4];
		for (j= 0; j < 4; j++)
			for(k=0; k <4; k++)
				arr1[j][k]=0; arr2[j][k]=0;
		scanf("%d",&ans1);
		for (j= 0; j < 4; j++)
			for(k=0; k <4; k++)
				scanf("%d",&arr1[j][k]);
		scanf("%d",&ans2);
		for (j= 0; j < 4; j++)
			for(k=0; k <4; k++)
				scanf("%d",&arr2[j][k]);
		for (j= 0; j < 4; j++)
			for(k=0; k <4; k++)
			{
				if(arr1[ans1-1][j] == arr2[ans2-1][k])
				{
					if(ans==-1) ans = arr1[ans1-1][j];
					else	ans = -2;
				}
			}
		if(ans==-1) printf("Case #%d: %s\n",i+1,"Volunteer cheated!");
		else if(ans==-2) printf("Case #%d: %s\n",i+1,"Bad magician!");
		else printf("Case #%d: %d\n",i+1,ans);
	}

	return 0;
}
