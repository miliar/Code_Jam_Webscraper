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



int tab[5][5];

int main()
{
    int n, m;//, q;//, k;
   // int tmp;
    scan(n);

	FOR(T,n)
	{
		scan(m);

		MII M;

		FOR(i,4)
			FOR(j,4) cin >> tab[i][j];
		

		FOR(i,4)
		{
			M[tab[m-1][i]]++;
		}

		scan(m);
		//cout << "m is " << m << endl;
		FOR(i,4)
			FOR(j,4) cin >> tab[i][j];
		FOR(i,4)
		{
			//cout << tab[m-1][i] << endl;
			M[tab[m-1][i]]++;
		}

		int count = 0;
		int number = -1;
		FOREACH(MII, it, M)
		{
			//cout << it->first << " " << it->second << endl;
			if(it->second == 2) 
			{
				count++;
				number = it->first;
			}
		}
		cout << "Case #" << T+1 << ": "; 
		switch(count)
		{
			case 0:
				{
				cout << "Volunteer cheated!" << endl;
				break;
				}
		
			case 1:
				{
				cout << number << endl;
				break;
				}
			default:
				{
				cout << "Bad magician!" << endl;
				break;
				}
		}
	}
    

    return 0;
}
