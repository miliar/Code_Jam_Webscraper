# include<iostream>
# include<fstream>
using namespace std;
int findhighest(int *p, int m)
{
	int temp = p[0];
	for(int i = 0; i < m; i++)
	{
		if(p[i] > temp)
		{
			temp = p[i];
		}
	}
	return temp;
}
void check(int **p, int n, int m, int k1, fstream &f)
{
	int **q;
	q = new int*[n];
	for(int i = 0; i < n; i++)
	{
		q[i] = new int[m];
	}
	for(int j = 0 ; j < n; j++)
	{
		for(int k = 0; k < m; k++)
		{
			q[j][k] = 100;
		}
	}
	for(int i = 0; i < n; i++)
	{
		int a = findhighest(p[i],m);
		for(int j = 0; j < m; j++)
		{
			q[i][j] = a;
		}
	}
	for(int i = 0; i < m; i++)
	{
		int *zm = new int[n];
		for(int zz = 0; zz < n; zz++)
		{
			zm[zz] = p[zz][i];
		}
		int a = findhighest(zm,n);
		for(int j = 0; j < n; j++)
		{
			if(q[j][i] > a)
			{
				q[j][i] = a;
			}
		}
	}
	for(int i = 0; i < n; i++)
	{
		for(int j = 0; j < m; j++)
		{
			if(p[i][j] != q[i][j])
			{
				f << "Case #" << k1 << ": NO" << endl;
				return;
			}
		}
	}
	f << "Case #" << k1 << ": YES" << endl;
	return;
}	
int main()
{
	int z=0, n, m,**p, kz = 1;
	fstream file1("OUTPUT.TXT",ios::in | ios::out);
	fstream file("B-large.in",ios::in | ios::out);	
	file >> z;
	while(z > 0)
	{
		file >> n >> m;
		p = new int*[n];
		for(int i = 0; i < n; i++)
		{
			p[i] = new int[m];
		}
		for(int j = 0 ; j < n; j++)
		{
			for(int k = 0; k < m; k++)
			{
				file >> p[j][k];
			}
		}
		check(p,n,m,kz, file1);
		z--;
		kz++;
	}
	file.close();
	file1.close();
	return 0;
}
