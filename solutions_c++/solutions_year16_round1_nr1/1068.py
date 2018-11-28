#include<iostream>
#include<cstdio>
#include<vector>
#include<cstdlib>
#include<cmath>
#include<iomanip>
#include<algorithm>
#include<set>
#include<iomanip>
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
#define VS vector<string>
#define VVS vector<VS>
#define MAXN 1024

int main()
{
	freopen("/Users/Sharat/GoogleDrive/Coding/C++/Contests/GCJ2016/A_input2.txt", "r", stdin);
	freopen("/Users/Sharat/GoogleDrive/Coding/C++/Contests/GCJ2016/A_output2.txt", "w", stdout);
	int cases;
	scanf("%d", &cases);

	for(int casenum=1;casenum<=cases;casenum++){
		string a;
		cin>>a;
		int N = a.size();
		string b = "";
		b = b + a[0];
		for(int i=1;i<N;i++){
			if(a[i] >= b[0]){
				b = a[i] + b;
			}
			else{
				b = b + a[i];
			}
		}
		/*
		char* s = new char[MAXN];
		for(int i=0;i<N;i++){
			s[i] = b[i];
		}
		s[N] = '\n';
		*/
		//printf("Case #%d: %s", casenum, s);
		cout<<"Case #"<<casenum<<": "<<b<<endl;
	}

	return 0;
}
