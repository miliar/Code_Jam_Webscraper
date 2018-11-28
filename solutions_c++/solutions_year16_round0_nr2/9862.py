#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	scanf("%d",&t);
	for(int k=1;k<=t;k++)
	{
		char str[101];
		int v[101];
		int n,x,y,i,z,counter=0,c1,c2,j;
		scanf("%s",str);
		x=strlen(str);
		for(i=0; i < x ;i++)
		{
			if(str[i]== '+')
				v[i]=1;
			else v[i]=0;
		}
		c2=0;

		if(x==1 && v[0]==0)
		{
			printf("Case #%d: %d\n",k,1);
			continue;
		}
		counter=-1;
		for(i=0;i<x;)
		{
			if(v[i]==1) {
				i++; counter=i;
			}
			else{
				i++;

				while(i<x && v[i]!=1) {
					i++;
				}
				if(i<x && v[i]==1) i--;

				if(counter < 0) c2+=1;
				else c2+=2;

				i++;
			}
		}
		printf("Case #%d: %d\n",k,c2);
	}
	return 0;
}
