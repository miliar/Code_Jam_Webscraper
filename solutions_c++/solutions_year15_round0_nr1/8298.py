#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
int t,i,smax,j,i_friend,stand_person,number;
char digits[1100],c;
scanf("%d",&t);
for(i=0;i<t;i++)
{	i_friend=0;
	stand_person=0;
	scanf("%d",&smax);
	scanf("%s",digits);
	for(j=0;j<=smax;j++)
	{
		c=digits[j];
		number=c-48;
		if(j==0)
			stand_person+=number;
		else
			{
			if(stand_person>=j)
			{
			stand_person+=number;
			}
			else
			{
			i_friend+=(j-stand_person);
			stand_person=j+number;			
			}
			}
	}
	printf("Case #%d: %d \n",i+1,i_friend);	

}
return 0;
}
