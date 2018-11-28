#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

#define N 30
#define MAX(a,b) ((a)>(b)?(a):(b))

int size;
struct node
{
	int n;
	int v;
};
node heap[2*N];
int ph[N];
int parent(int i)
{
	return i>>1;
}
int left(int i)
{
	return i<<1;
}
int right(int i)
{
	return (i<<1)+1;
}
void MAX_HEAPIFY(int i)
{
	node temp;
	int big=i;
	if(left(i)<=size&&heap[left(i)].v > heap[i].v)
		big=left(i);
	if(right(i)<=size&&heap[right(i)].v > heap[big].v)
		big=right(i);
	if(big!=i)
	{
		ph[heap[big].n]=i;
		ph[heap[i].n]=big;
		temp=heap[i];
		heap[i]=heap[big];
		heap[big]=temp;
		MAX_HEAPIFY(big);
	}
}
node extract_max()
{
	node max=heap[1];
	heap[1]=heap[size--];
	ph[heap[1].n]=1;
	MAX_HEAPIFY(1);
	return max;
}
bool empty()
{
	return size==0;
}

void insert(node t){
	heap[++size] = t;
	MAX_HEAPIFY(1);
}
int main(){
	int tcase;
	scanf("%d", &tcase);
	for(int icase = 1; icase <= tcase; icase++){
		memset(heap, 0, sizeof(heap));
		size = 0;
		int num;
		scanf("%d", &num);
		int total = 0;
		for(int i = 1; i <= num; i++){
			scanf("%d", &heap[i].v);
			total += heap[i].v;
			heap[i].n = i;
		}
		size = num;
		printf("Case #%d:", icase);
		MAX_HEAPIFY(1);
		while(1){
			node t1 = extract_max();
			node t2 = extract_max();
			node t3;
			t3.v = 0;
			if(!empty()){
				t3 = heap[1];
			}
			if(MAX(t1.v - 2, t2.v) <= (total - 2) / 2){
				printf(" %c%c", t1.n + 'A' - 1, t1.n + 'A' - 1);
				total -= 2;
				if(t1.v - 2 != 0){
					t1.v -= 2;
					insert(t1);
				}
				insert(t2);
			}
			else if(MAX(t1.v - 1, MAX(t2.v - 1, t3.v)) <= (total - 2) / 2){
				printf(" %c%c", t1.n + 'A' - 1, t2.n + 'A' - 1);
				total -= 2;
				if(t1.v - 1 != 0){
					t1.v -= 1;
					insert(t1);
				}
				if(t2.v - 1 != 0){
					t2.v -= 1;
					insert(t2);
				}
			}
			else{
				printf(" %c", t1.n + 'A' - 1);
				total -= 1;
				if(t1.v - 1 != 0){
					t1.v -= 1;
					insert(t1);
				}
				insert(t2);
			}
			if(total == 0){
				printf("\n");
				break;
			}
		}
	}
	return 0;
}
