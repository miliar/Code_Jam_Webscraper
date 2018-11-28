#include <stdio.h>
#include <math.h>
int q[9];
long long int conv(long long  int a);
long long int convert(int base, long long int num);
long long int check(int i, long long int num1);
int main(void){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("output_file_name.out","w",stdout);
	int t;
	scanf("%d",&t);
	int n, j, cj=0;
	scanf("%d%d",&n,&j);
	printf("Case #1:\n");
	long long int num=0,i , ch;
	i=n-1;
	while(i>=0){
		num = num + pow(2,i);
		i--;
	}
	while(cj < j){
		long long int num0 = num;
		num0 = conv(num0);
		for(i = 2; i<=10; i++){
			long long int num1 = convert( i, num0);
			ch = check(i, num1);
			if(ch == 0){
				break;
			}
		}
		if(ch == 1){
			printf("%lld", num0);
			for(i = 0; i < 9; i++ ){
				printf(" %d", q[i]);
			}
			cj++;
			printf("\n");
		}
		num = num -2;
	}
}
 
long long int conv(long long int a){
	long long int b;
	b = a;
	int c, i=0;
	while(b>0){
		c = pow(2,i);
		b = a / c;
		i++;
	}
	c = pow(2 , i-1);
	long long int d=0,e;
	e = a;
	while(c>0){
		if(c <= e){
			e = e -c;
			d = d*10 +1;
		}
		else if(c > e){
			d = d*10;
		}
		c = c/2;
	}
	return d;
} 

long long int convert(int i, long long int num0){
	long long int num, num1 = 0;
	int j = 0;
	num = num0;
	while(num > 0){
		int c = num %10;
		num1 = num1 + c * pow(i, j);
		num = num / 10;
		j++;
		
	}
	return num1;
}
long long int check(int i, long long int num1){
	long long int sq, x = 3;
	if(num1 % 2 == 0){
		q[i-2] = 2;
		return 1;
	}
	else if(num1 % 3 == 0){
		q[i-2] = 3;
		return 1;
	}
	sq = sqrt(num1);	
	while(1)
	{
		if( num1 % x == 0)
		{
			q[i-2] = x;
			return 1;
		}	
		x = x + 2;
		if(x > sq)
		{
			return 0;
		}
		if(x % 3 == 0){
			x = x + 2;
		}
	}
}

