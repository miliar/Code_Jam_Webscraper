#include<iostream>
#include<cstring>
#include<cstdio>

using namespace std;

int main(void)
{
	freopen("0A.in", "r", stdin);
	freopen("0A.out", "w+", stdout);
	int T = 1, t;
	cin>>t;
	while(t--)
	{
		int N, D = 0, S = 0; string C; cin>>N>>C; 
		for(int i = 0; i <= N; i++)
		{
			D += max(0, i-S);
			S += max(0, i-S);
			S += (C[i]-'0');
		}
		cout<<"Case #"<<T++<<": "<<D<<endl;
	}
	return 0;
}