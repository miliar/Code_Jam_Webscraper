#include <fstream>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

int n, m;
int a[102][102];

bool checkUp(int i, int j)
{
	int l;
	for(l=0;l<n;++l)
		if(l!=i && a[l][j]>a[i][j])
			return false;
	return true;
}
/*
bool checkDown(int i, int j)
{
	int l;
	for(l=i+1;l<n;++l)
		if(a[l][j]<a[i][j])
			return false;
	return true;
}
*/

bool checkLeft(int i, int j)
{
	int l;
	for(l=0;l<m;++l)
		if(l != j && a[i][l]>a[i][j])
			return false;
	return true;
}
/*
bool checkRight(int i, int j)
{
	int l;
	for(l=j+1;l<m;++l)
		if(a[i][l]<a[i][j])
			return false;
	return true;
}
*/
bool check(int i, int j)
{
	return checkUp(i,j) || checkLeft(i,j);
}

bool check()
{
	int i,j;
	for(i=0; i<n; ++i)
		for(j=0; j<m; ++j)
			if(!check(i,j))
				return false;
	return true;
}

int main()
{
	int t, tt, i,j;
	fin>>tt;
	for(t=1; t<=tt; ++t)
	{
		fin>>n>>m;
		for(i=0; i<n; ++i)
			for(j=0; j<m; ++j)
				fin>>a[i][j];
		fout<<"Case #"<<t<<": ";
		if(check())
			fout<<"YES"<<endl;
		else
			fout<<"NO"<<endl;
	}
	return 0;
}