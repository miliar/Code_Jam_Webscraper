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

int minmulDigit(int *digits, int **digitsout, int len)
{
    for (int i = 0; i < len; ++i)
      *digitsout[i]=-1*digits[i];
}

int main()
{
	freopen("B-large.in","rt",stdin);
	freopen("B-large.out","wt",stdout);
	int NCases;
	scanf("%d",&NCases);
	char N[100];int M[100];int length; 
    int idx;
	for (int ii = 0; ii < NCases; ++ii) {
		
		scanf("%s",&N);
		length=strlen(N);
		//printf("%d",length);
		for (int i = 0; i < length; ++i) 
        {
            if (N[i]=='-')M[i]=-1; 
            if (N[i]=='+')M[i]=1;
            //printf("%d",M[i]);
      
        }
 
        idx=0;
        while(length>0)
        {
            if (M[length-1]==-1)
            {
              for (int j = 0; j < length; ++j)
                 M[j]=-1*M[j];
              idx++;

            }
            length--;
           
        }
	

        printf("Case #%d: ",ii+1);
        printf("%d\n",idx);

    }

		
	return 0;
}
