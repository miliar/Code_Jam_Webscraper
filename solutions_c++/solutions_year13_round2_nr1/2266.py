#include<stdio.h>
#include<algorithm>
#include<iostream>
#include<string.h>
#include<stdlib.h>
#define loop(i, n) for(i=0; i<n ; i++)
#define FULL 1
#define NOTFULL 0
#define MAX 10
#define DEBUG 1
int i, j, k;
using namespace std;
int func ( int arr[],int a, int i, int n, int count)
{
	if (i<n)
	{
			if ( arr[i]<a)
			{
				a+=arr[i];
				return func( arr, a, i+1, n, count);
			}
			else
			{
				return min( func(arr, a, i+1, n , count +1), func ( arr, 2*a-1, i, n , count+1));
			}
	}
else
	return count;
}
using namespace std;
int main()
{
FILE *f1 = fopen("input1.txt", "r");
FILE *f2 =fopen("ouput1.txt", "w");
int cas=1, t;

fscanf(f1,"%d", &t);
	while (t--)
	{
		int a,  arr[10];
		int n;
		fscanf(f1,"%d%d", &a, &n);

		
		loop(i, n)
		{
			fscanf(f1,"%d", &arr[i]);
		}
		#ifdef DEBUG
		//	printf("%d", a);
		#endif
		if( a==1)
		{
			
			fprintf(f2, "Case #%d: %d\n", cas++, n);
		}
		else
		{
			int count =0;
			sort(arr, arr+n);
			//loop(i, n)
			//{
				//if(a>arr[i])
				//{
				//	a+=arr[i];
				//}
				//else if( arr[i]< 2*a-1)
				//{
					
			           fprintf(f2, "Case #%d: %d\n", cas++, func( arr, a, 0, n,0 ));
				//}
				
			//}
			
			//fprintf(f2, "Case #%d: %d\n", cas++, count);
		}

	}
fclose(f1);
fclose(f2);
}

