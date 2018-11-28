#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t, tmp;
	scanf("%d",&t);
	tmp = t;
	while(t--)
	{
		char str[2005], number[10][10] = {"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};
		scanf("%s", str);
		int j, i, n = 0, count[10], ch[27];
		memset(ch, 0, sizeof ch);
		memset(count, 0, sizeof count);
		for( i = 0 ; str[i] != '\0' ; i++ )
		{
			if(str[i] == 'Z')
				count[0]++;
			else if(str[i] == 'W')
				count[2]++;
			else if(str[i] == 'X')
				count[6]++;
			else if( str[i] == 'G')
				count[8]++;
			else if( str[i] == 'U')
				count[4]++;
			n++;
			ch[str[i] - 'A']++;
		}
		for( i = 0 ; i <= 9 ; i += 2 )
		{
			for( j = 0 ; number[i][j] != '\0' ; j++ )
			{
				ch[number[i][j] - 'A'] -= count[i];
			}
		}
		count[1] += ch['O' - 'A'];
		count[3] += ch['T' - 'A'];
		count[5] += ch['F' - 'A'];
		ch['I' - 'A'] -= count[5];
		count[7] += ch['S' - 'A'];
		count[9] += ch['I' - 'A'];
		printf("Case #%d: ",tmp - t);
		for( i = 0 ; i < 10 ; i++ )
		{
			for( j = 0 ; j < count[i] ; j++ )
			{
				printf("%d",i);
			}
		}
		printf("\n");
	}
	return 0;
}
