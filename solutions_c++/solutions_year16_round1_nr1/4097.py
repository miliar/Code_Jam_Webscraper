#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t, c=1, n;
	string str;
	char big;
	
	scanf("%d", &t);
	
	while(t--)
	{
		cin>>str;
		vector<char>comb;
		
		printf("Case #%d: ", c);
		++c;
		
		big = str[0];
		
		comb.push_back(big);
		n = str.length();
		
		for(int i=1;i<n;++i)
		{
			if(str[i]>=big)
			{
				big = str[i];
				comb.insert(comb.begin(), str[i]);
			}
			
			else comb.push_back(str[i]);
		}
		
		for(int i=0;i<n;++i)printf("%c", comb[i]);
		printf("\n");
	}
	return 0;
}
