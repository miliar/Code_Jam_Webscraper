/*
* @Author: ritesh
* @Date:   2016-04-09 01:23:41
* @Last Modified by:   ritesh
* @Last Modified time: 2016-04-09 11:53:50
*/

#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <cstring>
#include <queue>
#include <algorithm>
#include <climits>
#include <string>
#include <cstdlib>
#include <sstream>
#include <cmath>
#include <cctype>
#include <iomanip>
#include <cstdio>
#include <list>
#include <bitset>

using namespace std;

typedef pair <int, int> pii;
typedef pair <int, double> pid;
typedef pair <double, double> pdd;
typedef vector <int> vi;
typedef vector <double> vd;
typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;

#define MP make_pair
#define PB push_back
#define PPB pop_back
#define PF push_front
#define PPF pop_front
#define EL endl
#define CO cout


ll getDivisor(ull num)
{
	ll divisor = 0;
	for(ll i = 2; i <= sqrt(num); i ++)
	{
		if((ull(num)% i) == 0)
		{
			divisor = i;
			break;
		}
	}

	return divisor;
}


string decToBin(int number)
{
    if ( number == 0 ) return "0";
    if ( number == 1 ) return "1";

    if ( number % 2 == 0 )
        return decToBin(number / 2) + "0";
    else
        return decToBin(number / 2) + "1";
}

ull toBin(int count)
{
	return stoull(decToBin(count));
}


ull valueOf(string n, int baseN)
{

    char aux[n.size()], *end;
    strcpy(aux, n.c_str());
    return strtoull(aux, &end, baseN);

}

ull interpret(ull num, int baseN)
{
    return valueOf(to_string(num), baseN);
}


int main() {
	int Tcases;

	cin >> Tcases;

	for (int tc = 1; tc <= Tcases; tc++)
	{
		cout << "Case #" << tc << ":\n";

		int n, j;
		cin >> n >> j;

		int loops  = pow((n-2),2);

		string num_st = string(n, '0');
		num_st[0] = '1';
		num_st[num_st.length()-1] = '1';

		ull start_num = stoull(num_st);
		// cout << "statr num " << start_num << endl;
		int count = 0;

		for (int jj=0; jj<loops ; jj++)
		{
			bool jamcoin = true;
			vector<int> divisors;

			ull num = start_num + toBin(count)*10;	// generate new numbers

			// cout << " ::: " << num << "::::" << endl;
			for (int baseN=2; baseN <=10; baseN++)
			{
				ull interpreted = interpret(num, baseN);
				// cout << " inter " << interpreted;
				int divisor = getDivisor(interpreted);
				// cout <<  " :: divisor is : " << divisor << endl;
				if (divisor)
				{
					divisors.push_back(divisor);
				}
				else
				{
					jamcoin = false;
					divisors.clear();
					break;
				}

			}

			count += 1;

			if (jamcoin)
			{
				cout <<  num;
				for (int v=0; v<divisors.size(); v++)
				{
					cout << " " << divisors[v];
				}
				cout << "\n";

				j -= 1;
				if (j<=0)
				{
					break;
				}
			}

		}

	}

	return 0;
}
