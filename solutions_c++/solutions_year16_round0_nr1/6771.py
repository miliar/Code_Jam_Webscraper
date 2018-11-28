#include <stdio.h>
#include <vector>
using namespace std;
int main(void)
{
	FILE *in,*out;
	in=fopen("As.txt","r");
	out=fopen("Bs.txt","w");
	int n;
	fscanf(in,"%d",&n);
	for(int e=0;e<n;e++)
	{
		int k;
		fscanf(in,"%d",&k);
		if(k==0)
		{
			fprintf(out,"Case #%d: INSOMNIA\n",e+1);
			continue;
		}
		vector<int> a(10,0);
		int tot=10,p=k;
		while(tot!=0)
		{
			int q=p;
			while(q!=0)
			{
				if(a[q%10]==0)
				{
					a[q%10]=1;
					tot--;
				}
				q/=10;
			}
			p+=k;
		}
		fprintf(out,"Case #%d: %d\n",e+1,p-k);
	}
	return 0;
}
