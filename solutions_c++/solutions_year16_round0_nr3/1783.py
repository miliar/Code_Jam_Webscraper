#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
using namespace std;

#define cin fin
#define cout fout
ifstream fin("a.in");
ofstream fout("ans.txt");

map<string, bool>hash;
int a[100];
int proof[100];

bool find_proof(int m, int n)
{
	for(int i = 2; i <= 100; i++)
	{
		int sm = 0;
		for(int k = 1; k <= n; k++)
			sm = (sm * m + a[k]) % i;
		if(sm % i == 0)
		{
			proof[m] = i;
			return true;
		}
	}
	return false;
}

bool work(int n)
{
	//hash.clear();
	for(int i = 1; i <= n; i++)
		a[i] = rand() % 2;
	a[1] = 1; a[n] = 1;
	string t = "";
	for(int i = 1; i <= n; i++)
		t += char('0' + a[i]);
	if(hash[t]) return false;
	for(int i = 2; i <= 10; i++)
		if(!find_proof(i, n)) return false;
	cout << t;
	for(int i = 2; i <= 10; i++)
		cout << ' ' << proof[i];
	cout << endl;
	hash[t] = true;
	return true;
}

int main()
{
	srand(0);
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++)
	{
		int n, m;
		cin >> n >> m;
		cout << "Case #" << t << ":" << endl;
		while(m > 0)
		{
			if(work(n)) m--;
		}
	}
	return 0;
}

