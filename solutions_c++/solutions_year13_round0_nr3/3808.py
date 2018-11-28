#include<iostream>
#include<math.h>

using namespace std;
int pal(int i)
{
	int rem,num,sum=0;
	num=i;
	while(num!=0)
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

int perfect(int n)
{
	//double xp=sqrt((double)n);
    if(double(int(sqrt(n)))==sqrt(n))
        return 1;//return 1;
    else
        return 0;

}
int sqroot(int i)
{
	if(pal(i) && perfect(i) )
		if(pal(sqrt(i)))
			return 1;
	else
		return 0;

}
int main()
{
	int l,test=1;
	int a,b;
	int count=0,i;
	cin>>l;
	while(test<=l)
	{
		count=0;
		cin>>a>>b;
		for(i=a;i<=b;i++)
			if(sqroot(i))
				count++;
		cout<<"Case #"<<test<<": "<<count;
		cout<<"\n";
		test++;
	}

}
