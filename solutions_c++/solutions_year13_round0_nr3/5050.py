#include<iostream>
#include<cstdio>
using namespace std;

int main() 
{
	int x[] = {1, 4, 9, 121, 484};
    int t, a, b, i, j, count;
	cin>>t;
	for(i = 1; i <= t; i++) 
	{	
		cin>>a >>b;
		count = 0;
		for(j = 0; j < 5; j++) 
		{
			if(x[j] >= a && x[j] <= b)
			{
				count ++;
			}
		}
		cout<<"Case #"<<i<<": "<<count<<"\n";
	}
	return 0;
}