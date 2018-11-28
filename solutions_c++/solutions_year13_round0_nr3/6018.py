// fair1.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("C-small-attempt1.in");
ofstream fout("C-small-attempt1.out");

 int pal(int,int);
 int checkPalindromes(int,int);

int main()
{
	int noofcases=0;
    int min;
	int max,i=0;

	fin>>noofcases;//in the qstn it is given that first line if the no of inputs
	while(i<noofcases)
	{
      fin>>min;//these two fin stmts will take limits for first test case
      fin>>max;
	  fout<<"Case #";//to print case# :p
	  fout<<i+1;//to print case no,as i strts from 0,i printd 1+1 for frst case
	  fout<<": ";
	  fout<<pal(max,min);
	  fout<<"\n";
	  i++;
	}
      return 0;
}
   
   int pal(int max,int min)
   {
	int num,num1;
	int temp=0,count=0;
    for(num=min;num<=max;num++)
	{
		 temp=sqrt(num);
		 //to check if the num is a perfect square
		 num1=temp*temp;
		 if(num==num1)
			//comes inside if it is a perfect square
		//the num is perfect sqaure
		//now we should check that the munber and is sqrt are palindromes
			if(checkPalindromes(temp,num1))
				//comes inside if both temp and num are palindromes
					//maintain count to count the numbers which are fair and sqaure
				count++;
	}
	return(count);
   }	
   int checkPalindromes(int temp,int num)
   {
	   int copytemp,copynum,rem=0,suma=0,sumb=0;
	   copytemp=temp;
	   copynum=num;
	   while(temp!=0)//code to reverse temp
	   {
		   rem=temp%10;
		   temp=temp/10;
		   suma=suma*10+rem;
	   }
	   while(num!=0)//code to reverse number
	   {
		   rem=num%10;
		   num=num/10;
		   sumb=sumb*10+rem;
	   }
	   if(suma==copytemp && sumb==copynum)//check if temp and num are palindromes
		   return(1);
	   else
		   return(0);
   }
