#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define FOR(i,n) for(int i=0;i<n;++i)
#define FORB(i,b,n) for(int i=b;i<n;++i)
#define REV(i,n) for(int i=n;i>=0;--i)
#define FOREACH(T, it, v) for(T::iterator it = v.begin(); it !=v.end(); ++it)
#define print(STRING,INT) printf("%s= %d\n", STRING, INT)
#define scan(INT) scanf("%d", &INT)
#define PB(X) push_back(X)


typedef long long ll;
typedef unsigned int u32;
typedef unsigned int uint;
typedef unsigned int uInt;


const int INF = (0u - 11)/2;


typedef set<int> SI;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<long long> VL;
typedef set<long long> SL;
typedef map<int, int> MII;



int DEBUG = 1;

void log(char* S, long long a)
{
    if(DEBUG)
    {
        printf("%s= %lld\n", S, a);
    }
}

VI primes(int range = 10001)
{
    VI primes;
    primes.push_back(2);
    primes.push_back(3);
    primes.push_back(5);
    primes.push_back(7);
    for(int i = 9; i< range;i++)
    {
        int j=0;
        int flag = false;
        while((long long )primes[j]*primes[j]<= i)
        {
            if(i%primes[j++]==0)
            {
                flag = true;
                break;
            }
        }
        if(flag == false) primes.push_back(i);
    }
    return primes;
}

char tab[60][60];

void fill(char a)
{
	FOR(i,60)
		FOR(j,60)
		   tab[i][j] = a;
}

void printTab(int x, int y)
{
	FOR(i,x)
	{
		tab[i][y] = 0;
		printf("%s\n", tab[i]);
	}
}

int main()
{
    int n;//, m;//, q;//, k;
   // int tmp;
    scan(n);

	FOR(T,n)
	{
		double C, F, X;	
		double gen = 2.0;
		cin >> C>> F >> X;
		double time = 0;
		double bestTime = INF;
		while(bestTime > time + X/gen)
		{
			bestTime = time + X/gen;
			time += C / gen;
			gen += F;
		}
		cout.precision(18);
		cout << "Case #" << T+1 << ": " << bestTime << endl; 
	}
    

    return 0;
}
