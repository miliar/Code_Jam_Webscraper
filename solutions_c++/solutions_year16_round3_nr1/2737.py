#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <vector>

using namespace std;

const double pi = atan(1.0)*4.0;

int P[26];

int main(){

//	freopen("A-small-attempt0.in", "r", stdin);
//	freopen("A-small-attempt0.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int T;
	scanf("%d",&T);

	for(int t = 1 ; t <= T ; t++){
		int N;
		scanf("%d",&N);

		int num;
		int sum = 0;
		priority_queue<pair<int,int> > pq;
		for(int i = 0 ; i < N ; i++){
			scanf("%d",&num);
			sum += num;
			pq.push(make_pair(num,i));
		}

		int m;
		int par = N;
		printf("Case #%d: ",t);
		while(!pq.empty()){

			pair<int,int> x = pq.top();
			pq.pop();

			x.first--;
			sum--;
			m = sum/2;
			printf("%c",'A'+x.second);
			if(x.first != 0) pq.push(x);

			if(pq.top().first > m){
				pair<int,int> x = pq.top();
				pq.pop();

				x.first--;
				sum--;
				m = sum/2;
				printf("%c",'A'+x.second);
				if(x.first != 0) pq.push(x);
			}

			printf(" ");
		}
		printf("\n");
	}



	return 0;
}
