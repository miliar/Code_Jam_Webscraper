/*
Code written by briguychau
Google Code Jam 2013 Round 2
*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <algorithm>

typedef struct Pax {
	int stn;
	Pax* next;
} Pax;

void solve(int count) {
	Pax* enter = NULL;
	Pax* exit = NULL;
	
	int N, M, o, e, p;
	scanf("%d %d", &N, &M);
	
	int* stations = (int*)calloc(N + 1, sizeof(int));
	int sum = 0;
	for (int i = 0; i < M; i++) {
		scanf("%d %d %d", &o, &e, &p);
		stations[o] += p;
		stations[e] -= p;
		sum += p * (((e - o) * N) - ((e - o - 1) * (e - o) / 2));
	}
	
	int i = 1;
	int get = 0;
	int diff;
	Pax* list = NULL;
	Pax* temp;
	while (i <= N) {
		if (stations[i] == 0) {
			i++;
			continue;
		}
		if (stations[i] > 0) {
			temp = new Pax;
			temp->stn = i;
			temp->next = list;
			list = temp;
			stations[i]--;
			continue;
		}
		if (stations[i] < 0) {
			temp = list;
			list = temp->next;
			temp->next = NULL;
			diff = i - temp->stn;
			delete temp;
			get += (diff * N) - ((diff - 1) * diff / 2);
			stations[i]++;
		}
	}
	
	printf("Case #%d: %d\n", count, sum - get);
	
	free(stations);
	return;
}

int main() {
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		solve(i);
	}
	return 0;
}

