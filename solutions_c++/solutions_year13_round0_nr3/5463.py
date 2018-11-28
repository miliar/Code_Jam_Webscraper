#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;

int palindrome(int num)
{
int r,sum=0,temp;



    temp=num;
    while(num){
         r=num%10;
         num=num/10;
         sum=sum*10+r;
    }
    if(temp==sum)
         return 1;
    else
	return 0;
}


int main()
{
int t;
	int i,j,a,b;
	int A,B;
	int cnt=0;
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
		cnt=0;
		scanf("%d%d",&a,&b);
		A= (int)ceil(sqrt(double(a)));
		B= (int)floor(sqrt(double(b)));
		//printf("A=%d\n",A);	
		//printf("B=%d\n",B);	
		for(j=A;j<=B;j++)
		{	
			if(palindrome(j*j) && palindrome(j)  )
			{
			//printf("num=%d\n",j);	
			cnt++;
			}
		}
		
		
		printf("Case #%d: ",i+1);	
		printf("%d\n",cnt);	







	}







return 0;
}
