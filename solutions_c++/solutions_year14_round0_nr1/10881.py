/* 
 * File:   main.cpp
 * Author: Sreekanth
 *
 * Created on Apr 12, 2014
 */

#include <stdlib.h>
#include <stdio.h>
#include <algorithm>
#include <vector>
using namespace std;

/*
 * 
 */

int main()
{
  freopen("I.in","r",stdin);
  freopen("O.op","w",stdout);

  int cases;
  scanf("%d",&cases);
  int caserunning=0;
  while (cases--)
  {
	  int rowsfound[2] = {0};
	  std::vector<int> rowdata1;
	  std::vector<int> rowdata2;

	  scanf("%d",&rowsfound[0]);
	  int from = (4 * rowsfound[0]) - 4;
	  int to = from + 4;
	  for(int i = 0 ; i < 16;i++)
	  {
		  int dum;
		  scanf("%d",&dum);
		  if(i >= from && i < to)
		  {
			  rowdata1.push_back(dum);			  			  
		  }
	  }

	  scanf("%d",&rowsfound[1]);
	  from = (4 * rowsfound[1]) - 4;
	  to = from + 4;

	  for(int i = 0 ; i < 16;i++)
	  {
		  int dum;
		  scanf("%d",&dum);
		  if(i >= from && i < to)
		  {
			  rowdata2.push_back(dum);			  			 
		  }
	  }
	  int status = 0;
	  // 1 found the number
	  // 2 Volunteer cheated!
	  // 3 Bad magician!
	  int number;
	  for(int i = 0; i < 4 ; i++)
	  {
		 if(std::find(rowdata2.begin(), rowdata2.end(), rowdata1[i])!=rowdata2.end())
		 {
			 if(status == 1)
			 {
				status = 3;
				break;
			 }
			 else
			 {
				 status = 1;
				 number = rowdata1[i];
			 }
		 }
		 
	  }
	  
	  if(status == 1)
	  {
		printf("Case #%d: %d\n",++caserunning , number);
	  }
	  else if(status == 3)
	  {
		  printf("Case #%d: Bad magician!\n",++caserunning);		
	  }
	  else
	  {
		printf("Case #%d: Volunteer cheated!\n",++caserunning);
	  }
	
  }


  return 0;
}

