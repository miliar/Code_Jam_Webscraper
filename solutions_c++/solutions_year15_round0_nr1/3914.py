#include <stdio.h>
#include <string>
#include <iostream>
#include <stdlib.h> 

using namespace std;

int toInt(char c)
{
	return c-'0'; 
}

int main(void) {
	
	//freopen("A-small-attempt3.in", "rt", stdin);
	//freopen("A-small-attempt3.out", "wt", stdout);
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);
	
	int T, s, f, sum;
	string d;
	
	scanf("%d\n", &T);
	
	for(int i=0; i<T; i++)
	{	
		printf("Case #%d: ", i+1);
		
		scanf("%d\n", &s);
		getline(cin,d);
		
		sum = toInt(d[0]);
		f = 0;
		
		for(int j=1; j<s+1; j++)
		{				
			if( j > sum && toInt(d[j])>0 )
			{
				f += j-sum;
				sum += j-sum;
			}	
			sum += toInt(d[j]);
		}		
		printf("%d\n", f);
	}
    return 0;
}

