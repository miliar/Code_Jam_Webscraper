#include <algorithm>
#include <iostream>
#include <fstream>
#include <cctype>
#include <math.h>
#include <vector>
#include <string>
#include <sstream>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <list>
#include <cstring>

#define MIN(a,b) (a < b ? (a) : (b))
#define MAX(a,b) (a > b ? (a) : (b))

using namespace std;

vector<int> getPrimes(int P)
{
	vector<int> primes;
	int sievebound = (P-1)/2;
	int crossbound = ((int)sqrt((double)P)-1)/2;
	bool *sieve = new bool[(P-1)/2+1];
    memset(sieve, 0, (P-1)/2+1);
	for (int i = 1; i <= crossbound; i++)
		if (!sieve[i])
			for (int j = 2*i*(i+1); j <= sievebound; j += 2*i+1)
				sieve[j] = 1;
	primes.push_back(2);
	for (int i = 1; i <= sievebound; i++)
		if (!sieve[i])
			primes.push_back(2*i+1);
	delete [] sieve;
	return primes;
}

int main()
{
    ifstream fin("in.in");
    ofstream fout("out.out");

    vector<int> p = getPrimes(1000000);

    int T;
    fin >> T;
    for (int t = 1; t <= T; t++) {
        fout << "Case #" << t << ": ";
        long long P, Q;
        string s;
        fin >> s;
        int pos = s.find('/');
        s[pos] = ' ';
        stringstream ss(s);
        ss >> P >> Q;
        for (int i = 0; i < p.size() && p[i] <= P && p[i] <= Q; i++) {
            while (P % p[i] == 0 && Q % p[i] == 0) {
                P /= p[i]; Q /= p[i];
            }
        }
        int place;
        for (place = 0; place < 41; place++) {
            if (Q == (1LL << place)) break;
            else if (Q < (1LL << place)) {
                place = 41;
                break;
            }
        }
        if (place == 41) {
            fout << "impossible" << endl;
        }
        else {
            for (place = 0; Q > 2*P; place++)
                Q >>= 1;
            place++;
            fout << place << endl;
        }
    }
}