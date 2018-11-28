#include <iostream>
#include <fstream>
using namespace std;
ifstream in("input.txt");
ofstream out("output.txt");
bool badcondition (int mat[4][4], int mat2[4][4], int a, int b)
{
	int cont = 0;
	for(int n=0;n<4;n++)
	{
		for(int p=0;p<4;p++)
		{
			if(mat[a-1][n]==mat2[b-1][p])
			{
				cont++;
			}
			if(cont>1)
				return true;
		}
	}
	return false;
}
bool corresponds(int mat1[4][4],int mat2[4][4],int a,int b,int &val)
{
	for(int n=0;n<4;n++)
	{
		for(int p =0;p<4;p++)
		{
			if(mat1[a-1][n]==mat2[b-1][p])
			{
				val = mat1[a-1][n];
				return true;
			}
		}
	}
	return false;
}
void solve()
{
	int mat1[4][4], mat2[4][4];
	int a,b;
	in >> a;
	for(int n=0;n<4;n++)
	{
		for(int p=0;p<4;p++)
		{
			in >> mat1[n][p];
		}
	}
	in >> b;
	int val;
	for(int n=0;n<4;n++)
	{
		for(int p=0;p<4;p++)
		{
			in >> mat2[n][p];
		}
	}
	if(badcondition(mat1,mat2,a,b))
		out << "Bad magician!";
	else if(corresponds(mat1,mat2,a,b,val))
		out << val;
	else
		out << "Volunteer cheated!";
}
int main()
{
	int dim;
	in >> dim;
	for(int n=1;n<=dim;n++)
	{
		out << "Case #"<<n<<": ";
		solve();
		out<<endl;
	}
}