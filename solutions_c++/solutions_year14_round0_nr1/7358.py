// 

#define _CRT_SECURE_NO_WARNINGS 
#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <cmath>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <map>
#include <queue>
#include <set>
#include <queue>
#include <stack>
#include <deque>
#include <assert.h>
#include <ctime>
#include <bitset>
#include <numeric>
#include <complex>

using namespace std ;

int main()
{
	freopen("A-S.in","r",stdin);
    freopen("A-S.out","w",stdout);


	int t , count = 1 ;
	scanf("%d",&t);

	while(t--)
	{
		int arr[4][4] ; 
		int arr16 [17] = {} ;
		int r , r2 ; 
		scanf("%d",&r) ;
		for(int i = 0 ; i < 4 ; ++i)
			for(int j = 0 ; j < 4 ; ++j)
			{
				scanf("%d",&arr[i][j]);
				if(i==r-1)
					arr16[arr[i][j]]++ ;
			}

		scanf("%d",&r2) ;
		for(int i = 0 ; i < 4 ; ++i)
			for(int j = 0 ; j < 4 ; ++j)
			{
				scanf("%d",&arr[i][j]);
				if(i==r2-1)
					arr16[arr[i][j]]++;
			}

		int a = 0  , k ;

		for( int i = 1 ; i < 17 ; ++i)
			if(arr16[i]==2)
				a++ , k = i ;
		
		if(a==1)
			printf("Case #%d: %d\n",count++ , k);
		else if(a>1)
			printf("Case #%d: Bad magician!\n",count++);
		else
			printf("Case #%d: Volunteer cheated!\n",count++);
	}
}