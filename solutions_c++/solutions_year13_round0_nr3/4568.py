#include<stdio.h>
#include<iostream.h>
#include<conio.h>

#define maximum 100
float pal[maximum],count=0,count_final;


void chk_pal(long long i)
{
	long long rem,sum=0,temp;
	temp=i;
	while(i)
	{
	rem=i%10;
	sum=(sum*10)+rem;
	i=i/10;
	}
	if(temp==sum)
	{       pal[count]=sum;
		count++;
	}
}

int checkPalindrome(long long num)
{
    long long r = 0,temp=num;
    while(temp !=0)
   {
	r = r *10;
	r = r + temp%10;
	temp=temp/10;

    }
    if(num == r)
       return 1;
    return 0;
}

void main()
{  	clrscr();
	float beg,end,i,number,c,c1[maximum]={0};
	cin>>number;

	for(i=1;i<=100;i++)
		chk_pal(i);

	for(long long a=1;a<=number;a++)
	{  cin>>beg>>end;
	   for(i=0;i<count;i++)
	    {   c=pal[i]*pal[i];
		if(checkPalindrome(c))
		       if((beg<=c)&&(end>=c))
			    count_final++;
	    }

	   c1[a]=count_final;
	   count_final=0;
	}
	for(long long m=1;m<=number;m++)
		cout<<"Case #"<<m<<": "<<c1[m]<<endl;

}
