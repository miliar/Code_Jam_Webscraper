#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int T;
	cout << "Enter the number of cases: \n";
  scanf("%d", &T);
  for(int k=0;k<T;k++)
  {
			  int flag =0, dotCount=0;
		  printf("\nEnter the test sequence: \n");
			char line[5][4];

		  for (int j=0;j<4;j++)
		  {
			cin >>line[j];
		  }
		   for(int i=0;i<4;i++)
			{
			  int xcount=0,Ocount=0,Tcount=0;
			  for(int j=0;j<4;j++)
			  {
				  if(line[i][j]=='X')
					xcount++;
				  if(line[i][j]=='O')
					Ocount++;
				  if(line[i][j]=='T')
					Tcount++;
				  if(line[i][j]=='.')
					  dotCount++;
			  }
			  if(xcount==4)
			  {
				  printf("\nX wins\n");
				  flag=1;
				  break;
			  }
			  else if(xcount == 3 && Tcount ==1)
			  {
				  printf("\nX wins\n");
				  flag=1;
				  break;
			  }

			  else if(Ocount==4)
			  {
				  printf("\nO wins\n");
				  flag=1;
				  break;
			  }

			  else if (Ocount ==3 && Tcount ==1)
			  {
				  printf("\nO wins\n");
				  flag=1;
				  break;
			  }
			}
	   	
		    for(int j=0;j<4;j++)
			{
			  int xcount=0,Ocount=0,Tcount=0;
			  for(int i=0;i<4;i++)
			  {
				  if(line[i][j]=='X')
					xcount++;
				  if(line[i][j]=='O')
					Ocount++;
				  if(line[i][j]=='T')
					Tcount++;
			  }
			  if(xcount==4)
			  {
				  printf("\nX wins\n");
				  flag=1;
				  break;
			  }
			  else if(xcount == 3 && Tcount ==1)
			  {
				  printf("\nX wins\n");
				  flag=1;
				  break;
			  }

			  else if(Ocount==4)
			  {
				  printf("\nO wins\n");
				  flag=1;
				  break;
			  }

			  else if (Ocount ==3 && Tcount ==1)
			  {
				  printf("\nO wins\n");
				  flag=1;
				  break;
			  }

			}
	  			 int xcount=0,Ocount=0,Tcount=0;

			  for(int i=0;i<4;i++)
			{
				  if(line[i][i]=='X')
					xcount++;
				  if(line[i][i]=='O')
					Ocount++;
				  if(line[i][i]=='T')
					Tcount++;
				  if(line[i][i]=='.')
					  dotCount++;
		  }
			  if(xcount==4)
			  {
				  printf("\nX wins\n");
				  flag=1;
			  }
			  else if(xcount == 3 && Tcount ==1)
			  {
				  printf("\nX wins\n");
				  flag=1;
			  }

			  else if(Ocount==4)
			  {
				  printf("\nO wins\n");
				  flag=1;
			  }

			  else if (Ocount ==3 && Tcount ==1)
			  {
				  printf("\nO wins\n");
				  flag=1;
			  }
   
			   xcount=0,Ocount=0,Tcount=0;

				  if(line[3][0]=='X')
					xcount++;
				  else if(line[3][0]=='O')
					Ocount++;
				  else if(line[3][0]=='T')
					Tcount++;
				  else if(line[3][0]=='.')
					dotCount++;
				  if(line[1][2]=='X')
					xcount++;
				  else if(line[1][2]=='O')
					Ocount++;
				  else if(line[1][2]=='T')
					Tcount++;
				  else if(line[1][2]=='.')
					dotCount++;
				  if(line[2][1]=='X')
					xcount++;
				  else if(line[2][1]=='O')
					Ocount++;
				  else if(line[2][1]=='T')
					Tcount++;
				  else if(line[2][1]=='.')
					dotCount++;
				  if(line[0][3]=='X')
					xcount++;
				  else if(line[0][3]=='O')
					Ocount++;
				  else if(line[0][3]=='T')
					Tcount++;
				  else if(line[0][3]=='.')
					dotCount++;
				
			  if(xcount==4)
			  {
				  printf("\nX wins\n");
				  flag=1;
			  }
			  else if(xcount == 3 && Tcount ==1)
			  {
				  printf("\nX wins\n");
				  flag=1;
			  }

			  else if(Ocount==4)
			  {
				  printf("\nO wins\n");
				  flag=1;
			  }

			  else if (Ocount ==3 && Tcount ==1)
			  {
				  printf("\nO wins\n");
				  flag=1;
			  }
		  if(flag==0)
			 {
				 if(dotCount >0)
					  printf("Game is not completed");
				 if(dotCount == 0)
					 printf("Game is drawn");
			 }
  }
 system("pause");
}

