#include<iostream>
using namespace std;

char s[2000];
void solve(int test)
{
	int N;
	scanf("%d%s",&N,&s);
	int count = 0, answer = 0;
	for(int i = 0; i <=N; i++)
	{
		if(count < i)
		{
			answer += (i-count);
			count = i;
		}
		count += (s[i]-'0');
	}
	printf("case #%d: %d\n",test, answer); 
}



int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int i = 1; i <= T; i++) solve(i);
	return 0;
}