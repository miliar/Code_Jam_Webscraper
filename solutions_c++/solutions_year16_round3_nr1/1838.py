#include <iostream>
#include <queue>
#include <cstdio>
#include <algorithm>
#include <utility>

using namespace std;

typedef pair<int, char> pic;

int main(){
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		int N;
		priority_queue<pic> pq;
		cin >> N;
		for(int i=0;i<N;i++){
			int x;
			cin >> x;
			pq.push(make_pair(x, (char)('A' + i)));
		}

		cout << "Case #" << t << ": ";
		while(!pq.empty()){
			pic cur = pq.top();
			pq.pop();
			if(pq.size()!=1){
				cur.first -= 1;
				cout << cur.second << " ";
				if(cur.first!=0) pq.push(cur);
			}
			else{
				pic next = pq.top();
				pq.pop();
				if(next.first==cur.first){
					cout << cur.second << next.second << " ";
					cur.first -= 1;
					next.first -= 1;
					if(cur.first!=0){
						pq.push(cur);
						pq.push(next);
					}
				}
				else{
					cur.first -= 1;
					cout << cur.second << " ";
					if(cur.first!=0) pq.push(cur);
				}
			}
		}
		cout << endl;
	}
	return 0;
}