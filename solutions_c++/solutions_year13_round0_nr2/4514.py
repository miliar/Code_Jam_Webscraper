//============================================================================
// Name        : code_jam_b.cpp
// Author      : wfy
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int main()
{
	int arr[110][110],maxi[110],maxj[110];
	int T,n,m;
	scanf("%d",&T);
	for(int kk=1;kk<=T;kk++)
	{
		printf("Case #%d: ",kk);
		memset(maxi,-1,sizeof(maxi));
		memset(maxj,-1,sizeof(maxj));
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++)
			{
				scanf("%d",&arr[i][j]);
				maxi[i]=max(maxi[i],arr[i][j]);
				maxj[j]=max(maxj[j],arr[i][j]);
			}
		int i,j;
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				if(arr[i][j]<maxi[i]&&arr[i][j]<maxj[j]) break;
			}
			if(j<m) break;
		}
		if(i<n) printf("NO\n");
		else printf("YES\n");
	}
	return 0;
}
