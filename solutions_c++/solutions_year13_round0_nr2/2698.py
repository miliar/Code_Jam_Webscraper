#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <math.h>
#include <queue>
#include <cstdio>


#define sqr(t) ((t)*(t))
#define INF INT_MAX
using namespace std;

int i, j, q, poi, X, O, n, p, r, N, t, M, T;
int  arr[101][101], st[101], str[101], stMin[101], strMin[101], arr2[101], pp, zz;

int main ()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin>>T;
	for (q=0; q<T; q++)
	{
		cin>>M>>N;
		zz=0;
		for (i=0; i<M; i++)
		{
			str[i]=1;
			strMin[i]=100;
		}

		for (i=0; i<N; i++)
		{
			st[i]=1;
			stMin[i]=100;
		}

		for (i=0; i<M; i++)
			for (j=0; j<N; j++)
			{
				cin>>arr[i][j];
				if (arr[i][j]>str[i])
					str[i]=arr[i][j];
				if (arr[i][j]<strMin[i])
					strMin[i]=arr[i][j];

				if (arr[i][j]>st[j])
					st[j]=arr[i][j];
				if (arr[i][j]<stMin[j])
					stMin[j]=arr[i][j];
			}
		pp=-1;
		for (i=0; i<M; i++)
			if (str[i]>strMin[i])
			if (zz != 1)
			{
				for (r=0; r<N; r++)
				{
					if (arr[i][r]!=str[i])
					{
						pp++;
						arr2[pp]=r;
					}
				}

				for (j=0; j<=pp; j++)
				if	(stMin[arr2[j]]!=st[arr2[j]])
					{
						cout<<"Case #"<<q+1<<": NO"<<endl;
						zz=1;
						break;
					}
			}


		if (zz==0)
			cout<<"Case #"<<q+1<<": YES"<<endl;
	}

}
		