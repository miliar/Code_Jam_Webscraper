#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;

struct Node {
	int data;
	Node* next;
	Node* prev;	
	~Node();
	Node(int n):data(n),next(NULL),prev(NULL) {}
};

struct List {
	Node* head;
	Node* tail;
};

void translateNumber(int n, List* list) {
	int copy = n;
	list->head = new Node(copy % 10);
	list->tail= new Node(copy % 10);
	copy /= 10;
	Node* cur = list->head;
	while(copy > 0) {
		int num = copy % 10;
		cur->next = new Node(num);
		cur->next->prev = cur;
		cur = cur->next;
		list->tail = cur;
		copy /= 10;
	}
}

void printDigit(List* list) {
	Node* h = list->head;
	while(h) {
		cerr << h->data << ' ';
		h = h->next;
	}
	cerr << endl;
}

void addList(List* addToList, List* N) {
	Node* aHead = addToList->head;
	Node* nHead = N->head;
	int extra = 0;
	cerr << "beforeAdd" << ' ';
	printDigit(addToList);
	while(nHead) {
		int r = aHead->data + nHead->data + extra;
		extra = r / 10;
		aHead->data = r % 10;
		// cerr << "r: " << r << "extra: "<< extra << endl;
		if (aHead->next) {
			// cerr << "have next" << endl;
			aHead = aHead->next;
		} else {
			aHead->next = new Node(0);
			aHead->next->prev = aHead;
			addToList->tail = aHead->next;
			aHead = aHead->next;
		}
		nHead = nHead->next;
	}
	if (extra) {
		int extraNum = aHead->data + extra;
		aHead->data = extraNum % 10;
		if (extraNum >= 10) {
			aHead->next = new Node(extraNum / 10);
			aHead->next->prev = aHead;
			addToList->tail = aHead->next;
		}
	}
	cerr << "afterAdd" << ' ';
	// printDigit(addToList);
}

void printAnswer(List* list) {
	Node* h = list->tail;
	if (h && h->data == 0) {
		h = h->prev;
	}
	while(h) {
		cout << h->data;
		h = h->prev;
	}
	cout << endl;
}

bool scanList(List* list, bool* digit) {
	Node* h = list->tail;
	if (h && h->data == 0) {
		h = h->prev;
	}
	while(h) {
		digit[h->data] = true;
		h = h->prev;
	}
	for (int i = 0; i < 10; i++) {
		if (digit[i] == false) {
			return false;
		}
	}
	return true;
}

int main(int argc, char* argv[]) {
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		int n;
		cin >> n;
		// cout << "Case #" << i+1 << ": ";
		List* N = new List;
		List* addToList = new List;
		bool digit[10] = {0};
		if (n > 0) {
			translateNumber(n, N);
			translateNumber(n, addToList);
			bool result = scanList(addToList, digit);
			while (!result) {
				// cout << "scan result " << scanList(addToList, digit) << endl;
				addList(addToList, N);
				result = scanList(addToList, digit);
				printDigit(addToList);
			}
			cout << "Case #" << i+1 << ": ";
			printAnswer(addToList);
			// cout << endl;
		} else {
			cout << "Case #" << i+1 << ": ";
			cout << "INSOMNIA" << endl;
		}
	}
}
