#include<cstdio>
#include<string>
#include<cstring>
#include<iostream> 
#include<algorithm> 
using namespace std;
int main()
{
	//freopen("A-small-attempt0.in","r",stdin);
	//freopen("A-small-attempt0.out","w",stdout);
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T,kk=0;
	scanf("%d",&T);
	while(T>0)
	{
		T--;
		kk++;
		string x;
		cin>>x;
		int k;
		scanf("%d",&k);
		int lx=x.size();
		int i,j;
		int s=0;
		for(i=0;i<=lx-1;i++)
		{
			if(i+k-1>lx-1)
				break;
			if(x[i]=='-')
			{
				s++;
				for(j=i;j<=i+k-1;j++)
				{
					if(x[j]=='-')
						x[j]='+';
					else
						x[j]='-';
				}
			}
		}
		bool flag=true;
		j=i;
		for(i=j;i<=lx-1;i++)
			if(x[i]=='-')
				flag=false;
		printf("Case #%d: ",kk);
		if(flag)
			printf("%d\n",s);
		else
			printf("IMPOSSIBLE\n");
	}
	return 0;
}
