#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int ii = 1; ii <= t; ii++)
	{
		char s[2010]={0};
		int dg[10] = {0};
		int ctnc[30]={0};
		scanf("%s\n",s);
		int l = strlen(s);
		int cnt = 0;
		for(int i = 0; i<l; i++)
			ctnc[(int)(s[i] - 'A')]++;
		//ZERO
		cnt = ctnc[(int)('Z'-'A')];
		dg[0] = cnt;
		ctnc[(int)('O'-'A')] -= cnt;
		
		//EIGHT
		cnt = ctnc[(int)('G'-'A')];
		dg[8] = cnt;
		ctnc[(int)('H'-'A')] -= cnt;
		ctnc[(int)('I'-'A')] -= cnt;
		//TWO
		cnt = ctnc[(int)('W'-'A')];
		dg[2] = cnt;
		ctnc[(int)('O'-'A')] -= cnt;
		//FOUR
		cnt = ctnc[(int)('U'-'A')];
		dg[4] = cnt;
		ctnc[(int)('O'-'A')] -= cnt;
		ctnc[(int)('F'-'A')] -= cnt;
		//FIVE
		cnt = ctnc[(int)('F'-'A')];
		dg[5] = cnt;
		ctnc[(int)('V'-'A')] -= cnt;
		ctnc[(int)('I'-'A')] -= cnt;
		//SIX
		cnt = ctnc[(int)('X'-'A')];
		dg[6] = cnt;
		ctnc[(int)('I'-'A')] -= cnt;
		//SEVEN
		cnt = ctnc[(int)('V'-'A')];
		dg[7] = cnt;
		//NINE
		cnt = ctnc[(int)('I'-'A')];
		dg[9] = cnt;
		//THREE
		cnt = ctnc[(int)('H'-'A')];
		dg[3] = cnt;
		//ONE
		cnt = ctnc[(int)('O'-'A')];
		dg[1] = cnt;
		
		cout<<"Case #"<<ii<<": ";
		for(int i = 0; i<=9; i++)
		{
			while(dg[i]>0)
			{
				cout<<i;
				dg[i]--;
			}
		}
		cout<<endl;
	}
	return 0;
}