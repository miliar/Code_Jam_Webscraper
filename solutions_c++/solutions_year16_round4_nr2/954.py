#include <iostream>
#include <algorithm>
#include <vector>
#include <sstream>
#include <set>
#include <map>
#include <cmath>
#include <cstdio>
#include <queue>
#include <cstring>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define dforn(i,n) for(int i=(int)(n)-1;i>=0;i--)
#define all(v) v.begin(),v.end()

long double matriz[256][256];

double calc2(vector<long double> &vec,int k)
{
	matriz[0][0] = 1;
	for(int i=1;i<=k;i++)
	{
		for(int j=0;j<=i;j++)
		{
			if(i == j)
				matriz[i][j] = matriz[i-1][j-1] * vec[i-1];
			else if(j == 0)
				matriz[i][j] = matriz[i-1][0] * (1.-vec[i-1]);
			else
				matriz[i][j] = matriz[i-1][j-1] * vec[i-1] + matriz[i-1][j] * (1.-vec[i-1]);
		}
	}
	return matriz[k][k/2];
}

double calc(vector<long double> vec, int k)
{
	long double res = 0;
	forn(i,k+1)
	{
		vector<long double> vec2;
		for(int j=0;j<i;j++)
			vec2.push_back(vec[j]);
		int rem = k-i;
		for(int j = vec.size()-rem;j<vec.size();j++)
			vec2.push_back(vec[j]);
		long double aux = calc2(vec2,k);
		if(aux > res)
			res = aux;
	}
	return (double)res;
}

int main()
{
	int casos;
	cin >> casos;
	for(int casito = 1; casito <= casos; casito++)
	{
		int n,k;
		cin >> n >> k;
		vector<long double> vec(n);
		forn(i,n)
			cin >> vec[i];
		sort(all(vec));
		printf("Case #%d: %.7f\n",casito,calc(vec,k));
	}
}