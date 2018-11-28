/*******************************************************
Author	:	~~darkevolutions~~
Purpose	: Google CodeJam Event
Problem	: [C] Fair and Square 	
file	: problem.cpp

********************************************************/
#include<iostream>
#include<math.h>
#include<sstream>
#include<string>
#include<fstream>

using namespace std;


/*******************************************************
Author		: ~~darkevolutions~~
Method		: isperfect
Discription	: Gives the perfect Square root
Arguments	: n the number who's square root to be calculate
Returns: 
	Success	: will return the square root of the n
	Failure	: return -1
********************************************************/
long isperfect(long n)
{
    double x=sqrt((double)n);
    if(n==(x*x))
        return x;
    else
        return -1;
}

/*******************************************************
Author		: ~~darkevolutions~~
Method		: ispaliindrome
Discription	: Tells the number is paliindrome or not
Arguments	: num the number who's paliindrome to be calculate
Returns:		 
	Success	: will return the reverse of the num if it is a paliindrome
	Failure	: return -1
********************************************************/
long ispaliindrome(long num)
{

     int n, digit, rev = 0;
     n = num;
     do
     {
         digit = num%10;
         rev = (rev*10) + digit;
         num = num/10;
     }while (num!=0);

     if (n == rev)
     {
        return rev;
     }
     else
     {
        return -1;
     }
}

/*******************************************************
Author		: ~~darkevolutions~~
Method		: checkIntervals
Discription	: check the numbers between range and return the result of Fair and Square numbers
Arguments	: num the number who's paliindrome to be calculate
Returns		: will return the Fair and Square numbers
********************************************************/
int checkIntervals(long to, long from)
{
	int isplndrme,isprfct,ok;
	int count = 0;
	for( int i = to ; i <= from ; i++)
	{  
		if(( isplndrme = ispaliindrome(i)) != -1)
		{
			if(( isprfct = isperfect(isplndrme)) !=-1)
			{
			   	if(( ok = ispaliindrome(isprfct)) != -1)
		 		{
				    count++;
				}	
			}
		}
	}
 	return count;
}


/*******************************************************
Author		: ~~darkevolutions~~
Method		: main
Discription	: main of the program
Arguments	: takes file as a argument
Returns		: 0
********************************************************/
int main(int argc, char *argv[])
{    
	std::ifstream infile(argv[1]);
	std::string line;
	int T , A , B, result;
	infile >> T;
 	int count = 1;
	while (infile >> A >> B)
	{
		for(int i =1 ;i <= T ; i++) 
		{
			result = checkIntervals(A, B);
		} 
	cout <<"Case #" <<count << ": " << result <<endl;	
	count++;	
	}	

	return 0;
} 
