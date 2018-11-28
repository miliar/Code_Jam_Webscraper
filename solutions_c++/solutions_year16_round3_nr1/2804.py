#include <cstdio>
#include <iostream>
#include <vector>
#include <queue>
#include <utility>
using namespace std;

class cmp
{
public:
	bool operator() (const pair<int,int>& l, const pair<int,int>& r) const
	{
		return l.second<r.second;
	}
};

void solve(int z){
	int n;
	priority_queue<pair<int,int>,vector<pair<int,int> >,cmp> pq;
	int a;
	cin >> n;
	for(int i=0;i<n;++i){
		cin >> a;
		pq.push(make_pair(i,a));
	}
	printf("Case #%d:",z);
	int party1,party2,n1,n2;
	while(!pq.empty()){
		party1=pq.top().first;
		n1=pq.top().second;
		pq.pop();
		party2=pq.top().first;
		n2=pq.top().second;
		pq.pop();
		if(pq.empty()){
			if(n1-n2){
				printf(" %c",party1+65);
				--n1;
				pq.push(make_pair(party1,n1));
				pq.push(make_pair(party2,n2));
			}
			else{
				printf(" %c%c",party1+65,party2+65);
				--n1;--n2;
				if(n1){
					pq.push(make_pair(party1,n1));
					pq.push(make_pair(party2,n2));
				}
			}
		}
		else{
			if(n1==1){
				printf(" %c",party1+65);
				--n1;
				pq.push(make_pair(party2,n2));
			}
			else if(n2==1){
				printf(" %c%c",party1+65,party1+65);
				--n1;--n1;
				if(n1)
					pq.push(make_pair(party1,n1));
				pq.push(make_pair(party2,n2));
			}
			else{
				printf(" %c%c",party1+65,party2+65);
				--n1;--n2;
				if(n1)
					pq.push(make_pair(party1,n1));
				if(n2)
					pq.push(make_pair(party2,n2));
			}
		}
	}
	cout << endl;
}

int main(){
	int t;
	cin >> t;
	for(int i=1;i<=t;++i)
		solve(i);
	return 0;
}
/*

4
2
2 2
3
3 2 2
3
1 1 2
3
2 3 1

*/