#include <iostream>
#include <cmath>
#include <queue>
#include <utility>
using namespace std;

int main (){
	int ncases;
	cin >> ncases;
	for(int i = 1; i <= ncases; i++){
		int nparties;
		cin >> nparties;
		priority_queue<pair<int, int> > pq;
		for(int j = 0; j < nparties; j++){
			int numinj;
			cin >> numinj;
			pq.push(make_pair(numinj,j));
		}
		cout << "Case #" << i << ":";
		while(pq.size() > 2 || pq.top().first > 1){
			pair<int,int> tp = pq.top(); pq.pop();
			pair<int,int> sp = pq.top();
			//cout << tp.first << " " << tp.second << " " << sp.first << " " << sp.second << endl;
			if(tp.first == sp.first && tp.first > 1){
				pq.pop();
				tp.first -= 1;
				sp.first -= 1;
				cout << " " << char('A'+tp.second) << char('A'+sp.second);
				if(tp.first > 0) pq.push(tp); 
				if(sp.first > 0) pq.push(sp);
			}else{
				tp.first -= 1;
				cout << " " << char('A'+tp.second);
				if(tp.first > 0) pq.push(tp); 
			}
		}
		pair<int, int> p1 = pq.top(); pq.pop();
		pair<int, int> p2 = pq.top(); pq.pop();
		cout << " " << char('A'+p1.second) << char('A'+p2.second) << endl;
	}

	return 0;
}


