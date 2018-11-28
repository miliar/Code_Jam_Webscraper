#include<iostream>
#include<stdio.h>


using namespace std;

int main()
{
	freopen( "input.in", "r", stdin );
	freopen( "output.txt", "w", stdout );
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		int R,C,W;
		cin>>R>>C>>W;
		int rem=C;
		int tries=0;
		while(rem>W)
		{
			tries++;
			rem-=W;
		}
		tries+=W;
		cout<<"Case #"<<i+1<<": "<<tries<<endl;
	}
}