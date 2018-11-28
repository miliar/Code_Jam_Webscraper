using namespace std;
#include <cstdio>
#include <iostream>
#include <cstring>
#include <queue>
int arr[1000007];

#define INF 1000007

int reverse(int n) {
	int r = 0;
	while(n) {
		r = r*10 + n%10;
		n /= 10;
	}
	return r;
}

int main() {
	int tc;
	cin>>tc;
	for(int i = 0;i<=1000000; i++)
		arr[i] = INF;
	queue<int> q;
	q.push(1);
	arr[1] = 1;
	for(int t = 1;t<=tc;t++) {
		int i;
		cin>>i;
		while(arr[i] == INF) {
			int x = q.front();
			q.pop();
			if(arr[x+1] > arr[x]+1) {
				arr[x+1] = arr[x]+1;
				q.push(x+1);
			}
			int r = reverse(x);
			if(arr[r] > arr[x]+1) {
				arr[r] = arr[x]+1;
				q.push(r);
			}			
		}
		printf("Case #%d: %d\n", t, arr[i]);
	}
	return 0;
}