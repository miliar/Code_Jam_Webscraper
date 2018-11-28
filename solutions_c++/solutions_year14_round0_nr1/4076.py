#include<stdio.h>
#include<string>
#include<memory.h>
#include<math.h>
#include<iostream>
#include<istream>
#include <vector>
#include <algorithm>
#define fi(a,b) for( i = a; i < b ; i++ )
#define fj(a,b) for( j = a; j < b ; j++ )
#define fk(a,b) for( k = a; k < b ; k++ )

using namespace std;

typedef vector<int> vi;
typedef vector<char> vc;
//char a[26];
int ri()
	{ int a; 
	  scanf( "%d", &a ); 
	  return a; 
	}
int compare (const void * a, const void * b)
{
  return ( *(int*)b - *(int*)a );
}

int main()
{
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	vc buff;
	vi A,B;
	int i=0, j, k, t=0, r,temp=0,count,match;
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
		A.clear(); B.clear();
		scanf("%d",&r);
		for(j=1; j <= 16; j++)
		{
			scanf("%d",&temp);
			if((r-1)*4 < j && j <= (r*4))
			{
				A.push_back(temp);
			}
		}
		scanf("%d",&r);
		for(j=1; j <= 16; j++)
		{
			scanf("%d",&temp);
			if((r-1)*4 < j && j <=(r*4))
			{
				B.push_back(temp);
			}
		}	
			
			count = 0;
			for(j=0;j<4;j++)
				for(k=0;k<4;k++)
					if(A[j]==B[k])
					{
					count++;
					match=A[j];
					}

			if(count == 1)
				printf("Case #%d: %d\n",i+1,match);
			else if(count == 0)
				printf("Case #%d: %s\n",i+1,"Volunteer cheated!");
			else
				printf("Case #%d: %s\n",i+1,"Bad magician!");
	}
}