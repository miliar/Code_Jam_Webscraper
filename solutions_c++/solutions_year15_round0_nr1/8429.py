#include <cstdio>
#include <iostream>

using namespace std;


char s[10000];

int main()
{
	freopen("inp.in","r",stdin);
	freopen("output.txt","w",stdout);

	int t;
	scanf("%d",&t);
	for(int test = 1; test <= t; test++)
	{
		int n;
		scanf("%d",&n);
		scanf("%s",s);

		int total = (s[0] - '0') , k, ans = 0;
		// cout<<total<<endl;
		for(int i=1;i<=n;i++)
		{
			k = s[i] - '0';
			if(k == 0)
				continue;
			// cout<<"k:"<<k<<endl;
			if(total < i)
			{
				// cout<<(i-total)<<endl;
				ans += (i-total);
				total += (i-total);
			}
			
			total += k;
		}
		printf("Case #%d: %d\n",test,ans);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}