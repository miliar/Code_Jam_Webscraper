#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	cin>>t;

	for(int c=0;c<t;c++)
	{
		string S;
		cin>>S;

		vector <int> A;

		for(int i=1;i<S.size();i++)
			if(S[i] != S[i-1])
				if(S[i] == '+')
					A.push_back(1);
				else
					A.push_back(0);

		if(S[S.size()-1] == '+')
			A.push_back(1);
		else
			A.push_back(0);
		
		int x = A.size() - A[A.size()-1];

		printf("Case #%d: %d\n",c+1,x);
	}	
}