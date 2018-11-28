#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <sstream>
#include <algorithm>
#include <strings.h>
#include <stdlib.h>
#include <math.h>
#include <set>
#include "bigint/BigIntegerLibrary.hh"

using namespace std;

struct info {
	BigInteger origin;
	BigInteger end;
	BigInteger n;
};


BigInteger costS(BigInteger i, BigInteger j, BigInteger n){
	if (i == j){
		return 0;
	} else if (j - i == 1){
		return (n);
	} else {
		BigInteger dist = j - i;
		BigInteger first = n;
		BigInteger last = n - (dist - 1);
		BigInteger cost = ((first + last) * (dist) / 2);
		return cost;
	}
}
int main(){
	int T;
	cin >> T;
	for (int i = 0; i < T; i++){
		vector<info> list;
		long nStations;
		cin >> nStations;
		int nInfo;	
		cin >> nInfo;
		BigInteger realCost = 0;
		map<BigInteger, BigInteger> originToPeople;
		map<BigInteger , BigInteger> endToPeople;
	
		set<BigInteger> realStations;
		for (int j = 0; j < nInfo; j++){
			long tmporigin, tmpend, tmpn;
			cin >> tmporigin >> tmpend >> tmpn;
			info tmp;
			tmp.origin = tmporigin;
			tmp.end = tmpend;
			tmp.n = tmpn;
			list.push_back(tmp);
			originToPeople[tmp.origin] += tmp.n;
			endToPeople[tmp.end] += tmp.n;
			realCost += tmp.n * costS(tmp.origin, tmp.end, nStations);
			realStations.insert(tmp.origin);
			realStations.insert(tmp.end);
		}
		vector< pair<BigInteger, BigInteger> > cardList;
		BigInteger cost = 0;
	
		for (set<BigInteger>::iterator k = realStations.begin(); k != realStations.end(); k++){
			if (originToPeople[*k] != 0){
				cardList.push_back(pair<BigInteger, BigInteger> (*k, originToPeople[*k]));
			}
			//Remove from the end
			BigInteger pending = endToPeople[*k];
			while(pending != 0){
				for (int j = (unsigned int)cardList.size() - 1; j >= 0; j--){
					if (pending < cardList[j].second){
						cost += (pending * costS(cardList[j].first, *k, nStations));
						cardList[j].second -= pending;
						pending = 0;
					} else {
						cost += (cardList[j].second * costS(cardList[j].first, *k, nStations));
						pending -= cardList[j].second;
						cardList.pop_back();
					}
				}
			}
		}
		cout << "Case #" << (i + 1) << ": " << (realCost - cost) % 1000002013 << endl; 
	}
}
