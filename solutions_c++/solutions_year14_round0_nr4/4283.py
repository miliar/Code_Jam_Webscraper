#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		int N;
		cin>>N;
		int cheatScore=0,noCheatScore=0;
		float A[1001],B[1001];
		for(int i=0;i<N;i++)
			cin>>A[i];
		for(int i=0;i<N;i++)
			cin>>B[i];
		sort(A,A+N);
		sort(B,B+N);
		
		for(int a=0,bBegin=0,bEnd=N-1;a<N&&bBegin<=bEnd;)
		{
			if(A[a]<=B[bBegin])
			{
				a++;
				bEnd--;

			}
			else if(A[a]>B[bBegin])
			{
				a++;
				cheatScore++;
				bBegin++;
				
			}

		}
		for(int a=0,b=0;a<N&&b<N;)
		{
			if(A[a]<B[b])
			{
				a++;
				b++;
			}
			else 
			{
				noCheatScore++;
				b++;
			}
		}
		cout<<"Case #"<<t<<": "<<cheatScore<<" "<<noCheatScore<<endl; 
	}
	return 0;
}