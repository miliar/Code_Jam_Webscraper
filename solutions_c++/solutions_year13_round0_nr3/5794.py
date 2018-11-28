#include<iostream>
#include<cmath>
using namespace std;

int T;
int A,B;
int x=1;
int f_and_s_num;
bool is_fair(int value);
bool is_square(int value);
bool is_fair_and_square(int value);

int main()
{
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		cin>>A>>B;
		f_and_s_num=0;
		for(int j=A;j<=B;j++)
		{			
			if(is_fair_and_square(j))
			{
				f_and_s_num++;
			}
		}
		cout<<"Case #"<<i<<": "<<f_and_s_num<<endl;
	}
	return 0;
}

bool is_fair(int value)
{
	int tempValue=value;
	int reverse=0;
	int mod;
	int i=1;
	while(value!=0)
	{
		reverse*=10;
		mod=value%10;
		reverse += mod*i;
		value=(value-mod)/10;
	}
	if(reverse == tempValue)
	{
		return true;
	}
	else
	{
		return false;
	}
}

bool is_square(int value)
{
	if(value==(int)sqrt((double)value)*(int)sqrt((double)value))
	{
		return true;
	}
	return false;
}

int get_square(int value)
{
	return sqrt((double)value);
}

bool is_fair_and_square(int value)
{
	if(is_square(value))
	{
		if(is_fair(value) && is_fair(get_square(value)))
		{
			return true;
		}
	}
	return false;
	
}