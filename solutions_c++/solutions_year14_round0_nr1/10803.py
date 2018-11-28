// GCJ.cpp
// Case A.
#include <stdio.h>
#include <string.h>
#include <vector>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;
int T;
int main()
{
	freopen("C:/A-small-attempt0.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
	scanf("%d",&T);
	int first[4];
	int second[4];
	int temp;
	int row1,row2;
    for(int i =1;i<T+1;i++)
	{
       scanf("%d",&row1);
	   for(int i1 =0;i1<4;i1++)
	   {
		   if(i1 == row1-1)
		   {
			   for(int i2 =0;i2<4;i2++)
			   {
				  scanf("%d",&first[i2]);
			   }
		   }
		   else
		   {
			   for(int i2 =0;i2<4;i2++)
			   {
                 scanf("%d",&temp);
			   }
		   }
	   }
	   scanf("%d",&row2);
	   for(int i1 =0;i1<4;i1++)
	   {
		   if(i1 == row2-1)
		   {
			   for(int i2 =0;i2<4;i2++)
			   {
				  scanf("%d",&second[i2]);
			   }
		   }
		   else
		   {
               for(int i2 =0;i2<4;i2++)
			   {
				   scanf("%d",&temp);
			   }
		   }
	   }
	   vector<int> v(8);
	   vector<int>::iterator it;

	   sort(first,first+4);   
       sort(second,second+4);
	   it=set_intersection (first, first+4, second, second+4, v.begin());

	   printf("Case #%d: ", i);
	   if(it-v.begin()==1)
	   {
		   printf("%d\n",v.at(0));
	   }
	   else if(it-v.begin()==0)
	   {
		   printf("Volunteer cheated!\n");
	   }
	   else
	   {
		   printf("Bad magician!\n");
	   }
	}
	return 0;
}

