/*
TASK: A
LANG: C++
*/
#include <vector>
#include <valarray>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
using namespace std;
typedef long long ll;
typedef long double ld;
#define sz(x) ((int)(x).size())

int getDigit(ll from, int index)
{
   return (from /(int)pow(10.0f,(float)index)) % 10;
}
int sumDigit(int *digits)
{
    int sum=0;
    for (int i = 0; i < 10; ++i)
      sum+=digits[i];
    
    return sum;
}

int main()
{
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
	int NCases;
	int digits[10]={0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
	int digit;
	scanf("%d",&NCases);
	for (int ii = 0; ii < NCases; ++ii) {
		ll N, i, iN, lN; bool loop;
		scanf("%lli",&N);

		if (N==0)
		{
           printf("Case #%d: INSOMNIA\n",ii+1);
        }
        else
        {
            i=1;loop=true;
    		while (loop)
    		{
               iN=i*N;
               lN=(int)floor(log10((float)abs((double)iN))) + 1;
               
               for (int num=0;num<lN;num++)
               {
                  digit=getDigit(iN, num);
                  //printf("digit:%d\n ",digit);
                  if (digits[digit]==0)
                  {
                     digits[digit]=1; 
                     //printf("digits[%d]: %d\n", digit,digits[digit]);
                  }
  
               }
               if (sumDigit(digits)==10)
               {
                  printf("Case #%d: ",ii+1);
                  printf("%lli\n",iN);
                  loop=false;
                  for (int i = 0; i < 10; ++i) digits[i]=0;;
               }
                  		
               i++;               
               
            }
        }

		
	}
	return 0;
}
