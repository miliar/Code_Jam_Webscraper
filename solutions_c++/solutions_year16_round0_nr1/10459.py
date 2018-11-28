#include<iostream>
#include<map>
#include<string>
#include<cstring>
#include<cstdio>
#include<cmath>
using namespace std;
int main()
{
	long long ans,temp;
	int visit[10]={0};
	int n,num;
	FILE * fp;
	fp=fopen("m.txt","w");
	if(fp==NULL) return 0;
	cin>> n;
	for(int m=1;m<=n;m++)
	{
		int count=0;
		memset(visit,0,sizeof(visit));

		cin>> num;
		num=abs(num);
		int intc=num;
		while(count!=10 && num!=0)
		{
			temp=(long long)num;
			while(temp>0)
			{
				int a=temp%10;
				if(visit[a]==0) 
				{
					visit[a]=1;
					count++;

				}
				temp=temp/10;
			}
			if(count<10)num+=intc;
		}
		if(num==0) fprintf(fp,"Case #%d: INSOMNIA\n",m);
		else fprintf(fp,"Case #%d: %d\n",m,num);

	}
	fclose(fp);
	return 0;
}
