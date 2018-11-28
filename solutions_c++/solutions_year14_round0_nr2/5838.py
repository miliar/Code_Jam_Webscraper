#include <iostream>
#include <map>
#include <list>
#include <vector>
#include <string>
#include <algorithm>
#include <math.h>

using namespace std;

#define MAPITR(a,b) map<a,b>::iterator
#define LISTITR(a)  list<a>::iterator

#define ITER(itr,a) for( itr = (a).begin(); itr != (a).end(); ++itr )
#define ITERNI(itr,a)   for( itr = (a).begin(); itr != (a).end();  )
#define FORI(i,a,b) for( int i(a), _b(b); i < _b; ++i )
#define FORD(i,a,b) for( int i(a), _b(b); i > _b; --i )
#define FORLE(i,a,b)    for( int i(a), _b(b); i <= _b; ++i )
#define FORGE(i,a,b)    for( int i(a), _b(b); i >= _b; --i )

typedef list<bool> lb;
typedef list<char> lc;
typedef list<int> li;
typedef list<double> ld;
typedef list<string> ls;

typedef vector<bool> vb;
typedef vector<char> vc;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<string> vs;

void process()
{
    double farmCost, extra, end;

    cin >> farmCost;
    cin >> extra;
    cin >> end;

    double count = 0;
    double rate = 2.0;
    double totalTime = 0;

    while (count < end)
    {
        // buy farm or wait it out?
        double endTime = end / rate;

        // assume we buy the farm as soon can be afforded
        double farmTime = farmCost / rate;
        double farmEndTime = end / (rate + extra);

        if (endTime <= (farmTime+farmEndTime)) // wait it out, we're done
        {
            totalTime += endTime;
            break;
        }

        totalTime += farmTime;
        rate += extra;
    }

    cout.precision(7);
    cout << fixed << totalTime;
}

int main()
{
    int nCases;
    cin >> nCases;

    FORLE(i, 1, nCases)
    {
        cout << "Case #" << i << ": ";
        process();
        cout << endl;
    }

    return 0;
}