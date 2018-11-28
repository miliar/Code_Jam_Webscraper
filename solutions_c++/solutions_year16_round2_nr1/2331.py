#include <cstdio>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <cstring>
#include <vector>

using namespace std;

int main()
{
	int n ;
	scanf("%d",&n);
	char s[20000];
	for (int num = 0; num < n; ++num)
	{	
		vector<int> ans;

		int rec[30]={0};
		printf("Case #%d: ",num+1 );
		scanf("%s",s);
		int len =strlen(s);
		for (int i = 0; i < len; ++i)
		{	
			if (s[i]=='E')
			{
				int x ='E'-'A';
				rec[x]++;
			}
			if (s[i]=='F')
			{
				int x ='F'-'A';
				rec[x]++;
			}
			if (s[i]=='G')
			{
				int x ='G'-'A';
				rec[x]++;
			}
			if (s[i]=='H')
			{
				int x ='H'-'A';
				rec[x]++;
			}
			if (s[i]=='I')
			{
				int x ='I'-'A';
				rec[x]++;
			}
			if (s[i]=='N')
			{
				int x ='N'-'A';
				rec[x]++;
			}
			if (s[i]=='O')
			{
				int x ='O'-'A';
				rec[x]++;
			}
			
			if (s[i]=='R')
			{
				int x ='R'-'A';
				rec[x]++;
			}
			if (s[i]=='S')
			{
				int x ='R'-'A';
				rec[x]++;
			}
			if (s[i]=='T')
			{
				int x ='R'-'A';
				rec[x]++;
			}
			if (s[i]=='U')
			{
				int x ='U'-'A';
				rec[x]++;
			}
			if (s[i]=='V')
			{
				int x ='V'-'A';
				rec[x]++;
			}
			if (s[i]=='W')
			{
				int x ='W'-'A';
				rec[x]++;
			}
			if (s[i]=='X')
			{
				int x ='X'-'A';
				rec[x]++;
			}
			if (s[i]=='Z')
			{
				int x ='Z'-'A';
				rec[x]++;
			}
		}
		// for (int k = 0; k < 30; ++k)
		// {
		// 	printf("%d", rec[k]);
		// }
		//printf("\n");
		while(rec[25]>0)
		{
			rec[25]--;
			rec[17]--;
			rec[4]--;
			rec[14]--;
			ans.push_back(0);
		}
		while(rec[23]>0)
		{
			rec[23]--;
			rec[8]--;
			rec[18]--;
			//rec[14]--;
			ans.push_back(6);
		}
		while(rec[22]>0)
		{
			rec[22]--;
			rec[19]--;
			rec[14]--;
			//rec[14]--;
			ans.push_back(2);
		}
		while(rec[6]>0)
		{
			rec[6]--;
			rec[4]--;
			rec[8]--;
			rec[7]--;
			rec[19]--;
			//rec[14]--;
			ans.push_back(8);
		}
		while(rec[7]>0)
		{
			rec[7]--;
			rec[4]--;
			rec[4]--;
			rec[17]--;
			rec[19]--;
			//rec[14]--;
			ans.push_back(3);
		}
		while(rec[20]>0)
		{
			rec[5]--;
			rec[17]--;
			rec[14]--;
			//rec[17]--;
			rec[20]--;
			//rec[14]--;
			ans.push_back(4);
		}
		while(rec[5]>0)
		{
			rec[5]--;
			rec[8]--;
			rec[21]--;
			//rec[17]--;
			rec[4]--;
			//rec[14]--;
			ans.push_back(5);
		}
		while(rec[21]>0)
		{
			rec[13]--;
			rec[18]--;
			rec[21]--;
			//rec[17]--;
			rec[4]--;
			rec[4]--;
			//rec[14]--;
			ans.push_back(7);
		}
		while(rec[8]>0)
		{
			rec[13]--;
			rec[13]--;
			rec[8]--;
			//rec[17]--;
			//rec[4]--;
			rec[4]--;
			//rec[14]--;
			ans.push_back(9);
		}
		while(rec[14]>0)
		{
			rec[14]--;
			rec[4]--;
			rec[13]--;
			//rec[14]--;
			ans.push_back(1);
		}
		sort(ans.begin(),ans.end());
		for (int j = 0; j < ans.size(); ++j)
		{
			printf("%d",ans[j] );
		}
		printf("\n");
	}


return 0;

}