#include<bits/stdc++.h>
using namespace std;

int N;
int ans;

void add_rev(int K,char input[100])// how many string has to be reversed
{
	stack<char> Stack;
	for(int i=0;i<=K;++i)
		Stack.push(input[i]);
	int i=0;
	while(!Stack.empty())
	{
		char C=Stack.top();
		if(C=='+')
			C = '-';
		else
			C = '+';
		input[i++] = C;
		Stack.pop();
	}
}

void Solve_1(int K)
{
	char input[100];
	ans = 0;
	scanf("%s",input);
	N = strlen(input);
	printf("Case #%d: ",K);
	while(true)
	{
		int i=0,cnt=0;
		char prev = input[0];
		
		for(i=1;i<N;++i)
		{
			if(input[i] != prev)
			{
				break;
			}
		}
		

		//cout<<cnt<<"  i   "<<i<<"  N  "<<N<<"     "<<input<<"    "<<   ans<<endl;
		if(i == N)
		{
			if(input[0]=='-')
				ans = ans+1;
			printf("%d\n",ans);
			return;
		}
		else
		{
			add_rev(i-1,input);
			ans=ans+1;
		}
	}

}


int main()
{
	int T;
	scanf("%d",&T);
	
	for(int i=1;i<=T;++i)
		Solve_1(i);
}