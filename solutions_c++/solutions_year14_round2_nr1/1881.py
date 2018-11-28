#include<iostream>
const int MAX_N = 200;
const int MAX_L = 200;
char s[MAX_L],str[MAX_N][MAX_L];
int cnt[MAX_N][MAX_L];
int l[MAX_N];
int solve()
{
	int i,j;
	for(i=0;i<=MAX_N;i++)
	{
		l[i]=0;
		for(j=0;j<=MAX_L;j++)
		{
			cnt[i][j]=0;
			str[i][j]=NULL;
		}
	}
	int N;
	scanf("%d",&N);
	for(i=0;i<N;i++) 
	{
		scanf("%s",s);
		for(j=0;s[j];j++) 
		{
			str[i][l[i]]=s[j];
			cnt[i][l[i]]=1;
			while(s[j]==s[j+1]) 
			{
				cnt[i][l[i]]++;
				j++;
			}
			l[i]++;
		}
	}
	for(i=0;i<N;i++) 
	{
		if(l[0]!=l[i]) return -1;
		for(j=0;j<l[0];j++)
			if(str[0][j]!=str[i][j]) return -1;
	}
	int calc,answer=0;
	for(i=0;i<l[0];i++)
	{
		calc = 0;
		for(j=0;j<N;j++) calc+=cnt[j][i];
		if( 2*(calc%N) >=N) calc = calc/N+1;
		else calc = calc/N;
		for(j=0;j<N;j++)
		{
			answer+=abs(calc-cnt[j][i]);
		}
	}
	return answer;
}


int main()
{
	int tests,i,answer;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&tests);
	for(i=1;i<=tests;i++)
	{
		
		answer = solve();
		printf("Case #%d: ",i);
		if(answer>=0) printf("%d\n",answer);
		else printf("Fegla Won\n");
	}
	return 0;
}