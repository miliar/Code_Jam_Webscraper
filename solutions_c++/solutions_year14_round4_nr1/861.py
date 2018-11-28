/*
user  : triveni
date  : 31/05/2014
time  : 19:25:19
*/
#include <bits/stdc++.h>

using namespace std;

#define      pii               std::pair<int,int>
#define      vi                std::vactor<int>
#define      mp(a,b)           std::make_pair(a,b)
#define      X                 first
#define      Y                 second

typedef long long ll;
ll MOD = 1000000007;

void solve()
{
	int N, X;
	cin>>N>>X;
	int A[10009];
	for(int i=0;i<N;++i)
		cin>>A[i];
	if (N==1) {
		cout << 1 << endl;
		return;
	}
	sort(A,A+N);
	int ct = 0;
	int c = 0;
	while(c<N)
	{
		int id=-1;
		for(int i=N-2;i>=c;--i)
			if(A[i]<=X-A[N-1]) {id = i; break;}
		if(id == -1) A[N-1] = -1, c+=1;
		else{A[id] = A[N-1] = -1,
		c += 2;}
		ct++;
		sort(A,A+N);
	}
	cout << ct << endl;
}

int main()
{
	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;++i)
	{
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}