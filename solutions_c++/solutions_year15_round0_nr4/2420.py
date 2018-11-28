#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>

using namespace std;

int twoOmino1[2][2] = {{1,1}, {0,0}};
int twoOmino2[2][2] = {{1,0}, {1,0}};
//-------------//
int threeOmino11[3][3] = {
						{1,1,1},
						{0,0,0},
						{0,0,0}};
int threeOmino12[3][3] = {
						{1,0,0}, 
						{1,0,0},
						{1,0,0}};

int threeOmino21[3][3] = {
						{1,1,0}, 
						{0,1,0},
						{0,0,0}};
int threeOmino22[3][3] = {
						{1,1,0}, 
						{1,0,0},
						{0,0,0}};
int threeOmino23[3][3] = {
						{1,0,0}, 
						{1,1,0},
						{0,0,0}};
int threeOmino2[3][3] = {
						{0,1,0}, 
						{1,1,0},
						{0,0,0}};

//-------------//
int fourOmino11[4][4] = {
						{1,1,1,1},
						{0,0,0,0},
						{0,0,0,0},
						{0,0,0,0}};//line
int fourOmino12[4][4] = {
						{1,0,0,0},
						{1,0,0,0},
						{1,0,0,0},
						{1,0,0,0}};//line
//
int fourOmino21[4][4] = {
						{1,1,1,0},
						{0,1,0,0},
						{0,0,0,0},
						{0,0,0,0}};
int fourOmino22[4][4] = {
						{0,1,0,0},
						{1,1,0,0},
						{0,1,0,0},
						{0,0,0,0}};
int fourOmino23[4][4] = {
						{1,0,0,0},
						{1,1,0,0},
						{1,0,0,0},
						{0,0,0,0}};
int fourOmino24[4][4] = {
						{0,1,0,0},
						{1,1,1,0},
						{0,0,0,0},
						{0,0,0,0}};

//---------
int fourOmino31[4][4] = {
						{1,1,0,0},
						{1,0,0,0},
						{1,0,0,0},
						{0,0,0,0}};
int fourOmino32[4][4] = {
						{1,0,0,0},
						{1,0,0,0},
						{1,1,0,0},
						{0,0,0,0}};
int fourOmino33[4][4] = {
						{1,1,0,0},
						{0,1,0,0},
						{0,1,0,0},
						{0,0,0,0}};
int fourOmino34[4][4] = {
						{0,1,0,0},
						{0,1,0,0},
						{1,1,0,0},
						{0,0,0,0}};
int fourOmino35[4][4] = {
						{1,1,1,0},
						{1,0,0,0},
						{0,0,0,0},
						{0,0,0,0}};
int fourOmino36[4][4] = {
						{1,1,1,0},
						{0,0,1,0},
						{0,0,0,0},
						{0,0,0,0}};
int fourOmino37[4][4] = {
						{1,0,0,0},
						{1,1,1,0},
						{0,0,0,0},
						{0,0,0,0}};
int fourOmino38[4][4] = {
						{0,0,1,0},
						{1,1,1,0},
						{0,0,0,0},
						{0,0,0,0}};
//
int fourOmino41[4][4] = {
						{0,1,0,0},
						{1,1,0,0},
						{1,0,0,0},
						{0,0,0,0}};
int fourOmino42[4][4] = {
						{1,1,0,0},
						{0,1,1,0},
						{0,0,0,0},
						{0,0,0,0}};
int fourOmino43[4][4] = {
						{1,0,0,0},
						{1,1,0,0},
						{0,1,0,0},
						{0,0,0,0}};
int fourOmino44[4][4] = {
						{0,1,1,0},
						{1,1,0,0},
						{0,0,0,0},
						{0,0,0,0}};
//

int fourOmino51[4][4] = {
						{1,1,0,0},
						{1,1,0,0},
						{0,0,0,0},
{0,0,0,0}};
//
void initGrid(int **grid, int R, int C)
{
	for(int i=0; i<R; i++)
		for(int j=0; j<C; j++)
			grid[i][j] = 0;
}

int main()
{
	//ifstream in("A-small-attempt2.in");
	//ofstream out("A-small-attempt2.out");
	ifstream in("D-small-attempt2.in");
	ofstream cout("D-small-attempt2.out");

	int T;
	in>>T;
	int i=0;
	while(i<T)
	{
		int X, R, C;
		in>>X>>R>>C;
		if(X==1)
		{
			cout<<"Case #"<<i+1<<": "<<"GABRIEL"<<endl;
			i++;
			continue;
		}
		int **grid = new int*[R];
		for(int j=0; j<R; j++)
		{
			grid[j] = new int[C];			
		}

		initGrid(grid, R, C);
		
		if(X==2)
		{
			if((R*C)%2 == 0)
				cout<<"Case #"<<i+1<<": "<<"GABRIEL"<<endl;
			else
				cout<<"Case #"<<i+1<<": "<<"RICHARD"<<endl;
		}
		else if(X==3)
		{
			if(X >= R*C || R*C == 8 || R*C == 16 || R*C == 4)
				cout<<"Case #"<<i+1<<": "<<"RICHARD"<<endl;
			else if(R*C == 6 || R*C==12 || R*C == 9 )
				cout<<"Case #"<<i+1<<": "<<"GABRIEL"<<endl;
		}
		else if(X==4)
		{
			if(X >= R*C)
				cout<<"Case #"<<i+1<<": "<<"RICHARD"<<endl;
			else if(R*C == 12 || R*C == 16)
				cout<<"Case #"<<i+1<<": "<<"GABRIEL"<<endl;
			else
				cout<<"Case #"<<i+1<<": "<<"RICHARD"<<endl;

		}
		
		

		i++;
	}


	//system("pause");
	return 0;
}