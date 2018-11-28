#include <cstdio>
#include <iostream>
using namespace std;

#define H 10

void test(int *hist, int cost, int *minCost);

void test(int *hist, int cost, int *minCost) {
	int newHist[H];
	
//	printf("push\n");
	
	//option 1 -- everyone eats
	newHist[H-1] = 0;
	for (int i=H-2; i>=0; i--) newHist[i] = hist[i+1];
	
//	printf("option 1 cost %d:", cost+1); for (int i=1; i<H; i++) printf(" %d", newHist[i]); printf("\n");
	
	bool done = true;
	for (int i=1; i<H; i++) if (newHist[i]) { done = false; break; }
	if (done) {
		if (cost+1 < *minCost) *minCost = cost+1;
	}
	else {
		if (cost+1 < *minCost) test(newHist, cost+1, minCost);
	}
	
	//option 2 -- remove some of the pancakes from the plate with the most
	int max = 0, lowerSplitLargest;
	for (int i=1; i<H; i++) if (hist[i]) max = i;
	if (max >= 2 && cost+1 < *minCost) {
		lowerSplitLargest = max / 2;
		for (int split = lowerSplitLargest; split >= 1; split--) {
			for (int i=0; i<H; i++) newHist[i] = hist[i];
			int amountA = split;
			int amountB = max - amountA;
			newHist[max]--;
			newHist[amountA]++;
			newHist[amountB]++;
		//	printf("max %d, amount %d %d\n", max, amountA, amountB); printf("option 2 cost %d:", cost+1); for (int i=1; i<H; i++) printf(" %d", newHist[i]); printf("\n");
			
			test(newHist, cost+1, minCost);
		}
	}
//	printf("pop\n");
}




int main(void) {
	int T;
	cin >> T;
	int D, hist[H], p;
	int minCost;
	for (int t=1; t<=T; t++) {
		cin >> D;
		for (int i=0; i<H; i++) hist[i] = 0;
		minCost = 0;
		for (int i=0; i<D; i++) {
			cin >> p;
			hist[p]++;	//histogram
			if (p > minCost) minCost = p;	//initial solution -- everyone only eats
		}
		
	//	printf("init hist cost %d:", minCost); for (int i=1; i<H; i++) printf(" %d", hist[i]); printf("\n");
		
		test(hist, 0, &minCost);
		
		printf("Case #%d: %d\n", t, minCost);
	}
	return 0;
}