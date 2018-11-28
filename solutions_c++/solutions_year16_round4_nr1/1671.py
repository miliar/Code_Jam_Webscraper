#include <iostream>
#include <string.h>
using namespace std;

typedef long long int ll;

int main()
{
	int T, N, P, R, S, cr, cs, cp;
	char alpha[10][10000];
	char str[100000], abc[100000], min[100000];

	cin>>T;

	for(int i = 1; i <= T; i++)
	{
		int alp = 0;
		cin>>N>>R>>P>>S;
		cout<<"Case #"<<i<<": ";
		cr = cp = cs = 0;
		cp = 1;
		str[0] = 'P';
		str[1] = 0;

		for(int j = 1; j <= N; j++)
		{
			int a = cr, b = cp, c = cs;
			cr = a + b;
			cs = a + c;
			cp = b + c;

			int k = 0;

			for(int p = 0; p < strlen(str); p++)
			{
				if(str[p] == 'R')
				{
					abc[k] = 'R';
					abc[k + 1] = 'S';
				}
				else if(str[p] == 'S')
				{
					abc[k] = 'P';
					abc[k + 1] = 'S';
				}
				else
				{
					abc[k] = 'P';
					abc[k + 1] = 'R';
				}
				k = k + 2;
			}
			strcpy(str, abc);
			str[k] = 0;
		}
		// cout<<endl;
		// cout<<str<<endl;
		// cout<<cp<<" "<<cr<<" "<<cs<<" ";
		strcpy(min, str);

		if(P == cp && R == cr && S == cs)
		{
			int p = 1;
			for(int j = 1; j < N; j++)
			{
				p = p * 2;
				for(int k = 0; k < strlen(str); k += 2 * p)
				{
					int l;
					for(l = 0; l < p; l++)
					{
						if(str[k + l + p] < str[k + l])
						{
							break;
						}
					}
					if(l < p)
					{
						for(int xy = 0; xy < p; xy++)
						{
							char te = str[xy + k];
							str[xy + k] = str[xy + k + p];
							str[xy + k + p] = te;
						}
					}
				}
			}
			strcpy(alpha[alp], str);
			alp++;
		}
		strcpy(str, min);
		if(P == cp && R == cs && S == cr)
		{
			int xyz = 0;
			for(int j = 0; j < strlen(str); j+=2)
			{
				if(str[j] == 'R')
				{
					abc[xyz] = 'R';
					abc[xyz + 1] = 'S';
				}
				else if(str[j + 1] == 'R')
				{
					abc[xyz] = 'P';
					abc[xyz + 1] = 'S';
				}
				else
				{
					abc[xyz] = 'P';
					abc[xyz + 1] = 'R';
				}
				xyz += 2;
			}
			abc[xyz] = 0;
			strcpy(str, abc);
			int p = 1;
			for(int j = 1; j < N; j++)
			{
				p = p * 2;
				for(int k = 0; k < strlen(str); k += 2 * p)
				{
					int l;
					for(l = 0; l < p; l++)
					{
						if(str[k + l + p] < str[k + l])
						{
							break;
						}
					}
					if(l < p)
					{
						for(int xy = 0; xy < p; xy++)
						{
							char te = str[xy + k];
							str[xy + k] = str[xy + k + p];
							str[xy + k + p] = te;
						}
					}
				}
			}
			strcpy(alpha[alp], str);
			alp++;
		}
		strcpy(str, min);
		if(P == cr && R == cp && S == cs)
		{
			int xyz = 0;
			for(int j = 0; j < strlen(str); j+=2)
			{
				if(str[j] == 'R')
				{
					abc[xyz] = 'P';
					abc[xyz + 1] = 'S';
				}
				else if(str[j + 1] == 'S')
				{
					abc[xyz] = 'R';
					abc[xyz + 1] = 'S';
				}
				else
				{
					abc[xyz] = 'P';
					abc[xyz + 1] = 'R';
				}
				xyz += 2;
			}
			abc[xyz] = 0;
			strcpy(str, abc);
			int p = 1;
			for(int j = 1; j < N; j++)
			{
				p = p * 2;
				for(int k = 0; k < strlen(str); k += 2 * p)
				{
					int l;
					for(l = 0; l < p; l++)
					{
						if(str[k + l + p] < str[k + l])
						{
							break;
						}
					}
					if(l < p)
					{
						for(int xy = 0; xy < p; xy++)
						{
							char te = str[xy + k];
							str[xy + k] = str[xy + k + p];
							str[xy + k + p] = te;
						}
					}
				}
			}
			strcpy(alpha[alp], str);
			alp++;
		}
		strcpy(str, min);
		if(P == cr && R == cs && S == cp)
		{
			int xyz = 0;
			for(int j = 0; j < strlen(str); j+=2)
			{
				if(str[j] == 'R')
				{
					abc[xyz] = 'P';
					abc[xyz + 1] = 'S';
				}
				else if(str[j + 1] == 'S')
				{
					abc[xyz] = 'P';
					abc[xyz + 1] = 'R';
				}
				else
				{
					abc[xyz] = 'R';
					abc[xyz + 1] = 'S';
				}
				xyz += 2;
			}
			abc[xyz] = 0;
			strcpy(str, abc);
			int p = 1;
			for(int j = 1; j < N; j++)
			{
				p = p * 2;
				for(int k = 0; k < strlen(str); k += 2 * p)
				{
					int l;
					for(l = 0; l < p; l++)
					{
						if(str[k + l + p] < str[k + l])
						{
							break;
						}
					}
					if(l < p)
					{
						for(int xy = 0; xy < p; xy++)
						{
							char te = str[xy + k];
							str[xy + k] = str[xy + k + p];
							str[xy + k + p] = te;
						}
					}
				}
			}
			strcpy(alpha[alp], str);
			alp++;
		}
		strcpy(str, min);
		if(P == cs && R == cp && S == cr)
		{
			int xyz = 0;
			for(int j = 0; j < strlen(str); j+=2)
			{
				if(str[j] == 'R')
				{
					abc[xyz] = 'P';
					abc[xyz + 1] = 'S';
				}
				else if(str[j + 1] == 'S')
				{
					abc[xyz] = 'P';
					abc[xyz + 1] = 'R';
				}
				else
				{
					abc[xyz] = 'R';
					abc[xyz + 1] = 'S';
				}
				xyz += 2;
			}
			abc[xyz] = 0;
			strcpy(str, abc);
			int p = 1;
			for(int j = 1; j < N; j++)
			{
				p = p * 2;
				for(int k = 0; k < strlen(str); k += 2 * p)
				{
					int l;
					for(l = 0; l < p; l++)
					{
						if(str[k + l + p] < str[k + l])
						{
							break;
						}
					}
					if(l < p)
					{
						for(int xy = 0; xy < p; xy++)
						{
							char te = str[xy + k];
							str[xy + k] = str[xy + k + p];
							str[xy + k + p] = te;
						}
					}
				}
			}
			strcpy(alpha[alp], str);
			alp++;
		}
		strcpy(str, min);
		if(P == cs && R == cr && S == cp)
		{
			int xyz = 0;
			for(int j = 0; j < strlen(str); j+=2)
			{
				if(str[j] == 'R')
				{
					abc[xyz] = 'P';
					abc[xyz + 1] = 'R';
				}
				else if(str[j + 1] == 'S')
				{
					abc[xyz] = 'P';
					abc[xyz + 1] = 'S';
				}
				else
				{
					abc[xyz] = 'R';
					abc[xyz + 1] = 'S';
				}
				xyz += 2;
			}
			abc[xyz] = 0;
			strcpy(str, abc);
			int p = 1;
			for(int j = 1; j < N; j++)
			{
				p = p * 2;
				for(int k = 0; k < strlen(str); k += 2 * p)
				{
					int l;
					for(l = 0; l < p; l++)
					{
						if(str[k + l + p] < str[k + l])
						{
							break;
						}
					}
					if(l < p)
					{
						for(int xy = 0; xy < p; xy++)
						{
							char te = str[xy + k];
							str[xy + k] = str[xy + k + p];
							str[xy + k + p] = te;
						}
					}
				}
			}
			strcpy(alpha[alp], str);
			alp++;
		}
		if(alp == 0)
		{
			cout<<"IMPOSSIBLE"<<endl;
		}
		else
		{
			strcpy(min, alpha[0]);
			// cout<<alpha[0]<<endl;

			for(int j = 1; j < alp; j++)
			{
				// cout<<alpha[j]<<endl;
				if(strcmp(min, alpha[j]) > 0)
				{
					strcpy(min, alpha[j]);
				}
			}
			cout<<min<<endl;
		}
	}
	return 0;
}