#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int a[4][4][4]={{{1,0,0,0},
	{1,1,0,0},
	{1,0,0,0},
	{1,1,0,0}},

	{{1,1,0,0},
	{1,1,0,0},
	{1,1,1,0},
	{1,1,0,0}},

	{{1,0,0,0},
	{1,1,1,0},
	{1,0,1,0},
	{1,1,1,1}},

	{{1,1,0,0},
	{1,1,0,0},
	{1,1,1,1},
	{1,1,0,1}}};
	
	long long int x,r,c,z,t;
	
	
	cin>>t;
	
	
	for(z=1;z<=t;z++)
	{
		cin>>x>>r>>c;
		if(a[r-1][c-1][x-1]==1)
		{
			cout<<"Case #"<<z<<": GABRIEL\n";
		}
		else
		{
			cout<<"Case #"<<z<<": RICHARD\n";
		}

	}


	return 0;
}