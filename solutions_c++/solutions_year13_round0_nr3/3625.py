
#include <iostream>
#include <cmath>

bool isPali( long double num1)
{
	int digits[20], i=-1, j;
	long long num =num1;
	if(num1!=num)
		return false;

	while(num)
	{
		digits[++i]=num%10;
		num/=10;
	}  
  for(j=0;j<=i;++j,--i)
	  if (digits[i] != digits[j])
		  return false;
  return true;
}

int main(int argc, char *argv[])
{
    int T,Case=0;
	long double A, B, i, count;
    scanf("%d", &T);
    do
    {
       scanf("%lf%lf", &A, &B);	   
       for(i=A,count=0; i<=B ; ++i)
           if( isPali(i) && isPali(sqrt(i)))
			   ++count;

       printf("Case #%d: %.0lf\n", ++Case, count);       
    }while(--T);
}
