#include <stdio.h>
#include <iostream>
#include <queue>
using namespace std;

int K_MAX = 0;
int OPTIMAL = 9999;

void busca(priority_queue<int> q, int k){
	if(k < K_MAX){
		int a = q.top();
		if(a + k < OPTIMAL) OPTIMAL = a + k;
		q.pop();
		for(int i = 1; i <= a / 2; i++){
			priority_queue <int> aux = q;
			aux.push(i);
			aux.push(a - i);
			busca(aux, k + 1);
		}	
	}
}

int main(){
	
	int ct = 0, cn = 0;
	scanf("%d", &ct);
	while(ct--){
		OPTIMAL = 9999;
		int d = 0;
		priority_queue <int> q;
		scanf("%d", &d);
		for(int i = 0; i < d; i++){
			int a = 0;
			scanf("%d", &a);
			q.push(a);
		}
		K_MAX = q.top();
		busca(q, 0);		
		printf("Case #%d: %d\n", ++cn, OPTIMAL);
	}
	
	return 0;
}