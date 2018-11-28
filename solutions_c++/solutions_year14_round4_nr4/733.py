#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <string>
using namespace std;

int N, M;
string S[10];
int maxNode, numMaxPath;
int numNode;
int V[10];

int calcNodeServer(int server) {
	string tempS[10];
	int numS = 0;
	int ret = 0;

	for (int i = 0; i < M; i++)
		if (V[i] == server)
			tempS[numS ++] = S[i];

	sort(tempS, tempS + numS);

	ret = (int)tempS[0].size();

	for (int i = 1; i < numS; i++) {
		int minLength = min(tempS[i - 1].size(), tempS[i].size());

		for (int j = 0; j < minLength; j++) {
			if (tempS[i][j] != tempS[i - 1][j]) {
				ret += (int)tempS[i].size() - j;
				break;
			}
			if (j == minLength - 1)
				ret += (int)tempS[i].size() - j - 1;
		}
	}

	return ret;
}

void calcNode(void) {
	numNode = 0;

	for (int i = 1; i <= N; i++)
		numNode += calcNodeServer(i);
}

void getAns(int d, int server, int idx) {

	if (M - d - 1 < N - server)
		return;

	V[idx] = server;

	if (d == M - 1) {
		calcNode();
		if (maxNode == numNode) {
			numMaxPath ++;
		} else if (maxNode < numNode) {
			maxNode = numNode;
			numMaxPath = 1;
		}
	} else {
		for (int i = idx + 1; i < M; i++) {
			if (!V[i]) {
				getAns(d + 1, server, i);
			}
		}

		for (int i = 0; i < M; i++) {
			if (!V[i]) {
				if (server < N)
					getAns(d + 1, server + 1, i);
			}
		}
	}

	V[idx] = 0;
}

int main(void) {
	int testNum;
	scanf("%d", &testNum);
	for (int testCase = 1; testCase <= testNum; testCase++) {

		scanf("%d %d", &M, &N);

		for (int i = 0; i < M; i++) {
			char tempS[100];
			scanf("%s", tempS);
			S[i] = string(tempS);
		}
		maxNode = 0;
		numMaxPath = 0;

		for (int i = 0; i < M; i++) {
			for (int j = 0; j < M; j++)
				V[j] = 0;
			getAns(0, 1, i);
		}

		printf("Case #%d: %d %d\n", testCase, maxNode + N, numMaxPath);

	}

	return 0;
}
