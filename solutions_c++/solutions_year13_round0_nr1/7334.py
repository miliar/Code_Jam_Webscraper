// D.cpp: archivo de proyecto principal.
// C.cpp: archivo de proyecto principal.

#include "stdafx.h"
#include <vector>
#include <queue>
#include <map>
#include <list>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>

using namespace std;

/* tipos */
typedef pair<int,int> pint;
typedef long long tint;
typedef unsigned int mint;
typedef unsigned long long mtint;

typedef vector<int> vint;
typedef vector<vint> vvint;

typedef long double tipo;

/* "funciones" */
#define forn(i,n) for(int ___n=n, i=0;i<___n;++i)
#define dforn(i,n) for(int i=(n)-1;i>=0;--i)
#define forsn(i,s,n) for(int ___n=n, i=s;i<___n;++i)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define forall(it,X) for(typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define dforall(it,X) for(typeof((X).rbegin()) it = (X).rbegin(); it != (X).rend(); ++it)
#define all(X) (X).begin(), (X).end()
#define esta(e, c) (c.find(e) != c.end())
#define DBG(a) cerr << #a << " = " << a << endl;

template<class T> string itos(const T&x) { ostringstream o; o<<x; return o.str(); }

string wrd[5050];
char mp[256][15];

tint mcd(tint a, tint b){return (b==0)?a:mcd(b, a%b);}
char MAPA[30][30];
int H, W;
int d;
int vacios=0;

void Contar_Elemntos(char val, int* X,int* O, int* T, int* vacios)
{
	switch(val)
	{
	case 'X':
		(*X)++;
		break;
	case 'O':
		(*O)++;
		break;
	case 'T':
		(*T)++;
		break;
	case '.':
		(*vacios)++;
		break;
			
	}	
}

int Buscar_Ganador()
{
	int O,X,T;
	int i,j;
	int vacios=0;
	
	//Busco en filas
	for(i=0;i<4;i++)
	{
		X=0;
		O=0;
		T=0;
		for(j=0;j<4;j++)
		{
			Contar_Elemntos(MAPA[i][j], &X, &O, &T, &vacios);
			if(O==4 || (O==3 && T==1))
				return 1;
			if(X==4 || (X==3 && T==1))
				return 2;
		}
	}
	
	//Busco en columnas
	for(j=0;j<4;j++)
	{
		X=0;
		O=0;
		T=0;
		for(i=0;i<4;i++)
		{
			Contar_Elemntos(MAPA[i][j], &X, &O, &T, &vacios);
			if(O==4 || (O==3 && T==1))
				return 1;
			if(X==4 || (X==3 && T==1))
				return 2;
		}
	}
	
	//Busco Diagonal 1
	X=0;
	O=0;
	T=0;
	for(i=0;i<4;i++)
	{
		
		Contar_Elemntos(MAPA[i][i], &X, &O, &T, &vacios);
		if(O==4 || (O==3 && T==1))
			return 1;
		if(X==4 || (X==3 && T==1))
			return 2;
	}
	
	
	//Busco Diagonal 2
	X=0;
	O=0;
	T=0;
	for(i=0;i<4;i++)
	{
		
		Contar_Elemntos(MAPA[i][3-i], &X, &O, &T, &vacios);
		if(O==4 || (O==3 && T==1))
			return 1;
		if(X==4 || (X==3 && T==1))
			return 2;
	}

	if(vacios)
		return 3;
	return 4;
}

int main() {
	int casos;	
	
	int ret;
	cin >> casos;
	
	for(int i=0; i < casos; i++)
	{				
		for(int y=0;y<4;y++)
		{
			for(int x=0;x<4;x++)
			{
				cin >> MAPA[y][x];
			}
		}
		ret=Buscar_Ganador();
		switch(ret)
		{
		case 1:
			cout << "Case #"<< i+1<< ": O won" << endl;
			break;
		case 2:
			cout << "Case #"<< i+1<< ": X won" << endl;
			break;
		case 3:
			cout << "Case #"<< i+1<< ": Game has not completed" << endl;
			break;
		case 4:
			cout << "Case #"<< i+1<< ": Draw" << endl;
			break;

		}
	}
	
	return 0;
}

