#include<iostream>
#include<stdio.h>
#include<algorithm>

using namespace std;

int main(void)
{
	freopen("C:/stream/A-small-ichi.in", "r", stdin);
	freopen("C:/stream/A-small-ichi.out", "w", stdout);

    long long int R, t, add, counter;
	long long int T;

    counter = 0;
	cin>>T;


	while(T--)
	{
		cin>>R>>t;
		add = 0;

		counter++;

		long long int j = 0;

		for(long long int i = R; add <= t; i+=2, j++)
		{
			add += (2*i + 1);
		}
		cout<<"Case #"<<counter<<": "<<j-1<<endl;
	}
}
