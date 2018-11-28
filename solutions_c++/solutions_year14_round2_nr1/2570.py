#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<set>
#include<map>
#include<deque>
#include<stack>
#include<queue>
#include<algorithm>
#include<utility>
#include<vector>
#include<iostream>
using namespace std;


int main()
{
	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;i++)
	{
		int N,j,k,x,y,z,sum=0;
		string s[101];
		string V[101];
		vector<int> C[101];
		vector<int>Temp;
		scanf("%d",&N);
		for(j=0;j<N;j++)
		cin>>s[j];
		
		for(j=0;j<N;j++)
		{
			x=0;
			for(k=0;k<s[j].length();k++)
			{
				if(k==0 ||s[j][k]!=s[j][k-1])
				{
					V[j].push_back(s[j][k]);	
					if(k!=0)
					C[j].push_back(k-x);
					x=k;
				}
			}
			C[j].push_back(s[j].length()-x);			
		}
		
		for(j=0;j<N-1;j++)
		{
			if(V[j].compare(V[j+1])!=0)
			break;			
		}
		if(j<N-1)
		{
			printf("Case #%d: Fegla Won\n",i);
			continue;
		}
		
		for(k=0;k<V[0].length();k++)
		{
			Temp.clear();
		for(j=0;j<N;j++)
		{
			Temp.push_back(C[j][k]);
			
		}
		sort(Temp.begin(),Temp.end());
			
			x=Temp.size();
			x/=2;
			for(y=1,z=1;y<=x;y++,z++)
			{
				sum+=(Temp[y]-Temp[y-1])*z;
			}
			z--;
			for(y=x+1;y<Temp.size();y++,z--)
			{
				sum+=(Temp[y]-Temp[y-1])*z;
			}
		
		//printf("%d\n",sum);
		}
		printf("Case #%d: %d\n",i,sum);
	}
	return 0;
}

