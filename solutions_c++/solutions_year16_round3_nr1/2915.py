#include <stdio.h>
#include <math.h>
#include <vector>
#include <algorithm>
#include <queue>

#define INF 1987654321

using namespace std;


void run() {
	int N;
	scanf("%d", &N);
	
	//priority_queue<pair<int, int>> pq;
	//vector<char> result;
	vector<int> parties(N, 0);
	
	for (int i=0; i<N; i++) {
		//int d;
		//scanf("%d", &d);
		//pq.push( make_pair(d, i) );
		scanf("%d", &parties[i]);
	}
	
	while (true) {
		vector< pair<int, int> > maxes;
		maxes.push_back( make_pair(-1, -INF) );
		
		
		for (int i=0; i<N; i++) {
			if (maxes[0].second < parties[i]) {
				maxes.clear();
				maxes.push_back( make_pair(i, parties[i]) );
				
			}else if (maxes[0].second == parties[i])
				maxes.push_back( make_pair(i, parties[i]) );
		}
		
		if (maxes[0].second == 0 || maxes[0].first == -1) break;
		
		
		if (maxes.size() % 2 == 0) {
			printf("%c%c ", 'A' + maxes[0].first, 'A' + maxes[1].first);
			parties[ maxes[0].first ]--;
			parties[ maxes[1].first ]--;
			
			
		}else{
			printf("%c ", 'A' + maxes[0].first);
			parties[ maxes[0].first ]--;
			
		}
		
	}
	
	
	/*while (!pq.empty()) {
		int num = pq.top().first;
		int party = pq.top().second;
		pq.pop();
		
		if (num-1 > 0)
			pq.push( make_pair(num-1, party) );
		
		
		result.push_back( 'A' + party );
	}
	
	for (int i=0; i<result.size(); i++) {
		if (i == result.size()-2)
			printf("%c", result[i]);
		else
			printf("%c ", result[i]);
	}*/
}



int main() {
	int test_case;
	scanf("%d", &test_case);
	
	for (int t=1; t<=test_case; t++) {
		printf("Case #%d: ", t);
		run();
		printf("\n");
	}
	
	return 0;
}
