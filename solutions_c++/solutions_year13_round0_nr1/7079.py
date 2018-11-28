#include <cstdio>
#include <iostream>

using namespace std;

char tablero[4][4];

bool chequeoFila(char c, int fila)
{
	for(int i=0;i<4;i++)
	{
		if(tablero[fila][i] != c && tablero[fila][i] != 'T')
			return false;
	}
	return true;
}

bool chequeoColumna(char c, int colu)
{
	for(int i=0;i<4;i++)
	{
		if(tablero[i][colu] != c && tablero[i][colu] != 'T')
			return false;
	}
	return true;
}

bool chequeo(char c)
{
	for(int i=0;i<4;i++)
	{
		if(chequeoFila(c,i)) return true;
		if(chequeoColumna(c,i)) return true;
	}
	bool d1 = true;
	bool d2 = true;
	for(int i=0;i<4;i++)
	{
		if(tablero[i][i] != c && tablero[i][i] != 'T') d1=false;
		if(tablero[i][4-i-1] != c && tablero[i][4-i-1] != 'T') d2=false;
	}
	return (d1 || d2);
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T;
	cin>>T;
	for(int t=0;t<T;t++)
	{
		bool hayLibres = false;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>tablero[i][j];
				if(tablero[i][j] == '.') hayLibres = true;
			}
		}
		cout<<"Case #"<<t+1<<": ";
		if(chequeo('O')) cout<<"O won";
		else if(chequeo('X')) cout<<"X won";
		else if(hayLibres) cout<<"Game has not completed";
		else cout<<"Draw";
		cout<<endl;
	}
}
