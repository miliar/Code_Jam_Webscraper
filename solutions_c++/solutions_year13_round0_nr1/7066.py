#include<iostream>
#include<math.h>
using namespace std;
int Reverse(int num)
{
	int rem=0,rev=0;
	while(num!=0)
	{
		rem=num%10;
		num=num/10;
		rev=rev*10+rem;
	}
	return rev;
}
bool is_perfect_square(int n) 
{
    if (n < 0)
        return false;
    int root(round(sqrt(n)));
    return n == root * root;
}
int main()
{
	int i,j,k,test_case,num,reverse1,sqrt_n,n,num1,perfect,reverse2,output[10000],count=0;
	cin>>test_case;
	for(i=0;i<test_case;i++)
	{
	count=0;
	cin>>num>>num1;
	for(n=num;n<=num1;n++)
	{
		reverse1=Reverse(n);		
		if(n==reverse1)
		{
			sqrt_n=sqrt(n);
			perfect=is_perfect_square(n);
			if(perfect)
			{
				reverse2=Reverse(sqrt_n);
				if(sqrt_n==reverse2)
					count++;
			}
		}
	}
	output[i]=count;
	} 
	for(i=0;i<test_case;i++)
		cout<<"\nCase #"<<i+1<<": "<<output[i];
}
