#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
//#include <iomanip> 
using namespace std;
//#define LARGE



int main() 
{
#if 1
#ifndef LARGE
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
#else
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
#endif
#endif
	int T,row1,row2;
	int count=0;
	int card=0;

	int temp;
	int set1[4];
	int set2[4];
	scanf("%d", &T);

	for (int V = 1; V <= T; ++V) 
	{
	  count=0;
	  cin>>row1;
	  for(int i=1; i<=4;i++)
	  {
		  if(i ==row1)
		  {
			cin>>set1[0]>>set1[1]>>set1[2]>>set1[3];			
		  }
		  else
		  {
			cin>>temp>>temp>>temp>>temp;
		  }
	  }
	  cin>>row2;
	  for(int i=1; i<=4;i++)
	  {
		  if(i ==row2)
		  {
			  cin>>set2[0]>>set2[1]>>set2[2]>>set2[3];
			
		  }
		  else
		  {
			 //cin>>temp[0]>>temp[1]>>temp[2]>>temp[3];
			 cin>>temp>>temp>>temp>>temp;
			
		  }
	  }	  
	  
	  for(int i=0; i<4;i++)
	  {
		  for(int j=0; j<4;j++)
		  {
			if(set1[i]==set2[j])
			{
				count = count+1;
				card=set1[i];
			}
		  }
	  }
	 
	  printf("Case #%d: ", V);
	  if(count==0)
		  printf("Volunteer cheated!\n");
	  else if(count==1)
		  printf("%d\n",card);
	  else
		  printf("Bad magician!\n");
	}
	return 0;
}
