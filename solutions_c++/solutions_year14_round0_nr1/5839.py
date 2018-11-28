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
    int firstAnswer;
    cin >> firstAnswer;

    int firstArrangement[4][4];

    for (auto &y : firstArrangement)
    {
        for (auto &x : y)
        {
            cin >> x;
        }
    }

    int secondAnswer;
    cin >> secondAnswer;

    int secondArrangement[4][4];

    for (auto &y : secondArrangement)
    {
        for (auto &x : y)
        {
            cin >> x;
        }
    }

    int matches = 0;
    bool done = false;
    string output;

    for (auto first : firstArrangement[firstAnswer-1])
    {
        for (auto second : secondArrangement[secondAnswer-1])
        {
            if (first == second)
            {
                if (matches++ == 0)
                {
                    output = to_string(first);
                }
                else
                {
                    output = "Bad Magician!";
                    done = true;
                    break;
                }
            }

            if (done) break;
        }
    }

    if (matches == 0)
    {
        output = "Volunteer cheated!";
    }

    cout << output;
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