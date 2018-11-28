#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <assert.h>

const int INF = 1e9;

using namespace std;

int total = 37;
int mult = 36;

double getProb( vector<long long> &bets, vector<long long> &myBets )
{
	long long minBet = bets[0] + myBets[0];
	double res = 0;
	for( int i = 0; i < bets.size(); i++ ) {
		minBet = min( minBet, bets[i] + myBets[i] );
		res += -myBets[i];
	}
	int count  = 0;
	for( int i = 0; i < bets.size(); i++ ) {
		if( bets[i] + myBets[i] == minBet ) {
			count++;
		}
	}
	for( int i = 0; i < bets.size(); i++ ) {
		if( bets[i] + myBets[i] != minBet ) {
			continue;
		}
		res += 1. * myBets[i] * 36 / count;
	}
return res;	
	for( int i = 0; i < myBets.size(); i++ ) {
		cerr << myBets[i] << " ";
	}
	cerr << endl << res << endl;

	return res;
}

int main()
{
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );

	int t;
	cin >> t;
	for( int tt = 1; tt <= t; tt++ ) {
		cerr << "Test:" << tt << endl;
		long long cash;
		int n;
		cin >> cash >> n;
		vector<long long> bets( total, 0 );
		for( int i = 0; i < n; i++ ) {
			cin >> bets[i];
		}
		sort( bets.begin(), bets.end() );

		if( false && true ) {
			cerr << cash << endl;
			for( int i = 0; i < bets.size(); i++ ) {
				cerr << bets[i] << " ";
			}
			cerr << endl;
		}
		double res = 0;
		for( int i = 0; i < bets.size(); i++ ) {
			long long addCash = 0;
			for( int j = 0; j <= i; j++ ) {
				addCash += bets[j];
			}
			long long minAdd = bets[i];
			long long maxAdd = i < bets.size() - 1 ? bets[i + 1] - 1 : cash + addCash;
			long long maxTry = min( (cash + addCash) / ( i + 1 ), maxAdd );
			if( maxTry < minAdd ) {
				continue;
			}
/*			
			for( int k = 0; k < 2; k++ ) {
				long long add = k == 0 ? minAdd : maxTry;
				vector<long long> myBets( total, 0 );
				long long deltaCash = cash;
				for( int j = 0; j <= i; j++ ) {
					myBets[j] = add - bets[j];
					deltaCash -= myBets[j];
				}
				res = max( res, getProb( bets, myBets ) );
				for( int j = i; j >= 0; j-- ) {
					if( deltaCash == 0 ) {
						break;
					}
					assert( deltaCash > 0 );
					myBets[j]+= 1;
					deltaCash--;
					res = max( res, getProb( bets, myBets ) );
				}
			}
		*/	
			for( long long  add = minAdd; add <= maxTry; add++ ) {
//				long long add = k == 0 ? minAdd : maxTry;
				vector<long long> myBets( total, 0 );
				long long deltaCash = cash;
				for( int j = 0; j <= i; j++ ) {
					myBets[j] = add - bets[j];
					deltaCash -= myBets[j];
				}
				res = max( res, getProb( bets, myBets ) );
				for( int j = i; j >= 0; j-- ) {
					if( deltaCash == 0 ) {
						break;
					}
					assert( deltaCash > 0 );
					myBets[j]+= 1;
					deltaCash--;
					res = max( res, getProb( bets, myBets ) );
				}
				if( add == minAdd ) {
					add = max( minAdd, maxTry - 2 );
				}
			}
		}
/*
		long long firstBet = bets.back();
		for( int i = 0; i < bets.size(); i++ ) {
			firstBet = bets[i];
			if( firstBet > 0 ) {
				break;
			}
		}
		cerr << "FirstBet: " << firstBet << endl;
		int countOfFree = 0;
		for( int i = 0; i < bets.size(); i++ ) {
			if( bets[i] == 0 ) {
				countOfFree++;
			}
		}
		double res = 0;
		if( countOfFree > 0 && firstBet > 1 ) {
			long long maxTry = min( cash / countOfFree, firstBet - 1 );
			cerr << "maxTry: " << maxTry << endl;
			for( int i = 0; i < countOfFree; i++ ) {
				myBets[i] = maxTry;
				cash -= maxTry;
			}
			res = max( res, getProb( bets, myBets ) );
		}
			
		while( cash > 0 ) {
			long long start = myBets[0] + bets[0];
			int indexEnd = bets.size() - 1;
			for( int i = 0; i < bets.size(); i++ ) {
				if( bets[i] + myBets[i] > start + 1 ) {
					indexEnd = i;
					break;
				}
			}
			if( indexEnd == 0 ) {
				break;
			}
			long long end = myBets[indexEnd] + bets[indexEnd];
			long long delta = end - start;
			long long maxTry = min( cash / indexEnd, delta - 1 );
			if( maxTry == 0 ) {
				break;
			}
			for( int i = 0; i < countOfFree; i++ ) {
				myBets[i] += maxTry;
				cash -= maxTry;
			}
			res = max( res, getProb( bets, myBets ) );
		}
*/
		printf( "Case #%d: ", tt );
		printf( "%.8lf", res );
		cout << endl;
	}
	return 0;
}

