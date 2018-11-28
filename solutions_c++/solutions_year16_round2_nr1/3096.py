#include<cstdio>
#include<cstring>
#include<map>

using namespace std;

int judge(char alpha[],int temp[]) 
{
	int cnt[10] = {};
	int len = strlen(alpha);
	for (int i = 0; i < len; i++) 
	{
		cnt[i] = temp[alpha[i]-'A'];
	}
	int min = -1;
	for (int i = 0;i<len;i++)
	{
		int n = 0;
		for (int j = 0; j < len; j++) 
		{
			if(alpha[j] == alpha[i]) n++;
		}
		if (min == -1 || min > cnt[i]/n) 
		{
			min = cnt[i]/n;
		}
	}
	if(min!=-1)
	{	
		for (int i = 0;i<len;i++)
		{
			temp[alpha[i] - 'A'] -= min;
		}
		return min;
	}
	return 0;
}

void solve(char str[],int len) 
{
	int cnt[26] = {};
	for (int i = 0; i < len; i++)
	{
		cnt[str[i] - 'A']++;
	}
	int zero = judge("ZERO", cnt);
	int two = judge("TWO", cnt);
	int four = judge("FOUR", cnt);
	int six = judge("SIX", cnt);
	int seven = judge("SEVEN", cnt);
	int eight = judge("EIGHT", cnt);
	int three = judge("THREE", cnt);
	int one = judge("ONE", cnt);
	int five = judge("FIVE", cnt);
	int nine = judge("NINE", cnt);

	for (int i = 0; i <zero; i++) printf("0");
	for (int i = 0; i <one; i++) printf("1");
	for (int i = 0; i <two; i++) printf("2");
	for (int i = 0; i <three; i++) printf("3");
	for (int i = 0; i <four; i++) printf("4");
	for (int i = 0; i <five; i++) printf("5");
	for (int i = 0; i <six; i++) printf("6");
	for (int i = 0; i <seven; i++) printf("7");
	for (int i = 0; i <eight; i++) printf("8");
	for (int i = 0; i <nine; i++) printf("9");
}

int main() 
{
	int T;
	scanf("%d", &T);
	for (int c = 1; c <= T; c++) 
	{
		char str[2001];
		scanf("%s", str);
		printf("Case #%d: ", c);
		solve(str,strlen(str));
		printf("\n");
	}
	return 0;
}