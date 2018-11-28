#include<bits/stdc++.h>
using namespace std;
#define LL long long
int main(void)
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin>>T;
	int count = 1;
	while(T--)
	{
		cout<<"Case #"<<count++<<": ";
		string S;
		cin>>S;
		int total = 0;
		int N = S.length();
		for(int i=N-1;i>=0;i--)
		{
			if(S[i] == '-')
			{
				S[i] = '+';
				total++;
				int j;
				for(j=i-1;j>=1;j--)
				{
					if(S[j] == '-')
						S[j] = '+';
					else
						break;
				}
				i = j;
				for(int k=i;k>=0;k--)
				{
					if(S[k] == '+')
						S[k] = '-';
					else
						S[k] = '+';
				}
				i++;
			}
		}
		cout<<total<<endl;
	}
	return 0;
}
