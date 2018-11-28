#include<iostream>
#include<cstdio>
#include<cstring>

using namespace std;

int ans[1000];

void backtrack(int *al,int sum,int index,int ansindex,bool first)
{
	if(!first)
	{
		ans[ansindex] = index;

		switch(index){
			case 0:
				al['Z' - 'A']--;
				al['E' - 'A']--;
				al['R' - 'A']--;
				al['O' - 'A']--;
				sum -= 4;
				break;
			case 1:
				al['O' - 'A']--;
				al['N' - 'A']--;
				al['E' - 'A']--;
				sum -= 3;
				break;
			case 2:
				al['T' - 'A']--;
				al['W' - 'A']--;
				al['O' - 'A']--;
				sum -= 3;
				break;
			case 3:
				al['T' - 'A']--;
				al['H' - 'A']--;
				al['R' - 'A']--;
				al['E' - 'A']--;
				al['E' - 'A']--;
				sum -= 5;
				break;
			case 4:
				al['F' - 'A']--;
				al['O' - 'A']--;
				al['U' - 'A']--;
				al['R' - 'A']--;
				sum -= 4;
				break;
			case 5:
				al['F' - 'A']--;
				al['I' - 'A']--;
				al['V' - 'A']--;
				al['E' - 'A']--;
				sum -= 4;
				break;
			case 6:
				al['S' - 'A']--;
				al['I' - 'A']--;
				al['X' - 'A']--;
				sum -= 3;
				break;
			case 7:
				al['S' - 'A']--;
				al['E' - 'A']--;
				al['V' - 'A']--;
				al['E' - 'A']--;
				al['N' - 'A']--;
				sum -= 5;
				break;
			case 8:
				al['E' - 'A']--;
				al['I' - 'A']--;
				al['G' - 'A']--;
				al['H' - 'A']--;
				al['T' - 'A']--;
				sum -= 5;
				break;
			case 9:
				al['N' - 'A']--;
				al['I' - 'A']--;
				al['N' - 'A']--;
				al['E' - 'A']--;
				sum -= 4;
				break;
		}
	}


	if(sum == 0)
	{
		for(int i=0;i<=ansindex;++i)
			printf("%d",ans[i]);
		return;
	}

	for(int i=index;i<10;++i)
	{
/*		printf("\n\n%d %d\n\n",sum,i);
	
		for(int j=0;j<26;++j)
			printf("%d",al[j]);

*/
		switch(i){
			case 0:
				if(al['Z'-'A'] > 0 && al['E'-'A'] > 0 && al['R'-'A'] > 0 && al['O'-'A'] > 0)
				{
					backtrack(al,sum,i,ansindex + 1,false);
					al['Z' - 'A']++;
					al['E' - 'A']++;
					al['R' - 'A']++;
					al['O' - 'A']++;
				}
				break;
			case 1:
				if(al['O'-'A'] > 0 && al['N'-'A'] > 0 && al['E'-'A'] > 0)
				{
					backtrack(al,sum,i,ansindex + 1,false);
					al['O' - 'A']++;
					al['N' - 'A']++;
					al['E' - 'A']++;
				}		
				break;
			case 2:
				if(al['T'-'A'] > 0 && al['W'-'A'] > 0 && al['O'-'A'] > 0)
				{
					backtrack(al,sum,i,ansindex + 1,false);
					al['T' - 'A']++;
					al['W' - 'A']++;
					al['O' - 'A']++;
				}
				break;
			case 3:
				if(al['T'-'A'] > 0 && al['H'-'A'] > 0 && al['R'-'A'] > 0 && al['E'-'A'] > 1)
				{
					backtrack(al,sum,i,ansindex + 1,false);
					al['T' - 'A']++;
					al['H' - 'A']++;
					al['R' - 'A']++;
					al['E' - 'A']++;
					al['E' - 'A']++;
				}
				break;
			case 4:
				if(al['F'-'A'] > 0 && al['O'-'A'] > 0 && al['R'-'A'] > 0 && al['U'-'A'] > 0)
				{
					backtrack(al,sum,i,ansindex + 1,false);
					al['F' - 'A']++;
					al['O' - 'A']++;
					al['U' - 'A']++;
					al['R' - 'A']++;
				}	
				break;
			case 5:
				if(al['F'-'A'] > 0 && al['E'-'A'] > 0 && al['I'-'A'] > 0 && al['V'-'A'] > 0)
				{
					backtrack(al,sum,i,ansindex + 1,false);
					al['F' - 'A']++;
					al['I' - 'A']++;
					al['V' - 'A']++;
					al['E' - 'A']++;
				}
				break;
			case 6:
				if(al['S'-'A'] > 0 && al['I'-'A'] > 0 && al['X'-'A'] > 0)
				{	
					backtrack(al,sum,i,ansindex + 1,false);
					al['S' - 'A']++;
					al['I' - 'A']++;
					al['X' - 'A']++;
				}
				break;
			case 7:
				if(al['S'-'A'] > 0 && al['E'-'A'] > 1 && al['V'-'A'] > 0 && al['N'-'A'] > 0)
				{
					backtrack(al,sum,i,ansindex + 1,false);
					al['S' - 'A']++;
					al['E' - 'A']++;
					al['V' - 'A']++;
					al['E' - 'A']++;
					al['N' - 'A']++;
				}
				break;
			case 8:
				if(al['E'-'A'] > 0 && al['I'-'A'] > 0 && al['G'-'A'] > 0 && al['H'-'A'] > 0 && al['T'-'A'] > 0)
				{
					backtrack(al,sum,i,ansindex + 1,false);
					al['E' - 'A']++;
					al['I' - 'A']++;
					al['G' - 'A']++;
					al['H' - 'A']++;
					al['T' - 'A']++;
				}
				break;
			case 9:
				if(al['N'-'A'] > 1 && al['E'-'A'] > 0 && al['I'-'A'] > 0)
				{
					backtrack(al,sum,i,ansindex + 1,false);
					al['N' - 'A']++;
					al['I' - 'A']++;
					al['N' - 'A']++;
					al['E' - 'A']++;
				}
				break;
		}
	}
	
}

int main()
{
	int test,number = 1;
	while(scanf("%d",&test) != EOF)
	{
		char s[3000];
		int al[26];
		int sum = 0;
		number = 1;
		memset(ans,0,sizeof(ans));
		memset(al,0,sizeof(al));
		memset(s,0,sizeof(s));

		getchar();

		for(int i=0;i<test;++i)
		{
			printf("Case #%d: ",number);
			number++;
			gets(s);
			
			for(int j=0;j<strlen(s);++j)
			{
				sum++;
				al[s[j] - 'A']++;
			}

			backtrack(al,sum,0,-1,true);
	
			puts("");
			memset(ans,0,sizeof(ans));
			memset(al,0,sizeof(al));
			memset(s,0,sizeof(s));
			sum = 0;
		}
	}
	return 0;
}
