#include <iostream>
#include <cstdio>
#include <string.h>


using namespace std;
//**** Declare your data ********

int grid1[4][4]={0};
int grid2[4][4]={0};

int ans1=0;
int ans2=0;

int count=0;
int column=0;

int card=0;

// **** Initialize your data
void initialize()
{
	memset(grid1,0,16*sizeof( int));
	memset(grid2,0,16*sizeof( int));
	// emptysq = 0;

};
// *** Solver function
int run()	
{
	cin>>ans1;
	--ans1;
	for (int i = 0; i < 4; ++i)
	{
		for (int j = 0; j < 4; ++j)
		{
			cin>>grid1[i][j];
		}
	}
	cin>>ans2;
	--ans2;
	for (int i = 0; i < 4; ++i)
	{
		for (int j = 0; j < 4; ++j)
		{
			cin>>grid2[i][j];
		}
	}
	count=0;
	column=0;
	for (int i = 0; i < 4; ++i)
	{
		for (int j = 0; j < 4; ++j)
		{
			if(grid1[ans1][i]==grid2[ans2][j])
			{
				++count;
				column=i;
			}
		}
	}
	if(count==0)
		return 0;
	else if(count==1)
		return grid1[ans1][column];
	else 
		return 20;
	
}
void solve_case(int test_case)
{
	initialize();

	// **** call solver function
	card=run();
	
	// *** print output
	if(card==0)
		cout<<"Case #"<<test_case<<": "<<"Volunteer cheated!"<<endl;
	else if(card>16)
		cout<<"Case #"<<test_case<<": "<<"Bad magician!"<<endl;
	else 
		cout<<"Case #"<<test_case<<": "<<card<<endl;
		return;


};

int main()
{
	freopen("aa.in","r",stdin);
	freopen("a.out","w",stdout);
	initialize();
	int T; scanf("%d", &T);

	for (int tc = 1; tc <= T; tc++)
		solve_case(tc);

	return 0;
}
