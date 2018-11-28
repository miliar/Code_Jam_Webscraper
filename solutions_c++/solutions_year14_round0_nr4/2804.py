#include <iostream>
#include<algorithm>
#include<stdio.h>
using namespace std;

int main() {
	// your code goes here
	int t=1,T,war,dwar,N;
	freopen("input.txt","r",stdin);
	freopen("oute.txt","w",stdout);
	float Naomi[1005],Ken[1005],flag[1005];
	scanf("%d",&T);
	while(t<=T)
	{
		war=0;dwar=0;
		scanf("%d",&N);
		for(int i=0;i<N;i++)
		scanf("%f",&Naomi[i]);
		for(int i=0;i<N;i++)
		scanf("%f",&Ken[i]);
		sort(Naomi,Naomi+N);
		sort(Ken,Ken+N);
		for(int i=N-1,j=N-1;i>=0;i--)
		{
			if(Naomi[i]>Ken[j]) war++;
			else j--;
		}

		for(int i=N-1,j=N-1;i>=0;i--)
		{
			//code here
			while(j>=0)
			{
			if(Naomi[i]>Ken[j]){ dwar++; j--;break;}
			j--;
			}
		}
		printf("Case #%d: %d %d\n",t,dwar,war);
		t++;
	}
	return 0;
}
