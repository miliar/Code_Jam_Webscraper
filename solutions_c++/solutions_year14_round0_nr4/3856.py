#include <bits/stdc++.h>

using namespace std;

void solve()
{
	int N;
	double A[1001], B[1001];
	cin>>N;
	for(int i=0;i<N;++i)
		cin>>A[i];
	for(int i=0;i<N;++i)
		cin>>B[i];
	if(N==1)
	{
		if(A[0]<B[0]) puts("0 0");
		else puts("1 1");
		return;
	}
	std::sort(A,A+N);
	std::sort(B,B+N);

	std::deque<double> AA, BB;

	int Z = 0, Y = 0;
	for(int i=0;i<N;++i)
		AA.push_back(A[i]),
		BB.push_back(B[i]);
	for(int i=0;i<N;++i)
	{
		if(AA.front() < BB.front()) AA.pop_front(), BB.pop_back();
		else AA.pop_front(), BB.pop_front(), Y++;
	}
	
	std::vector<double> a,b;
	for(int i=0;i<N;++i)
		a.push_back(A[i]), b.push_back(B[i]);
	while(!a.empty())
	{
		bool flag = 0;	// flag = 0 means I am not in position to win
		for(int j=0;j<b.size();++j)
			if(b[j]>a[0]){
				flag=1;
				b.erase(b.begin()+j);
				a.erase(a.begin());
				break;
			}
		if(flag==0) break;
	}
	Z = a.size();
	printf("%d %d\n",Y,Z);
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
