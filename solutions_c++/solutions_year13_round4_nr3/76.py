#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

const int MAXN = 2020;
int T, N;
int A[MAXN], B[MAXN], Asub[MAXN], Bsub[MAXN];
int tmpa[MAXN], tmpb[MAXN];
int num[MAXN];

int main()
{
    ios_base::sync_with_stdio(0);

    cin>>T;
    for(int t=1; t<=T; t++)
	{
		cin>>N;
		for(int i=0; i<N; i++)cin>>A[i];
		for(int i=0; i<N; i++)cin>>B[i];
		for(int i=0; i<N; i++)num[i] = Asub[i] = Bsub[i] = 0;

		for(int i=1; i<=N; i++)
		{
			/*int b = 123456789;
			for(int j=0; j<N; j++)
			{
				if(num[j])continue;
				b = min(b, B[j]);
				tmpb[j] = b;
			}*/
			int a = 123456789;
			for(int j=N-1; j>=0; j--)
			{
				if(!num[j])a = min(a, A[j]);
				tmpa[j] = a;
			}

			int piv = -1;
			for(int j=0; j<N; j++)
			{
				if(A[j]-Asub[j]==1 && B[j]-Bsub[j]==1 && !num[j])
				{
					//if(j>0 && Bsub[j]+1>=tmpb[j-1])continue;
					if(j<N-1 && A[j]>=tmpa[j+1])continue;
					piv = j;
					break;
				}
			}
			if(piv==-1)cout<<"QQQQQQQQQ"<<endl;
			//else cout<<"PIV "<<piv<<" : "<<i<<endl;
			num[piv] = i;
			int Alen = Asub[piv]+1, Blen = Bsub[piv]+1;
			for(int j=0; j<piv; j++)if(num[j]==0)Bsub[j] = max(Bsub[j], Blen);
			for(int j=piv+1; j<N; j++)if(num[j]==0)Asub[j] = max(Asub[j], Alen);

			/*for(int j=0; j<N; j++)
			{
				if(num[j])cout<<0;
				else cout<<A[j]-Asub[j];
				cout<<" ";
			}
			cout<<endl;
			for(int j=0; j<N; j++)
			{
				if(num[j])cout<<0;
				else cout<<B[j]-Bsub[j];
				cout<<" ";
			}
			cout<<endl;*/
		}

		cout<<"Case #"<<t<<": ";
		for(int i=0; i<N; i++)cout<<num[i]<<(i==N-1 ? "\n" : " ");


	}

    return 0;
}
