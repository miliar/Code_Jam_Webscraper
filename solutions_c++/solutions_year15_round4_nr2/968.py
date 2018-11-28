#include <bits/stdc++.h>
//#define DEBUG

using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef pair<ll,ll> pll;
typedef vector<ll> vll;



int main()
{
	#ifndef DEBUG

    ifstream in("2b_s3.in");
    cin.rdbuf(in.rdbuf());
    //ofstream out("2b_s.out");
    //cout.rdbuf(out.rdbuf());
	freopen("2b_s3.out","w",stdout);

    #endif
	//cout.precision(15);
	int T;
	cin>>T;
	for(int TX = 1; TX <= T; TX++)
	{
		int N;
		double V,X;
		
		cin>>N>>V>>X;
		int valid1 = 0;
		int valid2 = 0;
		vector < pair<double,double> > A(N);
		for(int i = 0; i < N; i++)
		{
			cin>>A[i].first>>A[i].second;
			if(A[i].second >= X)	valid1 = 1;
			if(A[i].second <= X)	valid2 = 1;
		}
		//cout<<"Case #"<<TX<<": "; 
		printf("Case #%d: ",TX);
		
		if(valid1 == 0 || valid2 == 0)
			//cout<<"IMPOSSIBLE"<<endl;
			printf("IMPOSSIBLE\n");
		else if(N == 1)
		{
			double ans = V/A[0].first;
			printf("%.10lf\n",ans);
		}
		else
		{
			double v0,v1,t0,t1;
			double ans;
			
			if(A[0].second == X)
			{
				ans = V/A[0].first;
				if(A[1].second == X)
				{
					ans = V/(A[0].first + A[1].first);
				}
			}
			else if(A[1].second == X)
			{
				ans = V/A[1].first;
			}
			else
			{
				v1 = V*(A[0].second - X)/(A[0].second - A[1].second);
			
				v0 = V - v1;
				if(v1 > V + 0.000001)
				{
					ans = -1;
				}
				else
					ans = max(v1/A[1].first,v0/A[0].first);
			}
				
			if(ans == -1)
			{
				printf("IMPOSSIBLE\n");
			}
			else
				printf("%.10lf\n",ans);
		
		}
			
	}
	
	return 0;
}