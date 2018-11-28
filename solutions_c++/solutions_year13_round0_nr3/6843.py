#include <stdio.h>
#include <math.h>
#include <iostream>
#include <algorithm>
#include <iosfwd>
#include <vector>
#include <map>
#include <set>
#include <string.h>
using namespace std;

bool IsPalindrome(int n)
{
	int res = 0;
	int _n = n;
	if(n<0)
		return false;
	do 
	{
		res = res*10+_n%10;
		_n /=10;
	} while (_n);
	if(res == n)
		return true;
	return false;
}

int main()
{
	//FILE *f=fopen("result.txt","w+");

	int t,_t = 1;
	scanf("%d",&t);
	int n,a,b;
	int _a,_b;
	while(t--)
	{
		n=0;
		scanf("%d%d",&a,&b);
		_a = sqrt((double)a);
		_b = sqrt((double)b);
		if(_a*_a < a)
			_a++;
		//if((_b+1)*(_b+1) > b)
		//	_b++;
		for(int i = _a; i<=_b;i++)
		{
			if(IsPalindrome(i))
			{
				if(IsPalindrome(i*i))
					n++;
			}
		}
		printf("Case #%d: %d\n",_t++,n);
		//fprintf(f,"Case #%d: %d\n",_t++,n);
	}
	//fclose(f);
}
