/*int maintest(int argc,char **argv);*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#define FILEIO

int isFull(int array[],int count)
{
	int result =1;
	for(int i=0;i<count;i++)
	{
		if(array[i] ==0)
		{
			result = 0;
			break;
		}
	}
	return result;
}

void revert(int array[],int anchor)
{
	int counter = anchor%2 == 0? anchor/2:(anchor-1)/2;

	if(counter ==0)
	{
		array[0]=(array[0]+1)%2;
		return;
	}

	if(anchor%2==1)
	{
		array[(anchor-1)/2] = (array[(anchor-1)/2]+1)%2;
	}

	for(int i=0;i<counter;i++)
	{
		int temp = (array[i]+1)%2;

		array[i]=(array[anchor-1-i]+1)%2;
		array[anchor-1-i]=temp;
	}
}

int main(int argc,char **argv) 
{ 

#ifdef FILEIO
  freopen("in.txt","r",stdin); 
  freopen("out.txt","w",stdout); 
#endif

  int N;
  char c;
  int array[100] = {0};
  scanf("%d\n",&N);

  for(int index=0;index<N;index++)
  {
	  memset(array,0,100*sizeof(int));
	  int counter=0;
	  for(;;)
	  {
		  scanf("%c",&c);

		  if(c=='-')
		  {
			  array[counter] = 0;
		  }
		  else if(c=='+')
		  {
			  array[counter] = 1;
		  }
		  else
		  {
			  break;
		  }
		  counter++;
	  }
	  int result = 0;
	  int anchor = counter;
	  for(;;)
	  {
		  if(isFull(array,counter))
		  {
			  printf("Case #%d: %d\n", index+1, result);
			  break;
		  }

		  int i;
		  for(i=anchor-1;i>=0;i--)
		  {
			  if(array[i]==1)
			  {

			  }
			  else
			  {
				  anchor = i+1;
				  break;
			  }
		  }

		  if(array[0]==1)
		  {
			  int f = 0;
			  for(i=0;i<counter;i++)
			  {
				  if(array[i]==1)
				  {

				  }
				  else
				  {
					  f = i;
					  break;
				  }
			  }
			  revert(array,f);
			  result+=1;
		  }
		  
			revert(array,anchor);
			result++;
	  }
  }

#ifdef FILEIO
  fclose(stdin);
  fclose(stdout);
#endif  
  
  return 0; 
}
