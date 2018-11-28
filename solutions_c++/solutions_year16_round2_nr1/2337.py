#include <bits/stdc++.h>
using namespace std;
int main()
{
//freopen("inp1.in","r",stdin);
//freopen("out1.txt","w",stdout);
	int t;
	char arr[5000];
	int letter[30];
	int dig[12];
	scanf("%d",&t);
	int tc = 1;
	while(t--)
	{
		for(int i=0;i<=27;i++)
		{
			letter[i] = 0;
		}
		for(int i=0;i<=10;i++)
		{
			dig[i] = 0;
		}
		scanf("%s",arr);
		int l = strlen(arr);
		for(int i=0;i<l;i++)
		{
			letter[arr[i]-'0'-16]++;
		}
		//calculating sixes
		if(letter[24]!=0)
		{
			dig[6]=letter[24];
			letter[24]=0;
			letter[19]-=dig[6];
			letter[9]-=dig[6];
		}
		//calculating TWO
		if(letter[23]!=0)
		{
			dig[2] = letter[23];
			letter[23] = 0;
			letter[20]-=dig[2];
			letter[15]-=dig[2];
		}
		//calculating 4
		if(letter[21]!=0)
		{
			dig[4] = letter[21];
			letter[21] = 0;
			letter[6]-=dig[4];
			letter[15]-=dig[4];
			letter[18]-=dig[4];
		}
		//calculating 5
		if(letter[6]!=0)
		{
			dig[5] = letter[6];
			letter[6] -=dig[5];
			letter[9]-=dig[5];
			letter[22]-=dig[5];
			letter[5]-=dig[5];
		}
		//calculate 0
		if(letter[26]!=0)
		{
			dig[0] = letter[26];
			letter[5]-=dig[0];
			letter[18]-=dig[0];
			letter[15]-=dig[0];
		}
		//calculate seven
		if(letter[22]!=0)
		{
			dig[7] = letter[22];
			letter[22]-=dig[7];
			letter[19]-=dig[7];
			letter[5]-=dig[7];
			letter[5]-=dig[7];
			letter[14]-=dig[7];
		}
		//calculate eight
		if(letter[7]!=0)
		{
			dig[8] = letter[7];
			letter[7]-=dig[8];
			letter[5]-=dig[8];
			letter[9]-=dig[8];
			letter[8]-=dig[8];
			letter[20]-=dig[8];
		}
		//caluclate 3
		if(letter[18]!=0)
		{
			dig[3] = letter[18];
			letter[20]-=dig[3];
			letter[8]-=dig[3];
			letter[5]-=dig[3];
			letter[5]-=dig[3];
			// letter[20]-=dig[3];
		}
		//caluclate one
		if(letter[15]!=0)
		{
			dig[1] = letter[15];
			letter[15]-=dig[1];
			letter[14]-=dig[1];
			letter[5]-=dig[1];
			// letter[15]-=dig[1];
		}
		//calculate 9
		if(letter[5]!=0)
		{
			dig[9] = letter[5];
		}
		int ans[5000];
		int ptr = 0;
		for(int i=0;i<=9;i++)
		{
			if(dig[i]!=0)
			{
				for(int k=0;k<dig[i];k++)
				{
					ans[ptr++] = i;
				}
			}
		}
		printf("Case #%d: ",tc);
		tc++;
		for(int j=0;j<ptr;j++)
		{
			printf("%d",ans[j]);
		}
		printf("\n");
	}
}
