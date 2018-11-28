#include <cstring>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <map>
using namespace std;


int T,n,k;
char z[200][200];
int len[200];
int x[200][200];
int c[200][200];
int num[200];
int main()
{
	scanf("%d",&T);
	for(int idx=1;idx<=T;idx++)
	{
		scanf("%d",&n);
		for(int q=0;q<n;q++)
		{
			scanf("%s",z[q]);
			len[q]=strlen(z[q]);
			num[q]=1;
			x[q][0]=z[q][0];
			c[q][0]=1;
			for(int w=1;w<len[q];w++)
			{
				if(z[q][w]!=z[q][w-1])
				{
					x[q][num[q]]=z[q][w];
					num[q]++;
					c[q][num[q]-1]=1;
				}
				else
					c[q][num[q]-1]++;
			}
		}
		// for(int q=0;q<n;q++)
		// {
		// 	for(int w=0;w<num[q];w++)
		// 		cout<<x[q][w]<<" ";
		// 	cout<<endl;
		// }
			bool t=true;
			for(int q=1;q<n;q++)
				if(num[q]!=num[0])
					t=false;
			int ans=0;
			if(t)
			{
				for(int q=1;q<n;q++)
				{
					for(int w=0;w<num[0];w++)
						if(x[q][w]!=x[0][w])
							t=false;
						else
							ans+=abs(c[q][w]-c[0][w]);
					if(!t)
						break;
				}
			}
			if(t)
			printf("Case #%d: %d\n",idx,ans);
			else
				printf("Case #%d: Fegla Won\n",idx);

	}





	







	return 0;
}