#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <cmath>
#include <cstdio>
#include <cstring>
#include <vector>
#include <functional>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <cassert>
#include <map>
#include <deque>
#include <queue>
#include <set>
#include <stack>

using namespace std;

typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<vii> vvii;
typedef pair<int,ii> iii;
typedef unsigned int uint;

#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 
#define MAX_DISTANCE (300000)

class FenwickTree {
private:
	vi tree;
public:
	FenwickTree(int n, int init = 0): tree(n+1, init) {
		// store the real size of the tree
		tree[0] = n;
	}
	
	int get(int index) {
		index++;
		
		int sum = 0;
		while (index > 0){
			sum += tree[index];
			index &= index - 1;
		}
		return sum;
	}
	
	void set(int index ,int value) {
		index++;
		while (index < tree.size()){
			tree[index] += value;
			index += (index & -index);
		}
	}
	
	int operator[](int index){ 
		index++;
		int sum = tree[index];
		int z = index - (index & -index);
		index--;
		while (index != z) {
			sum -= tree[index]; 
			index -= (index & -index);
		}
		return sum;
	}
	
	int find (int freq) {
		int low = -1, high = tree[0];
		while (high - low > 1) {
			int mid = (low + high) / 2;
			int x = get(mid);
			
			if (x >= freq)
				high = mid;
			else
				low = mid;
		}
		
		return high;
	}
	
};

inline int isVowel(char c) {
	switch(c) {
		case 'a':
		case 'e':
		case 'i':
		case 'o':
		case 'u':
			return 1;
		default:
			return 0;
	}
}

int naive(char * name, int n) {
	int len = strlen(name);
	int count = 0, sum = 0;
	for (int x = 0; x < len; x++) {
		for (int y = x + n - 1; y < len; y++) {
			sum = 0;
			for (int z = x; z <= y; z++) {
				if (isVowel(name[z])) {
					sum = 0;
				} else {
					sum++;
				}

				if (sum >= n) {
					count++;
					break;
				}
			}
		}
	}
	
	return count;
}

int dp(char * name, int n) {
	int len = strlen(name);
	FenwickTree ft(len);
	int sum = 0;
	for (int x = 0; x < len; x++) {
		sum =  (isVowel(name[x])) ? 0: (sum + 1);
		if (sum >= n) {
			ft.set(x + 1, 1 + ft.get(x));
		}
	}
	
	return ft.get(len);
}

int main(void) {
	
	int x, y, z;
	int numCases;
	unsigned int i, j, k;
	
	scanf("%d", &numCases);
	for (int T = 1; T <= numCases; T++) {
		//string name;
		char name[1000000];
		int n;
		
		memset(name, 0x00, sizeof(name));
		scanf("%s %d", name, &n);
		
		int v = naive(name, n);
		//int w = dp(name, n);
		printf("Case #%d: %d\n", T, v);
	}

	return 0;
}