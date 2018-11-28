#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<stdio.h>

bool digits[10];

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int T;
	bool ch;
	cin>>T;
	long long number;
	long long number1;
	long long tmp;
	for(int t=1; t<=T; t++)
	{
		cin>>number;
		if(number==0)
		{
			cout<<"Case #"<<t<<": INSOMNIA\n";
			continue;
		}
		number1=number;
		while(true)
		{
			ch=true;
			tmp=number1;
			while(tmp!=0)
			{
				digits[tmp%10]=true;
				tmp/=10;
			}
			number1+=number;
			for(int i=0; i<10; i++)
				if(!digits[i]) ch=false;
			if(ch) break;
		}
		for(int i=0; i<10; i++) digits[i]=false;
		cout<<"Case #"<<t<<": "<<number1-number<<endl;
	}
	return 0;
}
