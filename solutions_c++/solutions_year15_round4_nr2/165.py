#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <deque>
#include <cstdio>
#include <cstdlib>
#include <numeric>
#include <functional>
#include <algorithm>
#include <cassert>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define forsn(i,s,n) for(int i=(s);i<(int)(n);i++)
#define dforn(i,n) for(int i=(n)-1;i>=0;i--)
#define dforsn(i,s,n) for(int i=(n)-1;i>=(int)(s);i--)

#define forall(i,c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define dforall(i,c) for(typeof((c).rbegin()) i = (c).rbegin(); i != (c).rend(); i++)
#define all(c) (c).begin(),(c).end()

#define esta(x,c) ((c).find(x) != (c).end())
#define zMem(c) memset((c),0,sizeof(c))

#define feq(x, y) (fabs((x)-(y)) <= EPS)

typedef long long tint;
typedef long double tdbl;

typedef pair<int,int> pint;
typedef pair<tint,tint> ptint;

typedef vector<int> vint;
typedef vector<vint> vvint;
typedef vector<string> vstr;

const int MAXN = 256;

pair<double,double> originals[MAXN];

double rate[MAXN], temp[MAXN];
double cant[MAXN];
double V,X;
int N;

const double EPS = 1e-10;

bool sePuede(double t)
{
    forn(i,N) cant[i] = t * rate[i];
    double meanValue = 0.0;
    double total = 0.0;
    forn(i,N)
    {
        meanValue += cant[i] * temp[i];
        total += cant[i];
    }
    if (total < V - EPS) return false;
    meanValue /= total;
    if (meanValue == X)
        return total >= V;
    else
    {
        double totalV = 0.0;
        double totalQ = 0.0;
        // Voy a usar toda el agua de la temperatura "incorrecta"
        forn(i,N)
        if ((meanValue < X && temp[i] >= X - EPS) || (meanValue > X && temp[i] <= X + EPS))
        {
            totalV += cant[i];
            totalQ += temp[i] * cant[i];
        }
        int start, step, last;
        if (meanValue < X)
        {
            start = N-1;
            step = -1;
            last = -1;
        }
        else
        {
            start = 0;
            step = 1;
            last = N;
        }
        for(int i = start; i != last; i += step)
        if ((meanValue < X && temp[i] < X - EPS) || (meanValue > X && temp[i] > X + EPS))
        {
            double newTemp = (totalQ + temp[i] * cant[i]) / (totalV + cant[i]);
            if ((meanValue < X && newTemp < X) || (meanValue > X && newTemp > X))
            {
                // (totalQ + temp[i] * z) / (totalV + z) = X
                // (totalQ + temp[i] * z)  = X * (totalV + z)
                // totalQ + temp[i] * z  = X * totalV + X * z
                // (temp[i] - X) * z  = X * totalV - totalQ
                // z  = (X * totalV - totalQ) / (temp[i] - X)
                double z = (X * totalV - totalQ) / (temp[i] - X);
                return totalV + z >= V;
            }
            else
            {
                totalV += cant[i];
                totalQ += temp[i] * cant[i];
            }
        }
        return totalV >= V;
    }    
    // (t1 - X) / (X-t2)  =  q2
    // (X-t2) Del 1 por cada (t1 - X) del 2
}

int main()
{
	int totalCasos;
	cin >> totalCasos;
	forn(caso,totalCasos)
	{
        cin >> N;
        cin >> V >> X;
        forn(i,N) cin >> originals[i].second >> originals[i].first; // rate + temp
        sort(originals, originals+N);
        forn(i,N)
        {
            rate[i] = originals[i].second;
            temp[i] = originals[i].first;
        }
        bool masOIgual = false, menosOIgual = false;
        int idMenor = -1, idMayor = -1;
        forn(i,N)
        {
            masOIgual   |= temp[i] >= X - EPS;
            if (temp[i] >= X - EPS) idMayor = i;
            menosOIgual |= temp[i] <= X + EPS;
            if (temp[i] <= X + EPS) idMenor = i;
        }
        cout << "Case #" << caso + 1 << ": ";
        if (masOIgual && menosOIgual)
        {
            assert(idMenor >= 0);
            assert(idMayor >= 0);
            
            double a = 0.0, b = 1e10;
            forn(steps, 256)
            {
                double c; 
                if (steps % 2 == 0)
                    c = sqrt(a*b);
                else 
                    c = (a+b) / 2.0;
                if (sePuede(c))
                    b = c;
                else
                    a = c;
            }
            printf("%.15lf\n", (a+b)/2.0);
        }
        else
        {
            cout << "IMPOSSIBLE" << endl;
        }
	}
	return 0;
}
