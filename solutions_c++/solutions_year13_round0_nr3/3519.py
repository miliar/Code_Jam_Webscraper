#include<iostream>
#include<math.h>

using namespace std;
int palin(int i)
{
	int rem,num,sum=0;
	num=i;
	while(num!=0)    //Loop to reverse the number.
    {
        rem=num%10;
        num=num/10;
        sum=sum*10+rem;
    }

    if(sum==i)
    	return 1;
    else
    	return 0;
}

int is_perfect(int n)
{
	//double xp=sqrt((double)n);
    if(double(int(sqrt(n)))==sqrt(n))
        return 1;//return 1;
    else
        return 0;

}
int sq_palin(int i)
{
	if(palin(i) && is_perfect(i) )
		if(palin(sqrt(i)))
			return 1;
	else
		return 0;

}
int main()
{
	int t,test=1;
	int a,b,count=0,i;
	cin>>t;
	while(test<=t)
	{
		count=0;
		cin>>a>>b;
		for(i=a;i<=b;i++)
			if(sq_palin(i))
				count++;
		cout<<"Case #"<<test<<": "<<count;
		cout<<'\n';
		test++;
	}

}
