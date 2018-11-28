#include <iostream>
using namespace std;

int main ()
{

	int lk[4][4][4]={{{1,0,0,0},
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
	int test;
	cin>>test;
	int x,r,c;
	int j=1;
	while(test--)
	{
		cin>>x>>r>>c;
		if(lk[r-1][c-1][x-1]==1)
		{
			cout<<"Case #"<<j++<<": GABRIEL\n";
		}
		else
		{
			cout<<"Case #"<<j++<<": RICHARD\n";
		}

	}



	return 0;
}