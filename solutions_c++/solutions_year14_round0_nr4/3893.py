// template

#include "stdafx.h"

#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz size()
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define dot(a,b) ((conj(a)*(b)).X)
#define X real()
#define Y imag()
#define length(V) (hypot((V).X,(V).Y))
#define vect(a,b) ((b)-(a))
#define cross(a,b) ((conj(a)*(b)).imag())
#define normalize(v) ((v)/length(v))
#define rotate(p,about,theta) ((p-about)*exp(point(0,theta))+about)
#define pointEqu(a,b) (comp(a.X,b.X)==0 && comp(a.Y,b.Y)==0)

typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vii;
typedef long long ll;
typedef long double ld;
typedef complex<double> point;
typedef pair<point, point> segment;
typedef pair<double, point> circle;
typedef vector<point> polygon;

int arr[2000];
//#define SMALL
#define LARGE
int main() {
	freopen("a.txt", "rt", stdin);
#ifdef SMALL
	freopen("D-small-attempt1.in","rt",stdin);
	freopen("D-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("D-large.in","rt",stdin);
	freopen("D-large.out","wt",stdout);
#endif
	int T;
	vector<double> naomi;
	vector<double> ken;

	int N;
	cin >> T;
	for (int i =1; i<=T; i++)
	{
		cin >> N;
		naomi.clear();
		ken.clear();
		double k;
		for (int j=0; j<N;j++)
		{
			cin >> k;
			naomi.push_back(k);
		}
		for (int j=0; j<N; j++)
		{
			cin >> k;
			ken.push_back(k);
		}
		int Dwar = 0;
		int war = 0;
		cout << "Case #" << i << ": ";

		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());
		int a = 0;
		int b = 0;
		while (a<N)
		{
			while ((b<N) && (naomi[a] > ken[b])) b++;
			if (b == N) break;
			else
			{
				war++;
				a++;
				b++;
			}
		}
		war = N - war;

		a = 0;
		b = 0;
		while (a < N)
		{
			if (naomi[a] > ken[b])
			{
				Dwar++;
				b++;
			}
			a++;
		}
		cout << Dwar << " " << war << endl;
	}
}




