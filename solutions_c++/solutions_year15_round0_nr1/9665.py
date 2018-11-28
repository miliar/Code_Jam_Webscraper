#include<bits/stdc++.h>
inline long long int power(long long int a, long long int b)
{
	long long int prod=1;
	while(b--)
	{
		prod=prod*a;
	}
	return prod;
}
using namespace std;
int main ()
{
    int t;
    cin>>t;
    int count=1;
    while(t--)
	{
        string str;
        int sum=0,mini=0,min1=0,str_length=0;
        cin>>str_length>>str;;
		for(int i=0;i<=str_length-1;i++)
		{
			sum=sum+str[i]-48;
			if(sum<i+1)
                mini=i+1-sum;
			min1=max(mini,min1);
		}
		cout<<"Case #"<<count<<": "<<min1<<"\n";;
		count=count+1;
	}
	return 0;
}
