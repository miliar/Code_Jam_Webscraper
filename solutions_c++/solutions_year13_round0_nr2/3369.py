#include<iostream>
#include<string.h>

using namespace std;

struct pattern{
int N,M;
int pt[100][100];
char verd[5];
};

int check_eq(int N, int M, int p[100][100],int q[100][100])
{
	for (int i=0; i<N; ++i)
		for (int j=0; j<M; ++j)
			if(p[i][j] != q[i][j])
				return 0;
	return 1;
}

int main()
{
	int T;
	cin>>T;
	
	pattern patt[T];
	
	for (int run=0; run<T; ++run)
	{
		cin>>patt[run].N>>patt[run].M;

		int p_t[100][100];

		for(int i=0; i<patt[run].N; ++i)
			for(int j=0; j<patt[run].M; ++j)
				cin>>patt[run].pt[i][j];
		
		for (int i=0;i <patt[run].N; ++i)
		{	int max = patt[run].pt[i][0];
			for(int j=0; j<patt[run].M; ++j)
				if(patt[run].pt[i][j] > max)
					max = patt[run].pt[i][j];
			for(int j=0; j<patt[run].M; ++j)
				p_t[i][j] = max;
		}

		for (int j=0;j <patt[run].M; ++j)
		{	int max = patt[run].pt[0][j];
			for(int i=0; i<patt[run].N; ++i)
				if(patt[run].pt[i][j] > max)
					max = patt[run].pt[i][j];
			for(int i=0; i<patt[run].N; ++i)
				{
				if(p_t[i][j] > max)
					p_t[i][j] = max;
				}
				
		}
		if(check_eq(patt[run].N, patt[run].M, patt[run].pt, p_t))
			strcpy(patt[run].verd,"YES");
		else
		strcpy(patt[run].verd,"NO");
		cout<<"Case #"<<run+1<<": "<<patt[run].verd<<'\n';
	}
}
