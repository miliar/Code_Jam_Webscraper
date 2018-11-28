#include<iostream>
#include<string>
#include<string.h>
#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<vector>
#include<stack>
#include<map>
#include<set>
#include<queue>
#include<math.h>
using namespace std;
int INFI = 0x7fffffff ;
int Res_cnt[10];
int cnt_sum[26];
int cnt_num[10][26];
int rem;
string Num_String[]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int maxn(int numK)
{
	int MaxKcnt = INFI;
	for(int i=0; i<26; i++)
	{
		if(cnt_num[numK][i]!=0 )
		{
		//	cout<<char('A'+i)<<" "<<numK<<" "<<cnt_num[numK][i]<<" "<<cnt_sum[i]<<endl;
			if(cnt_sum[i]/cnt_num[numK][i] < MaxKcnt ) MaxKcnt =cnt_sum[i]/cnt_num[numK][i];
		}
		
	}
	return MaxKcnt;
}
bool Res(int numK)
{
	if(rem==0) return true;
	if(numK==10) return false;
	//cout<<numK<<" "<<maxn(numK)<<endl;
	for( int tryKcnt = 0; tryKcnt <= maxn(numK); tryKcnt++)
	{
		for(int i=0; i<Num_String[numK].length(); i++)
		{
			cnt_sum[Num_String[numK][i]-'A'] -= tryKcnt;
		}
		rem -= tryKcnt * Num_String[numK].length();
		//cout<<rem<<endl;
		if(Res( numK+1))
		{
			Res_cnt[numK] = tryKcnt;
			return true;
		}
		rem += tryKcnt * Num_String[numK].length();;
		for(int i=0; i<Num_String[numK].length(); i++)
		{
			cnt_sum[Num_String[numK][i]-'A'] += tryKcnt;
		}
		
	}
	return false;
}

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("Output.txt","w",stdout);
	
	memset(cnt_num,0,sizeof(cnt_num));
	for(int i=0; i<=9; i++)
	{
		for(int j=0; j<Num_String[i].length(); j++)
		{
			cnt_num[i][Num_String[i][j]-'A']++;
		}
		//cout<<Num_String[i]<<" "<<Num_String[i][0]<<" "<<cnt_num[i][Num_String[i][0]-'A']<<endl;
		
	}
	int T;
	string str;
	cin>>T;
	for(int i=1; i<=T; i++)
	{
		cin>>str;
		memset(cnt_sum,0,sizeof(cnt_sum));
		for(int j=0; j<str.length(); j++) cnt_sum[str[j]-'A']++;
		memset(Res_cnt,0,sizeof(Res_cnt));
		rem = str.length();
		printf("Case #%d: ",i );
		if(Res(0))
		{
			for(int j=0; j<=9; j++)
			{
				while(Res_cnt[j]>0)
				{
					printf("%d",j); Res_cnt[j]--;
				}
			}
			printf("\n");
		}
		
	}
	return 0;
}
