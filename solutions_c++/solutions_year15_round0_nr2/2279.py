#include <bits/stdc++.h>

using namespace std;

int t,d,p[1010];
int ans,cur;

int cek(int c){
	// c = number cake per person
	priority_queue<int> pq;
	int f,g,h,z;
	z = 0;
	for (int i=0; i<d; i++){
		pq.push(p[i]);
	}
	for (;;){
		f = pq.top();
		if (f > c){
			pq.pop();
			while (f > c){
				pq.push(c);
				f -= c;
				z++;
			}
		} else break;
	}
	return (z+c);
}

int main(){
	scanf("%d",&t);
	for (int jj=1; jj<=t; jj++){
		scanf("%d",&d);
		for (int i=0; i<d; i++){
			scanf("%d",&p[i]);
		}
		cur = 1000000;
		for (int i=1; i<=1000; i++){
			cur = min(cur,cek(i));
		}
		printf("Case #%d: %d\n",jj,cur);
	}
	return 0;
}
