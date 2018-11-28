#include <cstdio>
#include <memory>
#include <string>
#include <string>
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <vector>

#define N 111111111

using namespace std;

int target;
int queue[N];
int queue_count[N];
int checker[N];
int head, tail;
void process();
int result;

void input();
int min(int a, int b);
int getResult(int current);
int intReserver(int value);

ifstream in("input.txt");
ofstream out("output.txt");

int main() {
	int i, T;
	in >> T;
	for (i = 0; i < T; i++) {
		cout << "current:" << i + 1 << endl;
		input();
		process();
		out << "Case #" << i + 1 << ": " << result << endl;
	}
	return 0;
}

void input() {
	in >> target;
}

void process() {
	memset(queue, 0x00, sizeof (queue));
	memset(queue_count, 0x00, sizeof(queue_count));
	memset(checker, 0x00, sizeof(checker));

	result = target;
	head = tail = 0;
	queue_count[tail] = 1;
	queue[tail++] = 1;
	checker[1] = 1;
	while (head < tail) {
		int current = queue[head];
		int currentCount = queue_count[head++];
		if (current == target) {
			result = currentCount;
			return;
		}
		int next = current + 1;
		if (checker[next] == 0) {
			checker[next] = 1;
			queue_count[tail] = currentCount + 1;
			queue[tail++] = next;
		}
		next = intReserver(current);
		if (checker[next] == 0) {
			checker[next] = 1;
			queue_count[tail] = currentCount + 1;
			queue[tail++] = next;
		}
	}
}

int intReserver(int value) {
	string str = to_string(value);
	reverse(str.begin(), str.end());
	int ret = stoi(str);
	return ret;
}

/*
Input

Output

3
1
19
23

Case #1: 1
Case #2: 19
Case #3: 15
*/