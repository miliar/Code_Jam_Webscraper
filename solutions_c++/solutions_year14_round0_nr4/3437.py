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

int game(vector<double> & V1, vector<double> & V2, int m)
{
	int i = 0, j = 0;
	while(i<m && j<m)
	{
		while(V2[j] > V1[i])
		{
			i++;
			if(i==m)
			{
				return j;
			}
		}
		j++;
		i++;
	}
	return j;
}
int main()
{
    int n, m;//, q;//, k;
   // int tmp;
    scan(n);

	FOR(T,n)
	{
		double d;
		scan(m);
		vector<double> V1(m, 0.0), V2(m, 0.0);


		FOR(i,m)
		{
			scanf("%lf", &d);
			V1[i] = d;
		}
		FOR(i,m)
		{
			scanf("%lf", &d);
			V2[i] = d;

		}
		sort(V1.begin(), V1.end());
		sort(V2.begin(), V2.end());
		int A = game(V1,V2, m);
		int B = game(V2,V1, m);
		cout << "Case #" << T+1 <<": " << A << " " << m - B << endl;
	}
    

    return 0;
}
