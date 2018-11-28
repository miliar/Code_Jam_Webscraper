#include <cstdio>
#include <fstream>
using namespace std;
int wynik[5][5][5];
int x,r,c,temp,t;
int main()
{
	fstream plik;
    plik.open( "C:/a.txt", ios::out);
	scanf("%d", &t);
	//I noticed that input is very small, so I can simply chceck all posibilities on the sheet of paper and I did it
	wynik[1][1][1]=1;
	wynik[1][2][1]=1;
	wynik[1][2][2]=1;
	wynik[1][3][1]=1;
	wynik[1][4][1]=1;
	wynik[1][4][2]=1;
	wynik[2][2][1]=1;
	wynik[2][2][2]=1;
	wynik[2][3][1]=1;
	wynik[2][3][2]=1;
	wynik[2][3][3]=1;
	wynik[2][4][1]=1;
	wynik[2][4][2]=1;
	wynik[3][3][1]=1;
	wynik[3][3][3]=1;
	wynik[3][4][1]=1;
	wynik[3][4][2]=1;
	wynik[3][4][3]=1;
	wynik[3][4][4]=1;
	wynik[4][4][1]=1;
	wynik[4][4][2]=1;
	wynik[4][4][4]=1;
	for(int i=1; i<=t; ++i)
	{
		scanf("%d%d%d", &x, &r, &c);
		if(r>c)
		{
			temp=r;
			r=c;
			c=temp;
		}
		if(wynik[r][c][x]==1)
			plik<<"Case #"<<i<<": GABRIEL"<<endl;
		else
			plik<<"Case #"<<i<<": RICHARD"<<endl;
	}
	plik.close();
}
