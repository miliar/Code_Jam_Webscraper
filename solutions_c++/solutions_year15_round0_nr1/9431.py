#include <cmath>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <deque>
#include <queue>
#include <functional>
#include <map>
#include <bitset>
#include <stack>
using namespace std;
#define fr(a,b,c) for(int a=b;a<c;a++)
const int infinity = 0x3f3f3f3f;
typedef long long ll;

int t,n;
char line[1010];

int main() {
	scanf("%d", &t);
	fr(ca, 1, t+1) {
		scanf("%d ", &n);
		cin.getline(line, 1010);
		int resp = 0;
		int count = 0;
		fr(i,0,n+1) {
			int at = line[i]-'0';
			if(count >= i) {
				count += at;
			} else {
				resp += i-count;
				count += (i-count) + at;
			}
			
		}
		printf("Case #%d: %d\n", ca, resp);
	}
}
