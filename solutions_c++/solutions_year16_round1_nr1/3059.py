#include <set>
#include <map>
#include <queue>
#include <stack>
#include <math.h>
#include <vector>
#include <stdio.h>
#include <fstream>
#include <iostream>
#include <string.h>
#include <limits.h>
#include <algorithm>
//#include <ext/pb_ds/assoc_container.hpp>
//#include <ext/pb_ds/tree_policy.hpp>
//#include <bits/stdc++.h>

#define ff first
#define ss second
#define ll long long
#define pb push_back
#define mp make_pair
#define inf 1000000007
#define mod 1000000007
#define pii pair <int, int>
#define all(x) x.begin(), x.end()
//#define tr(i,c) for(__typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)

//using namespace __gnu_pbds;

using namespace std;

//template <typename T> using ordered_set =  tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;

int t;
int Case;
char s[1005];

int main()
{
	freopen("word.in", "r", stdin);
	freopen("word.out", "w", stdout);
	scanf("%d", &t);
	
	while (t--) {
		scanf("%s", s);
		
		int n = strlen(s);
		
		deque <char> D;
		
		D.pb(s[0]);
		
		for (int i = 1; i < n; i++) {
			if (s[i] >= D.front())
				D.push_front(s[i]);
			else
				D.pb(s[i]);
		}
		
		printf("Case #%d: ", ++Case);
		while(!D.empty())
			printf("%c", D.front()), D.pop_front();
		
		printf("\n");
	}
}

