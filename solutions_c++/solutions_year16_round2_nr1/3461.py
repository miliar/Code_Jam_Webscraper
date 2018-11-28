// Sheep

#include <iostream>
#include <string.h>
using namespace std;
 
char d[10][10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
/*
Zero
tWo
siX
eiGht
tHree
foUr
4->Five
5->seVen
2->4->One
Last->ninE
*/

char s[128];
char str[2010];
int c[10];

void update(int i)
{
	for(int j=0 ; d[i][j] ; ++j)
		s[d[i][j]] -= c[i];
}

int main() {
	int tc,tst;
	cin >> tst;
#if 0
	int i,j,k;
	for(i=0 ; i<10 ; ++i)
	{
		for(j=0,k=0 ; d[i][j] ; ++j)
			k += (d[i][j]-'A');
		cout << d[i] << " " << k << endl;
	}
#endif
	for(tc=1 ; tc<=tst ; ++tc)
	{
		int n,i,j;

		memset(s,0,sizeof(s));
		memset(c,0,sizeof(c));

		cin >> str;
		for(j=0 ; str[j] ; ++j)
			s[str[j]]++;
			
		//Zero
		c[0] = s['Z'];	update(0);
		
		//tWo
		c[2] = s['W'];	update(2);

		//siX
		c[6] = s['X'];	update(6);

		//eiGht
		c[8] = s['G'];	update(8);
		
		//foUr
		c[4] = s['U'];	update(4);
		
		//thRee
		c[3] = s['R'];	update(3);

		//4->Five
		c[5] = s['F'];	update(5);

		//5->seVen
		c[7] = s['V'];	update(7);

		//2->4->One
		c[1] = s['O'];	update(1);

		//Last->ninE
		c[9] = s['E'];	update(9);
		
		for(i='A' ; i<='Z' ; ++i)
			if(s[i])
				printf("--> %c %d\n",i,s[i]);

		cout << "Case #" << tc << ": ";
		for(i=0 ; i<10 ; ++i)
			for(j=0 ; j<c[i] ; ++j)
				cout << i;
		cout << endl;

	}
	return 0;
}
