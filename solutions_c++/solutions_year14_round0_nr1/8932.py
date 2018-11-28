#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<cmath>
#include<string>
#include<cstdio>
#include <stdio.h>
#include<sstream>
#include<map>
#include<list>
#include<queue>
#include<set>
#include<numeric>
using namespace std;
int main()
{
   int t,r1,r2,i,j,counter,num;
   int arr1[10][10];
   int arr2[10][10];
   cin>>t;
   for (int k = 0; k < t; k++)
   {
	   counter=0;
	   cin>>r1;
	   r1--;
	   for ( i = 0;  i < 4;  i++)
	   {
		   for ( j = 0; j < 4; j++)
		   {
			   cin>>arr1[i][j];
		   }
	   }
	   cin>>r2;
	   r2--;
	   for ( i = 0;  i < 4;  i++)
	   {
		   for ( j = 0; j < 4; j++)
		   {
			   cin>>arr2[i][j];
		   }
	   }

	   for ( i = 0;  i < 4;  i++)
	   {
		   for ( j = 0; j < 4; j++)
		   {
			   if (arr1[r1][i]==arr2[r2][j])
			   {
				   counter++;
				   num=arr1[r1][i];
			   }
		   }
	   }
	   if (counter==0)
		   printf("Case #%d: Volunteer cheated!\n",k+1);
	   else if (counter==1)
	   printf("Case #%d: %d\n",k+1,num);
	   else printf("Case #%d: Bad magician!\n",k+1);

   }
	return 0;
}