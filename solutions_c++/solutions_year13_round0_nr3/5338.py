#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>


using namespace std;
int ni() { int a; scanf( "%d", &a ); return a; }
double nf() { double a; scanf( "%lf", &a ); return a; }
char sbuf[100005]; string ns() { scanf( "%s", sbuf ); return sbuf; }
long long nll() { long long a; scanf( "%lld", &a ); return a; }

int foo(int aNum)
{
  char buff[1024];
  int i = 0;
  int rnum = 0;
  while(aNum > 0)
  {
    buff[i] = '0'+(aNum%10);
    aNum /= 10;
    ++i;
  }
  
  buff[i] = '\0';
  
  rnum = atoi(buff);
  
  return rnum;
}

bool hsqr(int aNum)
{
  int del[] = {1, 4, 5, 6, 9};
  
  int last = aNum%10;
  
  for(int i = 0; i < 5; ++i)
  {
    if(del[i] == last)
    {
      return true;
    }
  }
  
  return false;
}

int main( )
{  
	freopen( "in.txt", "r", stdin );
	freopen( "out.txt", "w", stdout );

	int T = ni();
	
	for(int k = 0; k < T; ++k)
	{
	  int A = ni();
	  int B = ni();
	  
	  int count = 0;
	  
	  int thresh = (B-A)+1;
	  
	  for(int i = 0; i < thresh; ++i)
	  {
	    char buf[1024]={0};
	    int num = foo(A+i);
	    
	    if( !((A+i)-num) )
	    {
	      if(hsqr(num))
	      {
		int j = 1;
		int ticks = 0;
		while(num > 0)
		{		  
		  num -= j;
		  j +=2;
		  ++ticks;
		}
		
		if(0 == num)
		{
		  num = foo(ticks);
		  if( 0 == (num - ticks) )
		  {
		    ++count;
		  }
		}
	      }
	    }
	  }
	
	  printf("Case #%d: %d\n", (k+1), count);
	}
	
	return 0;
}
