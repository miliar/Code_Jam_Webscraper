#include<iostream>
using namespace std;
int chk(int i)  //function for checking palindrome condition
{
	int flag= 0;
	int rem,sum=0,temp;
	temp=i;
	do
	{
		rem=i%10;
		sum=(sum*10)+rem;
		i=i/10;

	}while(i!=0);

	if(temp==sum)
	{
			flag= 1;
			return flag;
	}
}


int chk_pal(int i)  //function for checking palindrome condition
{
	int count;
	int rem,sum=0,temp;
	temp=i;
	do
	{
		rem=i%10;
		sum=(sum*10)+rem;
		i=i/10;

	}while(i!=0);

	if(temp==sum)
	{
		
	int fla = 0;

		long long result = sqrt(static_cast<double>(sum));
		fla = chk(result);

		
		if(fla == 1)
		{

		if ((result * result)== sum) 
		{
			count=1;
			return count;
		}

		}
	}

}
int main()
{
	int palc = 0;
	int m = 1;
	int T;
	cin>>T;
	while(T--)
	{	int cont = 0;
		int beg,end,i;
		
		cin>>beg>>end;

		for(i=beg;i<=end;i++)
		{
			palc = chk_pal(i);
			if(palc==1)
				cont++;
		}
		cout<<"Case #"<<m++<<": "<<cont<<endl;
	}
return 0;
}