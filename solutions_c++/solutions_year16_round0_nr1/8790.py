# include <bits/stdc++.h>
using namespace std;
int main()
{
    FILE *fp, *fq;
    fp= fopen("asmall.in","rt");
    fq= fopen("asmallout.txt","wt");
	int t;
	fscanf(fp,"%d",&t);
	int l=1;
	while(t--)
	{
		long long n;
		int count=0;
		int hash[10]={0};
		fscanf(fp,"%lld",&n);
		if(n==0)
			fprintf(fq,"Case #%d: INSOMNIA\n",l);
		else
		{
			int i=1;
			while(count!=10)
			{
				long long temp=n*i;
				while(temp)
				{
					int a=temp%10;
					if(!hash[a])
					{
						hash[a]++;
						count++;
					}
					temp/=10;
				}
				i++;
			}
			long long temp=n*(i-1);
			fprintf(fq,"Case #%d: %lld\n", l, temp);
		}
		l++;
	}
	return 0;
}