#include<iostream>
#include<fstream>
using namespace std;
int mat[4][4][4]={
			{{1,1,1,1},{1,1,1,1},{1,1,1,1},{1,1,1,1}},
			{{0,1,0,1},{1,1,1,1},{0,1,0,1},{1,1,1,1}},
			{{0,0,0,0},{0,0,1,0},{0,1,1,1},{0,0,1,0}},
		        {{0,0,0,0},{0,0,0,0},{0,0,0,1},{0,0,1,1}}
		 };
int main()
{
ifstream in("inp.txt");
ofstream op("op.txt");
int t;
in>>t;
for(int i=1;i<=t;i++)
{
int x,r,c;
in>>x>>r>>c;
op<<"Case #"<<i<<": "<<(mat[x-1][r-1][c-1]==1?"GABRIEL":"RICHARD")<<'\n';
}
return 0;
}

