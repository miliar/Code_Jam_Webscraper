#include <bits/stdc++.h>

#define INF 2147483647
#define LLD int
#define clr(a) memset(a,0,sizeof(a))
#define reset(a) memset(a,-1,sizeof(a))

#define PRINT(X) (cout << #X << " -> " << X << endl)
#define PI acos(0)
#define MAX_INT 2147483647
#define SIZE 2001
#define MOD 1000000007

#define BD(i, j) (i >= 0 && i < n && j >= 0 && j < m)

using namespace std;

int main()
{
    int t, tc, x, y, z;
    int i, j, k, h;
    char ch;

#ifndef ONLINE_JUDGE
    freopen("A-large.in", "r", stdin); 
    freopen("output.txt", "w", stdout);
#endif
    
	cin >> tc;
    
	for (t = 1; t <= tc; t++) {
		cin >> x;
		string str;
		cin >> str;
		
		int hired = 0;
		int visited = 0;
		for (i = 0; i < str.size(); i++) {
			int peopleCount = str[i] - '0';
			if (peopleCount != 0 && i > hired + visited) {
				hired += i - (hired + visited);
			}
			visited += peopleCount;
		}
		
		printf("Case #%d: %d\n", t, hired);
	}
    
    return 0;
}