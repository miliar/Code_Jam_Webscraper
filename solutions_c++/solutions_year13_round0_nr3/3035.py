#include<iostream>
#include<cmath>
using namespace std;

long long int first_palin(long long int a);
long long int next_palin(long long int a);
bool is_palin(long long int a);
int num_digits(long long int a);
long long int rev(long long int a);

int main()
{
	int T;
	cin>>T;
	long long int A,B,a,b,count;
	for(int I=1;I<=T;I++)
	{
		count=0;
		cin>>A>>B;
		a=(sqrt(A)-int(sqrt(A)))>0?int(sqrt(A))+1:int(sqrt(A));
		b=int(sqrt(B));
	//	if(I==97)cout<<"****ERROR***"<<sqrt(A)-int(sqrt(A))<<endl;
		//cout<<A<<"("<<a<<")"<<"-"<<B<<" : ";
		a=first_palin(a);
//	cout<<a<<"-"<<b<<"("<<a*a<<","<<b*b<<")"<<endl;
		while(a<=b)
		{
					if(is_palin(pow(a,2))){count++;}//cout<<a<<","<<pow(a,2)<<endl;
					a=next_palin(a);
		}
		
		cout<<"Case #"<<I<<": "<<count<<endl;
		
	}

return 0;
}
long long int rev(long long int a)
{
				long long int ret=0;
				while(a)
				{
								ret= (ret*10) + a%10;
								a=a/10;
				}
				return ret;
}
long long int first_palin(long long int a)
{
			int a_dig = num_digits(a);
			int odd_flag;
			long long int s, ret;
			if(a_dig % 2 ==0 )
			{
				s= a/(pow(10,(a_dig/2)));
				odd_flag=0;
			}
			else
			{
				if(a_dig==1) s=a;
				else s= a/pow(10,((a_dig+1)/2)-1);
				odd_flag=1;
			}
			
			if(odd_flag)
			{
						if(num_digits(s)==1)ret = s;
						else ret = (s*(pow(10,(num_digits(s)-1))))+rev(s/10);
			}         
			else
			{
				ret = (s*(pow(10,(num_digits(s)))))+rev(s);
			}
			if (ret<a) return next_palin(ret);
			else return ret;
}




long long int next_palin(long long int a)
{
			int a_dig=num_digits(a), odd_flag;
			long long int s,ret;
			if(a_dig % 2 ==0 )
			{
				s= a/(pow(10,(a_dig/2)));
				odd_flag=0;
			}
			else
			{
				if(a_dig==1) s=a;
				else s= a/pow(10,((a_dig+1)/2)-1);
				odd_flag=1;
			}
			
			if(num_digits(s+1)==num_digits(s))
			{
					s = s+1;
			}
			else
			{
					s =s+1;
					odd_flag=(odd_flag+1)%2;
					if(odd_flag == 0)
					{
						s=s/10;
					}
			}
			
			if(odd_flag)
			{
						if(num_digits(s)==1)ret = s;
						else ret = (s*(pow(10,(num_digits(s)-1))))+rev(s/10);
			}         
			else
			{
				ret = (s*(pow(10,(num_digits(s)))))+rev(s);
			}
			return ret;

}

bool is_palin(long long int a)
{
		int a_dig=num_digits(a);
		while(num_digits(a)>1)
		{
				if(a%10 != a/int((pow(10,a_dig-1))))
				{
						return false;
				}
				else
				{
						a=a%int(pow(10,a_dig-1));
						a=a/10;
						a_dig-=2;
				}
				
		}
		return true;
}

int num_digits(long long int a)
{
						int dig=0;
						while(a)
						{
								dig++;
								a=a/10;
						}
						return dig;
}
