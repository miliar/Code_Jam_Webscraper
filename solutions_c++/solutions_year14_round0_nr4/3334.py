///SACAR FREOPEN.
#include <iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<cmath>
#include<set>
#include<list>
#include<cstdlib>
#include<cstdio>
#include<iomanip>
#include<stack>
#include<queue>
#include<stdio.h>
#include<string.h>
#include<map>
#include<sstream>
#include<assert.h>

using namespace std;

#define all(c) (c).begin(),(c).end()
#define forn(i,n) for(int i=0;i<(int)n;i++)
#define dforn(i,n) for(int i=n-1;i>=0;i--)
#define formn(i,m,n) for(int i=m;i<(int)n;i++)
#define dformn(i,m,n) for(int i=n-1;i>=m;i--)
#define mp make_pair
#define pb push_back

const double PI=acos(-1.0);

typedef long long tint;
typedef pair<int,int> pint;

int n;
double a[1010], b[1010];
int c[2020];

void merge(){
	int i = 0;
	int j = 0;
	while(i < n || j < n){
		if(i == n){
			c[i + j] = 2;
			j++;
		}
		else if(j == n){
			c[i + j] = 1;
			i++;
		}
		else{
			if(a[i] < b[j]){
				c[i + j] = 1;
				i++;
			}
			else if(a[i] > b[j]){
				c[i + j] = 2;
				j++;
			}
		}
	}
	cerr << endl;
}

int fair(){
	int lo = 0;
	int hi = n - 1;
	int res = 0;
	for(int ptr = n - 1; ptr >= 0; ptr--){
		if(a[ptr] > b[hi]){
			res++;
			lo++;
		}
		else if(a[ptr] < b[hi]){
			hi--;
		}
	}
	return res;
}

int unfair(){
	int res = 0;
	int open = 0;
	forn(i,2*n){
		if(c[i] == 2)
			open++;
		else if(c[i] == 1){
			if(open > 0){
				open--;
				res++;
			}
			else{
			}
		}
	}
	return res;
}

int main(){
freopen("Dlarge.in","r",stdin);
freopen("Dlarge.out","w",stdout);
	int TC; cin >> TC;
	for(int tc = 1; tc <= TC; tc++){
		cin >> n;
		forn(i,n)
			cin >> a[i];
		forn(i,n)
			cin >> b[i];
		sort(a,a + n);
		sort(b,b + n);
		merge();
		cout << "Case #" << tc << ": ";
		cout << unfair() << " " << fair() << endl;
	}
    return 0;
}
