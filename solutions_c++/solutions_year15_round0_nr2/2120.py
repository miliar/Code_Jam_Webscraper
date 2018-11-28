#include <stdio.h>
#include <string.h>
#include <memory.h>
#include <queue>
#include <functional>
using namespace std;



#define MAX 1100
int table[MAX][MAX];

struct CakeNode{
	int specialTime;
	int initCakeCount;
	int nodeValue;

	CakeNode(){
		specialTime = 0;
		initCakeCount = 0;
		nodeValue = 0;
	}

	bool operator > (const CakeNode& rhs) const {
		return nodeValue < rhs.nodeValue;
	}
};


int getMinTime(priority_queue<CakeNode, vector<CakeNode>, greater<CakeNode> >& max_heap){
	int bonusTime = 0;
	CakeNode topNode = max_heap.top();
	int minTime = topNode.nodeValue;
	while (bonusTime < minTime){
		topNode = max_heap.top();
		max_heap.pop();
		topNode.specialTime++;
		topNode.nodeValue = table[topNode.initCakeCount][topNode.specialTime];
		if (topNode.initCakeCount - 1 < topNode.specialTime){
			break;
		}
		max_heap.push(topNode);

		bonusTime++;
		if (bonusTime + max_heap.top().nodeValue < minTime){
			minTime = bonusTime + max_heap.top().nodeValue;
		}
	}
	return minTime;
}
//starti
void initSpecialTimeTable(int (*table)[MAX]){
	int number = 1;
	for (int number = 1; number < MAX; number++){
		for (int specialTime = 0; specialTime < MAX && specialTime < number; specialTime++){
			if (specialTime == 0)
				table[number][specialTime] = number;
			else{
				int divide = number / (specialTime+1);
				int bonus = number % (specialTime+1);
				if (bonus == 0){
					table[number][specialTime] = divide;
				}
				else{
					table[number][specialTime] = table[bonus][bonus - 1] + divide;
				}
			}
		}
	}
}

int main(){
	FILE* f = fopen("B-large(1).in", "r");
	FILE* output = fopen("outputlargelast.out", "w");

	initSpecialTimeTable(table);

	int testcase;
	fscanf(f, "%d", &testcase);
	for (int k = 0; k < testcase; k++){
		priority_queue<CakeNode, vector<CakeNode>,	greater<CakeNode> > max_heap;	//
		int peopleCount;
		fscanf(f,"%d", &peopleCount);
		for (int i = 0; i < peopleCount; i++)
		{
			int cakeCount;
			fscanf(f, "%d", &cakeCount);
			CakeNode node;
			node.initCakeCount = cakeCount;
			node.specialTime = 0;
			node.nodeValue = table[cakeCount][0];
			max_heap.push(node);
		}
		int minTime = getMinTime(max_heap);
		fprintf(output, "Case #%d: %d\n", k + 1, minTime);
	}
	fclose(output);
	fclose(f);


	return 0;
}
