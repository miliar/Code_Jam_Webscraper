#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
//#include <iomanip> 
using namespace std;
//#define LARGE

 //bool isPrime(int number)
 // {
 //   int i;
 //    for (i=2; i<number; i++)
 //    { 
	//	 if(number% i==0)
 //      return false;
 //   }
	// return true;

 // }
   

int main() 
{
#if 1
#ifndef LARGE
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
#else
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
#endif
#endif
	int T,row1,row2;
	long unsigned int count=0;
	
	int A,B,K;
	int temp;
	
	
	scanf("%d", &T);

	for (int V = 1; V <= T; ++V) 
	{
	  count=0;
	  cin>>A;
	  cin>>B;
	  cin>>K;
	

	  for (int i = 0; i<A;i++) 
	  {
		  //if(isPrime(i))
		  {
				for (int j = 0; j<B;j++) 
				{
					//if(isPrime(j))
					{
						temp = i&j;
						if(temp<K)
							count++;
					}
		
				}
		  }
	  }

	  printf("Case #%d: %ld\n", V,count);
	  
	}
	return 0;
}
