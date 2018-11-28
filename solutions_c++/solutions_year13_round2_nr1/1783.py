/*
 * osmos.cpp
 *
 *  Created on: 04-May-2013
 *      Author: rahul
 */

#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
using namespace std;
int findMinMoves(int armin, vector<int>& motes, vector<int>::iterator begin) {
		if(begin==motes.end()) return 0;
		if (*begin < armin) {
			armin += *begin;
			return findMinMoves(armin,motes,begin+1);
		} else {
			int newArmin=armin,numOfMoves=0;
			while(newArmin<=*begin){
				newArmin+=(newArmin-1);
				if(newArmin==armin)
					break;
				numOfMoves+=1;
			}

			if(newArmin==armin){
				return numOfMoves,findMinMoves(armin,motes,begin+1)+1;
			}else
				return min(findMinMoves(newArmin+*begin,motes,begin+1)+numOfMoves,findMinMoves(armin,motes,begin+1)+1);
		}

}
int main() {
	int cases;
	cin >> cases;
	for (int i = 0; i < cases; i++) {
		int armin, othersize;
		cin >> armin >> othersize;
		vector<int> othermotes;
		for (int j = 0; j < othersize; ++j) {
			int osize;
			cin >> osize;
			othermotes.push_back(osize);
		}
		sort(othermotes.begin(), othermotes.end());
		int ans=findMinMoves(armin,othermotes,othermotes.begin());
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
}

