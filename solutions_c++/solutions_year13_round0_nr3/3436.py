#include <iostream>
#include <cstdio>
#include <algorithm>
#include <complex>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <cstdlib>
#include <memory.h>
#include <iostream>
#include<list>
using namespace std;

#define pb push_back
#define sz size()
#define mp make_pair
#define mset(ar,val) memset(ar,val,sizeof ar)
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
static inline bool is_palindrome(int orig)
{
  int reversed = 0, n = orig;
  while (n > 0)
  {
    reversed = reversed * 10 + n % 10;
    n /= 10;
  }
  return orig == reversed;
}
int main() {
	int T,A,B,t,i,count,num;
	int startingpt,endingpt;
	cin>>T;
	for(t=1;t<=T;++t){
		count=0;
		cin>>A>>B;
		startingpt=sqrt(A);
		endingpt=sqrt(B);
		for(i=startingpt;i<=endingpt;++i){
			num=pow(i,2);
			if(is_palindrome(num)&&is_palindrome(i) && num<=B && num>=A)
				++count;
		}
		printf("Case #%d: %d\n",t,count);

	}
	return 0;
}

