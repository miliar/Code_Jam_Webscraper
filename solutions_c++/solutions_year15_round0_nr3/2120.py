#include<string>
#include<stdio.h>
#include<iostream>
#include<stdlib.h>

using namespace std;

int min(int a, int b)
{
	return(a<b?a:b);
}

int cast(char);
int sign(int);
int setf3(int,int);
int m[4][4] = { {1,2,3,4},
				{2,-1,4,-3},
				{3,-4,-1,2},
				{4,3,-2,-1}
			};

int main()
{
	
	int t ;
	scanf("%d",&t);
	int counter = 1;
	while(t--)
	{
		string s;
		int l , x;
		scanf("%d%d",&l,&x);getchar();
		getline(cin,s);
		if(x > 4)
		{
			s = s+s+s+s+s+s+s+s;
		}
		
		int factor = min(8,x);
		int limit = l*factor;
		int *a = (int *) malloc(sizeof(int)*limit);
		int i = 0 ;
		a[0] = cast(s[0]);
		for(i = 1 ; i < limit ; i++)
		{
			a[i] =m[abs(a[i-1])-1][cast(s[i])-1] * sign(a[i-1]);
		}
		int f1 = 0 , f2 = 0 , f3 = 0 ;
		for(i = 0 ; i < limit ; i++)
		{
			if(a[i] == 2)
			{
				f1 = 1 ;
				break ;
			}
		}
		int j ; 
		for(j = i+1 ; j < limit ; j++)
		{
			if(a[j] == 4)
			{
				f2 = 1 ;
				break ;
			}
		}
		
		
		f3 = setf3(a[l-1],x);
		if(f1&&f2&&f3)
		{
			printf("Case #%d: YES\n",counter++);
		}
		else
			printf("Case #%d: NO\n",counter++);		
	}
		  
}

int cast(char a)
{
	if(a == 'i')
		return 2;
	else if(a == 'j' )
		return 3;
	else
		return 4 ;	
}

int sign(int a)
{
	if(a < 0)
		return -1;
	else
		return 1;
}

int setf3(int num , int power)
{
	if(num == 1)
		return 0 ;
	if(num == -1 && (power%2) )
		return 1;
	if(num == -1 && !(power%2))
		return 0 ;
	
	int result ;
	if(!(power%2))
	{
		if((power/2)%2)
		{
			result = 1;
		}
		else 
			result = 0 ;
		return result ;
	}
	else
	{
		return 0;
	}
	
}
