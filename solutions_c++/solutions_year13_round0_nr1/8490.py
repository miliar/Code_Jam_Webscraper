#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <iterator>
#include <utility>
using namespace std;

typedef long long ll; 
typedef pair<int, int> ii; 
typedef vector<ii> vii; 
typedef vector<int> vi; 


template< class T > T _abs(T n) { return (n < 0 ? -n : n); }
template< class T > T _max(T a, T b) { return (!(a < b) ? a : b); }
template< class T > T _min(T a, T b) { return (a < b ? a : b); }
template< class T > T sq(T x) { return x * x; }

#define	FOR(i,a,b)	for (int i = int(a); i < int(b); i++)
#define	FORN(i,a,b)	for (int i = int(a)-1; i >= int(b); i--)
#define	ALL(v)		v.begin(), v.end()
#define	RALL(v)		v.rbegin(), v.rend()
#define C(i)	fcout << #i << " : " << i << endl
#define MP(x, y) make_pair(x, y)
#define SET(p) memset(p, -1, sizeof(p))
#define CLR(p) memset(p, 0, sizeof(p))
#define MEM(p, v) memset(p, v, sizeof(p))
#define CPY(d, s) memcpy(d, s, sizeof(s))
#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)
#define SZ(c) (int)c.size()
#define PB(x) push_back(x)
#define i64 unsigned long long
#define ld long double
#define pii pair< int, int >
#define psi pair< string, int >

string readString();
void evaluateString(string);
bool evaluateX(string);
bool evaluateY(string);
bool evaluateDiagonal(string);
bool evaluateTX(string);
bool evaluateTY(string);
bool evaluateTDiagonal(string);
bool evaluateBlanks(string);
bool checkSub(string);
bool checkSubT(string);

ifstream fcin("test.txt");
ofstream fcout("results.txt");
int main()
{
	
	int cases;
	string matriz;

	fcin >> cases;

	FOR(i,0,cases)
	{	
		matriz = readString();
		if(i!=0) fcout << endl;
		fcout << "Case #" << i+1 << ": ";
		evaluateString(matriz);
		
	}
}


void evaluateString(string matriz)
{
	if(matriz == "................")
	{
		fcout << "Game has not completed";
		return;
	}
	else if(evaluateX(matriz)) return;
	else if(evaluateY(matriz)) return;
	else if(evaluateDiagonal(matriz)) return;
	else if(evaluateTX(matriz))return;
	else if(evaluateTY(matriz)) return;
	else if(evaluateTDiagonal(matriz)) return;
	else if(evaluateBlanks(matriz)) return;

	fcout << "Draw";
}

bool evaluateY(string matriz)
{
	string sub;

	FOR(x,0,4)
	{
		sub = matriz[x];
		sub += matriz[x+4];
		sub += matriz[x+8];
		sub += matriz[x+12];

		if(checkSub(sub)) return true;
	}

	return false;
}

bool evaluateX(string matriz)
{
	int contX = 0;
	string sub;

	FOR(x,0,4)
	{
		sub = matriz.substr(contX,4);
		contX += 4;
		if(checkSub(sub)) return true;
	}

	return false;
}

bool evaluateDiagonal(string matriz)
{
	string sub;

	sub = matriz[0];
	sub += matriz[5];
	sub += matriz[10];
	sub += matriz[15];

	if(checkSub(sub)) return true;

	sub = matriz[3];
	sub += matriz[6];
	sub += matriz[9];
	sub += matriz[12];
	if(checkSub(sub)) return true;
	return false;
}

bool evaluateTX(string matriz)
{

	int pos = matriz.find("T");
	string sub;

	if(pos < 0) return false;

	if(pos%4 == 0 || pos == 0)//T is on left Side
	{
		sub = matriz[pos+1];
		sub += matriz[pos+2];
		sub += matriz[pos+3];
	}
	else if((pos+1)%4 == 0)//T is on right Side
	{
		sub = matriz[pos-1];
		sub += matriz[pos-2];
		sub += matriz[pos-3];
	}
	else if((pos+3)%4 == 0)//XTXX
	{
		sub = matriz[pos-1];
		sub += matriz[pos+1];
		sub += matriz[pos+2];
	}
	else if((pos+2)%4 == 0)//XXTX
	{
		sub = matriz[pos-2];
		sub += matriz[pos-1];
		sub += matriz[pos+1];
	}

	if(checkSubT(sub)) return true;
	return false;
}
bool evaluateTY(string matriz)
{
	int pos = matriz.find("T");
	string sub;

	if(pos < 4)//T is on the top
	{
		sub = matriz[pos+4];
		sub += matriz[pos+8];
		sub += matriz[pos+12];
	}
	else if(pos >= 12)
	{
		sub = matriz[pos-4];
		sub += matriz[pos-8];
		sub += matriz[pos-12];
	}
	else if(pos >= 4 && pos <= 7)	//XOOX
	{								//TOXO <-
		sub = matriz[pos-4];		//XOOO
		sub += matriz[pos+4];		//XXOX
		sub += matriz[pos+8];
	}
	else if(pos >= 8 && pos <= 11)	//OOOX
	{								//OOXO
		sub = matriz[pos-8];		//TXOO <-
		sub += matriz[pos-4];		//OOOX
		sub += matriz[pos+4];
	}

	if (checkSubT(sub)) return true;
	return false;
}


bool evaluateTDiagonal(string matriz)
{
	int pos = matriz.find("T");
	string sub;

	if(pos == 0)
	{
		sub = matriz[5];
		sub += matriz[10];
		sub += matriz[15];
	}
	else if(pos == 3)
	{
		sub = matriz[6];
		sub += matriz[9];
		sub += matriz[12];
	}
	else if(pos == 12)
	{
		sub = matriz[9];
		sub += matriz[6];
		sub += matriz[3];
	}
	if(pos == 15)
	{
		sub = matriz[10];
		sub += matriz[5];
		sub += matriz[0];
	}

	if(checkSubT(sub)) return true;
	return false;
}

bool evaluateBlanks(string matriz)
{
	int pos = matriz.find(".");

	if(pos >= 0)
	{
		fcout << "Game has not completed";
		return true;
	}

	return false;
}

bool checkSub(string sub)
{
	if(sub == "OOOO"){
		fcout << "O won";
		return true;
	} else if(sub == "XXXX"){
		fcout << "X won";
		return true;
	}

	return false;
}

bool checkSubT(string sub)
{
	if(sub == "OOO"){
		fcout << "O won";
		return true;
	} else if(sub == "XXX"){
		fcout << "X won";
		return true;
	} 

	return false;
}

string readString()
{
	string matriz = "";
	char letter;

	FOR(i,0,16){
		fcin >> letter;
		matriz += letter;
	}

	return matriz;
}