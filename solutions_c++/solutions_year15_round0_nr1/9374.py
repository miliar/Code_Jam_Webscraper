#include <stdio.h>
#include <string.h>
#include <cstdio>
#include <math.h>
#include <stdlib.h>
using namespace std;


#define maxT 100
#define Smax 1002
// 1000

#define toDigit(c) (c-'0')
// char c = ppl[k] ; // = '1';
// int i = c - '0';  // i is now equal to 1, not '1'

void printarray (int arg[], int length) {
  for (int n=0; n<length; ++n)
    printf("Case #%d: %d\n", n+1, arg[n]);
}

int main(void)
{
	freopen("A-large.in", "r", stdin);
    freopen("A-large2.out", "w", stdout);


    int T; //1<=T<=100
    int res[maxT];
    int s;
    char ppl[Smax];
    
    //cin >> T;
	scanf("%d", &T);

    for(int c= 0; c<T; c++)
    {
         scanf("%d", &s);
         scanf("%s", ppl); 
		 
		 int observed=0;
		 //int expected=0;
		 int needed =0;

		 int x= toDigit(ppl[0]);
		 observed += x;
		 //if(x==0)  needed++;
		 //expected = observed+ needed;

		 for(int k= 1; k<=s; k++)
		 {
			 if((observed +needed) < k )
			 {
				needed++;
			 }

			 x = toDigit(ppl[k]) ;
			 //expected++;
			 observed += x;

		 }

         res[c] = needed; 
    }

	//-----------------------
	//cout<< "----------------";
    //cout << T;

    printarray(res, T);

	//getchar();

    return 0;
}