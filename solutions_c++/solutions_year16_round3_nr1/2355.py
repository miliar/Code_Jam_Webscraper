#define _CRT_SECURE_NO_WARNINGS

#include<iostream>
#include<math.h>
#include<cstdio>


#define fo(i,n) for(int i=0;i<n;++i)
#define rfo for(int i=n-1;i>=0;--i)

#define max(a,b) (a>b)?(a):(b);
#define min(a,b) (a<b)?(a):(b);

using namespace std;

class party {
public:
	int number;
	char letter;
	bool operator<(party b){
		return number < b.number;
	}
};

int heap_size = 0;
party heap[50009];

void restore_heap(int pos) {
	int son = 2 * pos + 1;
	int maxson = son;
	if (son >= heap_size)return;
	++son;
	if (son<heap_size &&  heap[maxson] < heap [son] )
		maxson = son;
	if (heap[pos] < heap[maxson]) {
		swap(heap[pos], heap[maxson]);
		restore_heap(maxson);
	}
}

void up_restore_heap(int pos) {
	if (pos == 0)return ;
	int parent = (pos - 1) / 2;
	if (heap[parent] < heap[pos]) {
		swap(heap[parent], heap[pos]);
		up_restore_heap(parent);
	}
}



int main()
{

	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin >> t;
	//int non_zero = 0;
	int sum = 0;
	fo(h, t) {
		cout << "Case #" << h + 1 << ": ";
		int n;
		
		cin >> n;
		
		heap_size = 0;
		sum = 0;
		//non_zero = 0;
		fo(i, n) {
			heap_size++;
			cin >> heap[i].number;
			sum += heap[i].number;
			heap[i].letter = 'A' + i;
			up_restore_heap(i);
		}

		bool q = sum % 2;

		while (heap[0].number) {

			

			cout << heap[0].letter;
			if (q && sum>1 )cout << ' ';
			q = !q;
			--heap[0].number;
			--sum;
			restore_heap(0);
			
		//	cout << "\n";
		//	fo(g, n)cout << heap[g].letter << ' ' << heap[g].number << '\n';
		//	cout << "\n";
		}
		if (h + 1 < t)
			cout << '\n';
	}
	cin >> t;
}