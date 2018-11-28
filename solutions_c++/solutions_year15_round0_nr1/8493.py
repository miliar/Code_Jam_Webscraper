#include<stdio.h>
#include<fstream>
#define max 1001
using namespace std;
int main()
{
	
	long s[max]={0},sum;
	int i=0,j,t,sl;
	freopen("Input.in","r",stdin);
	freopen("output.in","w",stdout);
	scanf("%d",&t);
	while(i++<t)
	{
		sum=0;
		scanf("%d",&sl);
		getchar();
		s[0]=getchar()-'0';
		for(j=1;j<=sl;++j)
		{
			s[j]=getchar()-'0';
			if((s[j]!=0)&&(s[j-1]<j))
			{
				sum+=j-s[j-1];
				s[j]+=j;
			}
			else
			{
		        s[j]+=s[j-1];
			}
		}
		printf("Case #%d: %d\n",i,sum);
		
	}
}
