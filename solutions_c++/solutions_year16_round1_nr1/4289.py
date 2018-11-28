#include<bits/stdc++.h>
using namespace std;

int main()
{
	long long t,i,j,k;
	string s;
	scanf("%lld",&t);
	for(j=1;j<=t;j++)
	{
		deque<char> output;
		cin >> s;
		output.push_back(s[0]);
		for(i=1;i<s.length();i++)
			if(s[i]<output.front())
				output.push_back(s[i]);
			else	output.push_front(s[i]);
		printf("Case #%lld: ",j);
		for(i=0;i<output.size();i++)
			printf("%c",output[i]);

		printf("\n");
	}

	return 0;
}
