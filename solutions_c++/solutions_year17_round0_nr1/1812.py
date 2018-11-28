#include<bits/stdc++.h>

using namespace std;

int N,K;
string S;
int res;

int main()
{
	int testN;

	cin >> testN;


	for(int test=1; test<=testN; test++)
	{
		cin >> S >> K;

		N = S.size();
		res = 0;

		queue<int> Q;
		bool flag = false;

		for(int i=0; i<N; i++)
		{
			if(!Q.empty() && Q.front()+K <= i)
				Q.pop();

			if( (Q.size() & 1) + (S[i]=='-') == 1 )
			{
				if(i+K > N) 
				{
					flag = true;
					break;
				}

				Q.push(i);
				res++;
			}
		}


		cout << "Case #" << test << ": ";

		if(flag) 
			cout << "IMPOSSIBLE" << endl;

		else 
			cout << res << endl;
	}
}
