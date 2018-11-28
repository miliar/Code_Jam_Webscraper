#include <iostream>
using namespace std;

int t[17][17];
int count();
int INF=10000;
int x, y, n;

int movex[]={0, 0, -1, 1};
int movey[]={1, -1, 0, 0};

int jedynka(int x, int y);

int main()
{
	int ilez;
	cin>>ilez;
	for(int aa=0; aa<ilez; aa++)
	{
		cin>>x>>y>>n;
		int wynik=INF;

		
		int ilejedynek;
		for(int i=0; i<(1<<(x*y)); i++)
		{
			ilejedynek=0;
			for(int a=0; a<x*y; a++)
			{
				if( ((1<<a)&i)!=0) ilejedynek++;
				t[a/y][a%y]=((1<<a)&i)!=0;
			}
			

			if(ilejedynek==n)
			{

				wynik=min(wynik, count());
			}
		}

		cout<<"Case #"<<aa+1<<": "<<wynik<<endl;
	}
}
int count()
{
	int wynik=0;
	for(int i=0; i<x; i++)
	{
		for(int j=0; j<y; j++)
		{
			if(t[i][j]==1)
			for(int k=0; k<4; k++)
			{
				if(jedynka(i+movex[k], j+movey[k]))
					wynik++;
			}
		}
	}
	return wynik/2;
}
int jedynka(int i, int j)
{
	if(i<0 || j<0 || i>=x || j>=y) return 0;
	return t[i][j];
}
