#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

#define SMALL
using namespace std;

int main()
{
	
#ifdef SMALL
	freopen("A-small-practice.in","rt",stdin);
#else
	freopen("B-large-practice.in","rt",stdin);
#endif
	freopen("out.out","wt",stdout);
	
	int N,t=1;
	cin>>N;
	cin.ignore();
	while(N--)
	{
		cout<<"Case #"<<t++<<": ";

		int first,second;
		int A1[4][4],A2[4][4];

		cin>>first;first--;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>A1[i][j];

		cin>>second;second--;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>A2[i][j];

		int found=0,iff=0;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
			{
				if(A1[first][i]==A2[second][j])
				{
					found++;
					iff=i;
				}
			}


			if(found==0)
			{
				cout<<"Volunteer cheated!";
			}
			else if(found==1)
			{
				cout<<A1[first][iff];
			}
			else
			{
				cout<<"Bad magician!";
			}

		cout<<"\n";
	}


	return 0;
}
