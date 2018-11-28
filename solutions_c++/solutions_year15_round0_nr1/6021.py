#include<iostream>
using namespace std;

int main() {
	int T;
	int Smax;
	char S[1001];
	int clap;
	int result;
	scanf("%d",&T);
	for(int i=0; i<T; i++)
	{
		scanf("%d %s",&Smax, S);	
		clap = 0;
		result = 0;
		for(int j=0; j<=Smax; j++)
		{
			if(Smax <= clap)
				break;
			
			if(j > clap)
			{
				result++;
				clap += S[j] - '0';
				clap++;
			}
			else
			{
				clap += S[j] - '0';
			}
		}
		printf("Case #%d: %d\n",(i+1), result);
	}
	return 0;
}