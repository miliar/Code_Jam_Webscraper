#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;

vector<int> number;
vector<int> rnumber;

//int count;

int palindrome( int n)
{
	number.clear();
	rnumber.clear();
	 int num = n;
	while(num>0)
	{
		number.push_back(num%10);
		rnumber.push_back(num%10);
		num=( int) num/10;
	}
	
	reverse(rnumber.begin(), rnumber.end());
	
	if(number==rnumber)
		return 1;
		
	
	else
		return -1;

}


int square( int n)
{
	
	float s = sqrt(n);
	int s1 = sqrt(n);
	//cout<<"S+==="<<s<<endl;
	if(s==s1)
	{
		int ck = palindrome(s);
		if(ck==1)
			return 1;
		else
			return -1;
	}
}


int main()
{
	
	freopen("input.in", "r", stdin);
	freopen("output.in", "w", stdout);
	
	int m;
	cin>>m;
	
	int i=1;
	
	while(i<=m)
	{
	
		int count =0;
		int a;
		int b;
		
		cin>>a;
		cin>>b;
		
		//long long int n = 676;
		for(int j=a; j<=b; j++)
		{
				
			int ch = palindrome(j);
			if(ch==1)
			{
				//cout<<"inside!!";
				int ck = square(j);
				if(ck==1)
					count++;
			
			}
	
		}
		
		cout<<"Case #"<<i<<": "<<count<<endl;
		i++;
	}
}		
	
	
