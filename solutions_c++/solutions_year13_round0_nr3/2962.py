#include <stdio.h>
#include <memory.h>
#include <limits.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <list>
#include <map>

using namespace std;



int T;
char tempA[110],tempB[110];
int A;
int B;


bool pal(int number)
{
	//printf("testP");
	int cnt = 0;
	int digit[100];
	//printf("Number: %d\n",number);
	while(number!=0)
	{
		digit[cnt++] = number%10;
		number/=10;
	}
	int j = cnt-1;
	int i = 0;
	while(i < j)
	{
		if(digit[i] != digit[j])
			return false;
		i++;
		j--;
	}
	return true;
}

int isSquare(int number)
{
	//printf("testS");
	int l = 0,h = number,m;
	while(l < h)
	{
		m = (l+h+1)/2;
		//printf("%d %d %d",l,h,m);
		if(m*m == number)
			return m;
		if(m*m < number)
		{
			l = m+1;
		}
		if(m*m > number)
		{
			h = m-1;
		}
	}
	if(l*l == number)
		return l;
	return -1;

}


int main()
{
	scanf("%d",&T);
	for(int i = 0; i<  T;i++)
	{
		//printf("\ntry\n");
		scanf("%d %d",&A,&B);
		int result=0;
		for(int j = A;j <= B;j++)
		{
			//printf("j:%d\n",j);
				if(pal(j))
				{
					int temp = isSquare(j);
					if(temp != -1)
					{
						if(pal(temp))
							result++;
					}
							//printf("%d\n",j);
				}		
					
		}
		
		printf("Case #%d: %d\n",i+1,result);
		
	}
	return 0;
}

