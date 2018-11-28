#include <cstdio>
#include <vector>
#include <utility>
#include <cstring>
#include <cstdlib>
#include <map>
#include <iostream>
#include <algorithm>
#include <string>
#include <stack>
#include <queue>
#include <cmath>
#include <set>
#include <assert.h>
#include <bitset>
#include <climits>
#include <sstream>

using namespace std;
#define pb push_back
#define mp make_pair
#define S second
#define F first
#define INF 0x3f3f3f3f
#define ll long long
#define mod 10
#define B 33
#define MAX 100011
#define eps 1e-7
#define ull unsigned long long

double pi = acos(-1);

typedef vector<int> vi;
typedef pair<int,int>ii;
typedef vector<ii> vii;

set<double> naomi;
set<double> ken;
set<double> ken2;

int main() {
	int n;
	cin>>n;

	for (int i = 0; i < n; ++i)
	{
		int m;
		cin>>m;
		naomi.clear();
		ken.clear();
		ken2.clear();
		for (int j = 0; j < m; ++j)
		{
			double aux;
			cin>> aux;
			naomi.insert(aux);
		}

		for (int j = 0; j < m; ++j)
		{
			double aux;
			cin>> aux;
			ken.insert(aux);
			ken2.insert(aux);
		}

		int warnp =0;
		
		for(set<double>::iterator it = naomi.begin(); it!=naomi.end(); it++){
			set<double>::iterator aux = upper_bound(ken.begin(),ken.end(), *it);
			if(aux != ken.end()){
				ken.erase(aux);
			}		
			else{
				warnp++;
			}
		}

		int np=0;

		set<double>::iterator nit = naomi.begin();
		set<double>::iterator kit = ken2.begin();
		
		while(nit!=naomi.end()){
			if(*nit>*kit){
				np++;
				kit++;	
			}
			nit++;

		}

		printf("Case #%d: %d %d\n", i+1, np,warnp);


	}
	return 0;
}