#include<iostream>
#include<cstdio>


using namespace std;

int main ()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int test,tests;
	scanf ("%d", &tests);
	for (test = 1; test <= tests; test++)
	{
		int K,C,S;
		scanf("%d", &K);
		scanf("%d", &C);
		scanf("%d", &S);
		printf("Case #%d: ",test);
		for (int i=1; i <=K; i++)
			printf("%d ",i);
		printf("\n");
	}
	
}

