#include<iostream>
#include<cstdio>
#include<vector>
#include<cstdlib>
#include<cmath>
#include<iomanip>
#include<algorithm>
#include<set>
#include<queue>
#include<map>
#include<deque>

using namespace std;

#define VI vector<int>
#define PI pair<int,int>
#define F first
#define S second
#define MP make_pair
#define LL long long
#define PB push_back
#define VB vector<bool>

int main()
{
	freopen("/Users/Sharat/GoogleDrive/Coding/C++/Contests/GCJ2016/pancakes_input2.txt", "r", stdin);
	freopen("/Users/Sharat/GoogleDrive/Coding/C++/Contests/GCJ2016/pancakes_output2.txt", "w", stdout);
	int cases;
	scanf("%d", &cases);
	for(int t=1;t<=cases;t++){
		VB v;
		string s;
		cin>>s;
		int sz = s.size();
		for(int i=0;i<sz;i++){
			v.PB((s[i] == '+'));
		}
//		printf("v is: "); for(int i=0;i<sz;i++)	printf("%d ", (int)v[i]); printf("\n");

		VB::iterator it = unique(v.begin(),v.end());
		sz = it - v.begin();
//		printf("v is: "); for(int i=0;i<sz;i++)	printf("%d ", (int)v[i]); printf("\n");

        printf("Case #%d: %d\n", t, sz - v[sz-1]);
	}
    return 0;
}
