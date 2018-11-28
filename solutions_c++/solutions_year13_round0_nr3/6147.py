#include<iostream>
#include<math.h>
#include <sstream>
#include <string>
#include <fstream>

using namespace std;

long isperfect(long n)
{
    double x=sqrt((double)n);
    if(n==(x*x))
        return x;
    else
        return -1;
}

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

int writeOutput(long to, long from)
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
			result = writeOutput(A, B);
		} 
	cout <<"Case #" <<count << ": " << result <<endl;	
	count++;	
	}	

	return 0;
} 
