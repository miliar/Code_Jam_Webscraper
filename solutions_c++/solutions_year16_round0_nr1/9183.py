#include<stdio.h>
#include<string.h>
#include<stdbool.h>
#include <cassert>


bool isInArray(int val, int *arr, int size){
    int i;
    for (i=0; i < size; i++) {
        if (arr[i] == val)
            return true;
    }
    return false;
}
                     

int main()
{
	int num = 0,digit = 0,c = 0,a[11],b[100],n,n1,t=0;
	FILE *fin = freopen("A-large.in", "r", stdin);
     assert( fin!=NULL );
     FILE *fout = freopen("A-large.out", "w", stdout);
	
	scanf("%d",&t);
	for(int j = 0; j < t; j++){
		scanf("%d",&num);
		n = num;
		
	if(n > 0){
	for(int i = 1;; i++)
	{
	num = n * i;
	while(num != 0)
	{
		digit = num % 10;
	
		if(!isInArray(digit,b,c+1))
		{
			c++;
			b[c] = digit;
		}

	if(num > 9)
		num /= 10;
	else 
		num  = 0;
	}
	if(c>9)
	{
		printf("Case #%d: %d\n",1 + j,n * i);
		c = 0;
		for(int k = 0; k < 50; k++)
			b[k] = 89349;
		break;
	}
	}
}
else
	printf("Case #%d: INSOMNIA\n",j + 1);

	
}
	
}


