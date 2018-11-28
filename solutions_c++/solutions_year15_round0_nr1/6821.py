#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int N, S, v[1010];
string str;

int main()
{
	freopen("A-large.in", "r", stdin );
	freopen("out_large.txt", "w", stdout);
	cin>>N;
	for( int T = 1; T <= N; T++ )
	{
		memset(v, 0, sizeof(v));
		cin>>S>>str;
		for( int i = 0; i<= S; i++ )
		{
			v[i] = str[i]-'0';
		}

		int invite = 0, cnt = 0;
		for( int i = 0; i < S; i++ )
		{
			cnt += v[i];
			if( cnt < i+1 ) 
			{
				invite += i+1-cnt;
				cnt += i+1-cnt;
			}
		}
		cout<<"Case #"<<T<<": "<<invite<<endl;
	}

	return 0;
}