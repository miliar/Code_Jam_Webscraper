#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>

using namespace std;
/* Palindromic number */
 double isPalindrome( double j)
{
   int reverse = 0, temp;
   temp = j;
 
   while( temp != 0 )
   {
      reverse = reverse * 10;
      reverse = reverse + temp%10;
      temp = temp/10;
   }
 
   if ( j == reverse )
      return 0;     
	/* printf("%d is a palindrome number.\n", n); */
   else
     return 1;
	/* printf("%d is not a palindrome number.\n", n); */
}
	
int isInteger(double d){
int i=d;
double t=d-i;
//printf("%f", t);
if ((t==0)&&((isPalindrome(d)==0))) return 1;
else 
    return 0;
	
}		

int T,a,b;
double h;
double s;
int main()
{
	freopen("C-small-attempt4.in","r",stdin);
	freopen("C4.out","w",stdout);
	scanf("%d", &T);
	for (int casenum=0; casenum<T; casenum++)
	{
		scanf("%d%d", &a,&b);
		
		int count=0;
		for (int i=0; i<(b-a+1); i++)
		{   
		h=a+i;
	//	printf("%f \n", s);
	//	printf("%d",isInteger(s) );
		if ((isPalindrome(h)==0)){
		s=sqrt(h);
		if(isInteger(s)==1) 
		  { // printf("%f", s);
		  count++;}
        else  count=count+0;}
    }
      
       
		printf("Case #%d: %d\n", casenum+1, count);
	}
}


	
