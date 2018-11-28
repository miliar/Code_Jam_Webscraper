#include <stdio.h>

using namespace std;

int main(int argc, char const *argv[])
{
	int t,n,ans,j=0;
	char arr[2000];
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		scanf("%d %s",&n,arr);
		int total=0,ans=0,pre=0;		
		for(int shy=0;shy<=n;shy++)
		{
			if(total>=shy)
				total+=(arr[shy]-48);
			else
			{
				pre=shy-total;//extra friends required
				ans+=pre;
				total+=pre+(arr[shy]-48);
			}
		//	printf("%d %d %d %d\n",ans,total,(int)arr[shy],pre );
		}


		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}
