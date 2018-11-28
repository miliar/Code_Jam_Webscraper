#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
#include <string>
#define BSIZE 1<<15
using namespace std;
char buffer[BSIZE];
long bpos = 0L, bsize = 0L;
long readLong() 
{
	long d = 0L, x = 0L;
	char c;
	while (1)  {
		if (bpos >= bsize) {
			bpos = 0;
			if (feof(stdin)) return x;
			bsize = fread(buffer, 1, BSIZE, stdin);
		}
		c = buffer[bpos++];
		if (c >= '0' && c <= '9') { x = x*10 + (c-'0'); d = 1; }
		else if (d == 1) return x;
	}
	return -1;
}

void solver()
{
  int A,B,C;
  cin>>A>>B>>C;
 int result=0;
 for(int c=0;c<C;c++)
 {
  for(int a=0;a<A;a++)
    for(int b=0;b<B;b++)
      if((a&b) ==c)
	{
	  result++;
	}
 }
 cout<<result<<endl;
}
int main()
{
  int testcases;//=readLong();
  cin>>testcases;
  for(int i=0;i<testcases;i++)
  {
    printf("Case #%d: ",i+1);
    solver();
  }
  return 0;
}
