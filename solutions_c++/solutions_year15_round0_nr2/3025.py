#include <cstdio>
#include <algorithm>
#include <set>
using namespace std;
int P[1111];
int slove( int D, int  P[]){
	sort( P, P + D);
	multiset<int> maxHeap;
	int ans = P[D-1];
	for(int i = 1; i < P[D - 1];i++){
		maxHeap.clear();
		for(int i = 0; i < D; i++)
			maxHeap.insert(P[i]);
		int move = 0;
		while(true){
			multiset<int>::iterator top = maxHeap.end();
			top--;
			if(move + i >= ans || *top <= i)break;
			move++;
			maxHeap.insert(i);
			maxHeap.insert(*top - i);
			maxHeap.erase(top);
		}
		if(move + i < ans)ans = move + i;
	}
	return ans;
}
int main(){
	int T;
	scanf("%d", &T);
	for(int caseT = 1; caseT <= T; caseT++){
		int D;
		scanf("%d", &D);
		for(int i = 0; i < D; i++)
			scanf("%d", P + i);
		printf("Case #%d: %d\n", caseT, slove( D, P));
	}
	return 0;	
}