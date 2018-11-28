#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <utility>
#include <cmath>
#include <list>
#include <map>
#include <vector>
#include <stack>
#include <queue>
using namespace std;
pair<long long, long long> oe[2048];

long long MODULUS = 1000002013;
int main(){
	int T;
	cin >> T;
	
	for(int q=0;q<T;q++){
		long long firstCost = 0;
		long long N, M;
		cin >> N >> M;
		
		for(int i=0;i<M;i++){
			long long O, E, P;
			cin >> O >> E >> P;
			firstCost += ((((N + 1) * (E-O) - ((E - O) * (E - O + 1))/2)%MODULUS)*P)%MODULUS;
			firstCost %= MODULUS;
			oe[2*i] = pair<long long, long long>(O, -P);
			oe[2*i+1] = pair<long long, long long>(E, P);
		}
		sort(oe, oe + 2*M);
		long long secondCost = 0;
		deque<pair<long long, long long> > entry;
		for(int i=0;i<2*M;i++){
			if(oe[i].second < 0){
				entry.push_front(oe[i]);
			} else {
				long long x = oe[i].second;
				long long e = oe[i].first;
				while(!entry.empty() && entry.front().second + x >= 0){
					long long o = entry.front().first;
					secondCost += ((((N + 1) * (e-o) - ((e - o) * (e - o + 1))/2)%MODULUS)*(-entry.front().second))%MODULUS;
					secondCost %= MODULUS;
					x += entry.front().second;
					entry.pop_front();
				}
				if(!entry.empty()){
					long long o = entry.front().first;
					secondCost += ((((N + 1) * (e-o) - ((e - o) * (e - o + 1))/2)%MODULUS)*(x))%MODULUS;
					secondCost %= MODULUS;
					entry.front().second += x;
				}
			}
		}
		
		cout << "Case #" << (q+1) << ": " << (firstCost - secondCost + MODULUS)%MODULUS << endl;
	}
}
