#include<algorithm>
#include<cmath>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<map>
#include<queue>
#include<set>
#include<sstream>

#define forn(i,n) for(int i=0;i<n;i++)
#define all(v) v.begin(),v.end()

using namespace std;

long double calc(long double f, long double c, long double x)
{
    long double aux = 0., c2=2.,res = x/c2;
    for(int i=1;i<(int)((x+1.)*10.);i++)
    {
        aux += f/c2;
        c2 += c;
        res = min(res,aux+x/c2);
    }
    return res;
}


int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int casos;
	cin >> casos;
	forn(casito,casos)
	{
        long double c,f,x;
        cin >> c >> f >> x;
        cout << "Case #" << casito+1 <<": ";
        double res = (double)calc(c,f,x);
        printf("%.7f\n",res);
	}
}
