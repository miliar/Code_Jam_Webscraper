#include <stdio.h>
#include <vector>
#include <algorithm>
#include <stdlib.h>
using namespace std;


char let='A';
class sen{
public:
	int Pi;
	char letter;
	bool operator<(const sen& b) {
		return this->Pi>b.Pi;
	}

};
vector<sen> A;
int choose(int N)
{
	for(int i=1;i<N;i++)
	{
		if(A[i].Pi!=0)
			return i;
	}
}
void solve(int N,int sum)
{
	sort(A.begin(),A.end());
	sum=sum-A[0].Pi;
	bool k =sum!= A[0].Pi;
	int last=N-1;
	while(k)
	{
		if(A[last].Pi!=0)
		{
			printf("%c ",A[last].letter);
			A[last].Pi--;
				sum--;
		}
		else
			last--;
	k =sum != A[0].Pi;
	}
	while(A[0].Pi)
	{
		if(A[last].Pi!=0){
		printf("%c%c ",A[0].letter,A[last].letter);
		A[last].Pi--;
		A[0].Pi--;
		}
		else
			last--;
	}

}


int main()
{
	int N;
	scanf("%d",&N);
	for(int i=1;i<=N;i++)
	{
		int T;
		scanf("%d",&T);
		A.resize(T);
		int sum=0;
		for(int j=0;j<T;j++)
		{
			scanf("%d",&A[j].Pi);
			sum+=A[j].Pi;
			A[j].letter= let + j;
		}
		printf("Case #%d: ",i);
		solve(T,sum);
		printf("\n");
	}
}

