#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <algorithm> 

bool isPalindrome(int num)
{
	int numCopy = num;
	int sum = 0;
	int rem;
	while(num!=0)
    {
        rem=num%10;
        num=num/10;
        sum=sum*10+rem; 
    }
	
	return sum == numCopy;
}

int binarySearch(int arr[],int search, int index)
{
	int first = 0;
	int last = index -1;
	int middle = (first + index)/2;
 
	   while( first <= last )
	   {
	      if ( arr[middle] < search )
	         first = middle + 1;    
	      else if ( arr[middle] == search ) 
	      {
	         return middle;
	      }
	      else
	         last = middle - 1;
	 
	      middle = (first + last)/2;
	   }
	   return last;
}

int main()
{
	FILE *fp,*fp1;
    fp = fopen("C-small-attempt2.in","r");
    fp1 = fopen("output.txt","w");
     if(fp == NULL || fp1 == NULL){
     exit(0);
    }
     int T;

    fscanf(fp,"%d",&T);
    int count = T-1;
    int tCount = T;
	
	int start ;
	int end;
	int output = 0 ;
	int numberOfFairPalindrome = 31;
	int looper = 1;
	int fairPalindrome[numberOfFairPalindrome];
	//printf("%d\n",numberOfFairPalindrome);
	int index = 0;
	while( looper <= numberOfFairPalindrome)
	{
		if(isPalindrome(looper))
		{
			int newNum = looper*looper;
			if(isPalindrome(newNum))
			{
				fairPalindrome[index++] = newNum;
				printf("%d\n",newNum);
			}
		}
		looper++;
	}
 	while( tCount > 0 ){
		output = 0 ;  //Reset output
		fscanf(fp,"%d",&start);
		fscanf(fp,"%d",&end);
	 	int startP = binarySearch(fairPalindrome,start,index);
	 	int endP = binarySearch(fairPalindrome,end,index);
	 	if( startP == -1)
	 		startP = 0;
 		if(endP == -1)
 			endP = 0;
 			
		if(fairPalindrome[startP] < start && startP < (index -1))
 		{
		 	startP++;
		 }
		if(fairPalindrome[endP] < end && endP < (index -1))
 		{
		 	end++;
		}
		if(  endP == (index -1) && fairPalindrome[endP] < end && fairPalindrome[startP] >= start)
		{
			fprintf(fp1,"Case #%d: %d\n",(T-count),index - startP);
		}else if(( endP == startP && endP == (index	-1)&& fairPalindrome[endP] < end && fairPalindrome[startP] < start)){
			fprintf(fp1,"Case #%d: %d\n",(T-count),0);
			
		}else{
			fprintf(fp1,"Case #%d: %d\n",(T-count),endP+1 - startP);
			
		}
		
		printf("%d %d\n",startP,endP);
        count--;
        tCount--;
		//free(scores);
	}	
	fclose(fp);
	fclose(fp1);
	return 1;
}
