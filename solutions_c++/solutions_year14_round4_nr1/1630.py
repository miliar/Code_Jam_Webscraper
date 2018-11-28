#include<cstdio>
#include<iostream>
#include<queue>
#include<utility>
#include<cstring>
#include<algorithm>

using namespace std;

#define ii pair<int, int>
#define i3 pair<int, ii>
#define ll long long int

int N, X;
int S[10005];

int main(void)
{
	freopen("A2.in", "r", stdin);
	freopen("A2.out", "w", stdout);
	
	int T;
	cin>>T;
	for(int t = 1; t <= T; t++)
	{
		cin>>N>>X;
		int count = 0, begin = 0, end = N-1;
		for(int i = 0; i < N; i++)
		{
			cin>>S[i];
		}
		
		sort(S, S+N);
		
		for(; begin <= end; )
		{
			if(S[end] + S[begin] > X)
			{
				count++;
				end--;
			}
			else
			{
				count++;
				end--;
				begin++;
			}
		}
		cout<<"Case #"<<t<<": "<<count<<endl;
	}
	return 0;
}
