#include<cstdio>
#include<cstring>
#include<cmath>
#include<iostream>
#include<vector>
#include<algorithm>
#include<limits.h>
using namespace std;


int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	int cases;
	scanf("%d",&cases);
	int count=0;
	while(cases--)
	{
		char s[2009];
		scanf("%s",s);
		int d[26];
		memset(d, 0, sizeof(d));
		for(int i=0;i<strlen(s);i++)
		{
			d[s[i]-'A']++;
		}

		int ans[10];
		memset(ans, 0, sizeof(ans));
		int tmp[10];
		//Six zero          seven      eight  three   four       five   nine      one two
		tmp[0]=6;tmp[1]=0;tmp[2]=7;tmp[3]=8; tmp[4]=3;tmp[5]=4;tmp[6]=5;tmp[7]=9;tmp[8]=2;tmp[9]=1;
		for(int i=0;i<10;i++)
		{
			switch(tmp[i])
			{
				case 0:
					while(1)
					{
						//zero
						if(d['Z'-'A'] > 0 && d['E'-'A'] > 0 && d['R'-'A'] > 0 && d['O'-'A'] > 0 )
						{
							ans[0]++;
							
						d['Z'-'A']--;d['E'-'A']--; d['R'-'A']--;d['O'-'A']--;
						}
						else break;
					}
					break;

				case 1:
					while(1)
					{
						//ONE
						if(d['O'-'A'] > 0 && d['N'-'A'] > 0 && d['E'-'A'] > 0)
						{
							ans[1]++;
							
						d['O'-'A']--;d['N'-'A']--; d['E'-'A']--;
						}
						else break;
					}
					break;
				case 2:
					while(1)
					{
						//TWO
						if(d['T'-'A'] > 0 && d['W'-'A'] > 0 && d['O'-'A'] > 0 )
						{
							ans[2]++;
							
						d['T'-'A']--;d['W'-'A']--; d['O'-'A']--;
						}
						else break;
					}
					break;
				case 3:
					while(1)
					{
						//THREE
						if(d['T'-'A'] > 0 && d['H'-'A'] > 0 && d['R'-'A'] > 0 && d['E'-'A'] > 1 )
						{
							ans[3]++;
							
						d['T'-'A']--;d['H'-'A']--; d['R'-'A']--;d['E'-'A']--;d['E'-'A']--;
						}
						else break;
					}
					break;
				case 4:
					while(1)
					{
						//FOUR
						if(d['F'-'A'] > 0 && d['O'-'A'] > 0 && d['U'-'A'] > 0 && d['R'-'A'] > 0 )
						{
							ans[4]++;
							
						d['F'-'A']--;d['O'-'A']--; d['U'-'A']--;d['R'-'A']--;
						}
						else break;
					}
					break;
				case 5:
					while(1)
					{
						//FIVE
						if(d['F'-'A'] > 0 && d['I'-'A'] > 0 && d['V'-'A'] > 0 && d['E'-'A'] > 0 )
						{
							ans[5]++;
							
						d['F'-'A']--;d['I'-'A']--; d['V'-'A']--;d['E'-'A']--;
						}
						else break;
					}
					break;
				case 6:
					while(1)
					{
						//SIX
						if(d['S'-'A'] > 0 && d['I'-'A'] > 0 && d['X'-'A'] > 0 )
						{
							ans[6]++;
							
						d['S'-'A']--;d['I'-'A']--; d['X'-'A']--;
						}
						else break;
					}
					break;
				case 7:
					while(1)
					{
						//SEVEN
						if(d['S'-'A'] > 0 && d['E'-'A'] > 1 && d['V'-'A'] > 0 && d['N'-'A'] > 0 )
						{
							ans[7]++;
							
						d['S'-'A']--;d['E'-'A']--; d['E'-'A']--; d['V'-'A']--;d['N'-'A']--;
						}
						else break;
					}
					break;
				case 8:
					while(1)
					{
						//EIGHT
						if(d['E'-'A'] > 0 && d['I'-'A'] > 0 && d['G'-'A'] > 0 && d['H'-'A'] > 0 && d['T'-'A'] > 0 )
						{
							ans[8]++;
							
						d['E'-'A']--;d['I'-'A']--; d['G'-'A']--;d['H'-'A']--;d['T'-'A']--;
						}
						else break;
					}
					break;
				case 9:
					while(1)
					{
						//NINE
						if(d['N'-'A'] > 1 && d['I'-'A'] > 0 && d['E'-'A'] > 0)
						{
							ans[9]++;
							
						d['N'-'A']--;d['N'-'A']--; d['I'-'A']--;d['E'-'A']--;
						}
						else break;
					}
					break;
				default:
					break;
			}

		}
					

		printf("Case #%d: ",++count);
		for(int i=0;i<10;i++)
		{
			while(ans[i]--)
			{
				printf("%d",i);
			}
		}
		printf("\n");
		for(int i=0;i<26;i++)
		{
			if(d[i] != 0)
			{
				printf("HI %d \n",i);
			}
		}

	}
	

		
	return 0;

}
