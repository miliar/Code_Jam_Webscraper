#include <fstream>
#include <iostream>
#include <stdlib.h>
#include <string.h>

using namespace std;

unsigned int tab[1001];

ifstream fin;
ofstream fout;
	
	
void prep()
{
	memset(tab, 0, 1001 * sizeof(unsigned int));
	
	tab[1] = 1;
	tab[4] = 1;
	tab[9] = 1;
	tab[121] = 1;
	tab[484] = 1;
	
	int i;
	
	for(i = 1; i < 1001; i ++)
	{
		tab[i] += tab[i - 1];
	}
}

void solve(int game, int A, int B)
{
	int res = tab[B] - tab[A - 1];
	
	cout << "Case #" << game << ": " << res << endl;
	fout << "Case #" << game << ": " << res << endl;
}

int main()
{
	int n, A, B, i, j, k;
	char ch;
	
	fin.open("p3.in");
	fout.open("p3.out");
	
	fin >> n;
	prep();
	
	for(i = 0; i < n ; i ++)
	{
		fin >> A >> B;
		
		solve(i + 1, A, B);
	}
	fout << endl;
	
	
	
	fin.close();
	fout.close();
	
}
