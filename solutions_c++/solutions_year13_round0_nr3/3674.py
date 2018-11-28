
// Author Faisal

#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <string>

using namespace std;
#define MAX 1001001

int PS(int );
int PALINDROME(int );

char str[MAX];

int PALINDROME(int NUMBER){
 int REVERSE,n,DIGIT;
 n = NUMBER;
 REVERSE = 0;
 while (NUMBER > 0) {
      DIGIT = NUMBER % 10;
      REVERSE = REVERSE * 10 + DIGIT;
      NUMBER = NUMBER / 10;
  }
if(n==REVERSE) return 1; else  return 0;
}


int PS(int n)
{
    int h = n & 0xF; 
    if (h > 9)
        return 0; 

    if ( h != 2 && h != 3 && h != 5 && h != 6 && h != 7 && h != 8 )
    {
        int t = (int) floor( sqrt((double) n) + 0.5 );
            return t*t == n;
    }
    return 0;
}

int main()
{
	int t, len, odd, mid, i, j, flag,CNT,a,b;
	scanf("%d", &t);
	for(j=0;j<t;j++ )
	{
	        CNT=0;
		scanf("%d %d\n",&a,&b);
		for(i=a;i<=b;i++)
		  if(PALINDROME(i)&&PS(i)&&PALINDROME(sqrt(i)))
		   CNT++;
		
	  printf("Case #%d: %d\n",j+1,CNT);
	}
	return 0;
}



