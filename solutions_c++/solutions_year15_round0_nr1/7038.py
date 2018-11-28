#include <iostream>
#include <cstdio>

using namespace std;

int main ()
{
	int t, caso=1;
	
	scanf("%d", &t);
	
	while(t--)
	{
		int s;
		
		scanf("%d", &s);
			
		char aux[s+2];
		
		scanf(" %s", &aux[0]);
		
		int vetor[s+1];
		
		for(int i=0 ; i<=s ; i++)
			vetor[i]=aux[i]-'0';
		
		int pessoas=0, amigos=0;
		
		for(int i=0 ; i<=s ; i++)
		{
			if(vetor[i]!=0)
			{
				if(pessoas>=i)
				{
					pessoas+=vetor[i];
				}
				else
				{
					amigos+=i-pessoas;
					pessoas+=i-pessoas;
					i--;
				}
			}
		}
		
		printf("Case #%d: %d\n", caso++, amigos);
	}
}
