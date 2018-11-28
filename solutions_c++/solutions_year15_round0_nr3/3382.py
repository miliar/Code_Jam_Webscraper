#include<bits/stdc++.h>
using namespace std;
char A[1000005];
int co (char a)
{
	if(a == '1')  return 1;
	if(a == 'i') return 2;
	if(a == 'j') return 3;
	if(a == 'k') return 4;
}
int T[6][6];
int L[7000005];
int P[7000005];
int mnoz (int a, int b)
{
	int razy = a*b;
	
	int fir = abs(a);
	int sec = abs(b);
	
	if(razy < 0) return -T[fir][sec];
	else return T[fir][sec];
}
int main()
{
	T[1][1] = 1; T[1][2] = 2; T[1][3] = 3; T[1][4] = 4;
	T[2][1] = 2; T[2][2] = -1; T[2][3] = 4; T[2][4] = -3;
	T[3][1] = 3; T[3][2] = -4; T[3][3] = -1; T[3][4] = 2;
	T[4][1] = 4; T[4][2] = 3; T[4][3] = -2; T[4][4] = -1;
	int t;
	scanf("%d", &t);
	for(int z = 1; z <= t; z++)
	{
		int l,x; scanf("%d%d",&l, &x);
		scanf("%s", A);
		string As = A;
		string S = As;
		x--;
		while(x--)
		{
			S = S + As;
		}
	//	for(int i = 0; i < S.size(); i++)
	//		printf("%c ", S[i]);
	//	puts("");
		L[0] = co(S[0]);
		for(int i = 1; i < S.size(); i++)
		{
			L[i] = mnoz(L[i-1], co(S[i]));
			//printf("%d ", L[i]);
		}
		//puts("");
		P[S.size()-1] = co(S[S.size()-1]);
		for(int i = S.size()-2; i >= 0; i--)
		{
			P[i] = mnoz( co(S[i]), P[i+1] );
		}
		
		bool czy = true;
		for(int i = 0; i < S.size() && czy; i++)
		{
			if(L[i] == 2)
			{
				int ilo = 1;
				for(int j = i+1; j < S.size(); j++)
				{
					if(P[j] == 4 && ilo == 3)
					{
						czy = false;
						break;
					}
					ilo = mnoz( ilo, co(S[j]));
				}
			}
		}
		
		if(czy == false)
			printf("Case #%d: YES\n", z);
		else
			printf("Case #%d: NO\n", z);
	}

return 0;
}