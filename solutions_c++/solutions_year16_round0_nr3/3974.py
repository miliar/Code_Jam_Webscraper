#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
void strev(char *str)
{
    int len = strlen(str);
    int i;
    for (i = 0; i < len/2; i++)
    {
        char temp = str[i];
        str[i] = str[len-i-1];
        str[len-i-1] = temp;
    }
}
long long int isprime(long long int x , long long int *t , long long int jj)
{
	long long int i,j;
	for(i=2 ; i<=sqrt(x) ; i++)
	{
		if(x%i==0)
		{
			t[jj]=i;
			return 0;
		}
	}
	return 1;
}
long long int toDeci(char *str, long long int base)
{
    long long int len = strlen(str);
    long long int power = 1; 
    long long int num = 0; 
    long long int i;
	for (i = len - 1; i >= 0; i--)
    {
        num += (str[i]-'0')* power;
        power = power * base;
    }
    return num;
}
void omDeci(char *res, long long int base, long long int inputNum)
{
    long long int index = 0; 
     while (inputNum > 0)
    {
        res[index++] = (inputNum % base)+48;
        inputNum /= base;
    }
    strev(res);
    res[index] = '\0';
}
int main(){
	long long int tc,n,k,i,j,x,m,count,low,high,inc=1;
	scanf("%lld",&tc);
	while(tc--){
		scanf("%lld%lld",&n,&k);
		low=pow(2,n-1)+1;
		high=pow(2,n)-1;
		count=0;
		printf("Case #%lld:\n",inc++);
		for(i=low ; count<k ; i+=2)
		{
			long long int te[12]={0};
			char bb[100];
			omDeci(bb,2,i);
			for(j=2 ; j<=10 ; j++)
			{
				long long int temp=toDeci(bb,j);
				if(isprime(temp,te,j))
				break;
			}
			if(j==11)
			{
				count++;
				printf("%s ",bb);
				for(j=2 ; j<=10 ; j++)
				printf("%lld ",te[j]);
				printf("\n");
			}
		}
	}
	return 0;
}

