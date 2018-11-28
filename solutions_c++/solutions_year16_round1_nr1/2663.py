#include <climits>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>

#define io_r freopen("input.txt","r",stdin);
#define io_w freopen("output.txt","w",stdout);
#define io_file io_r; io_w;

#define PB push_back
#define MP make_pair
#define ll long long

#define rep(i,n) for (int i = 0; i<n; ++i)
#define clr(x, y) memset(x, y, sizeof x)
#define all(x) (x).begin(), (x).end()

#define MAX 1010
#define MOD 1000000007

using namespace std;

char s[MAX];

int main (){
	int T;
	scanf("%d", &T);
	
	int v[30];
	rep(k, T){
		printf("Case #%d: ", k+1);
		scanf("%s", s);
		int sz = strlen(s);
		deque<char> q;
		deque<char> :: iterator it;
		
		q.push_front(s[0]);
		for(int i = 1; i<sz; i++){
			if(s[i] >= q.front()) q.push_front(s[i]);
			else q.push_back(s[i]);
		}
		
		for(it = q.begin(); it != q.end(); it++)
			putchar(*it);
		puts("");
	}

	return 0;
}
