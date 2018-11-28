#include <stdio.h>
#include <map>
using namespace std;

pair<int,char> multiplica(pair< int,char> a, pair< int,char> b)
{
	pair< int,char> c;
	c.first = a.first*b.first;
	switch(a.second)
	{
		case '1':
		{
			c.second = b.second;
			return c;
		}
		case 'i':
		{	
			if (b.second == 'i')
			{
				c.first*=-1;
				c.second = '1';
				return c;
			
			}
			else if (b.second == 'j')
			{
				c.second = 'k';
				return c;
				
			}
			else if (b.second == '1')
			{
				c.second = a.second;
				return c;
			}
			else 
			{
				c.first*=-1;
				c.second = 'j';
				return c;
			}

			break;
		}

		case 'j':
		{	
			if (b.second == 'i')
			{
				c.first*=-1;
				c.second = 'k';
				return c;
			
			}
			else if (b.second == 'j')
			{
				c.first*=-1;
				c.second = '1';
				return c;
				
			}
			else if (b.second == '1')
			{
				c.second = a.second;
				return c;
			}
			else 
			{
				
				c.second = 'i';
				return c;
			}

			break;
		}

		case 'k':
		{	
			if (b.second == 'i')
			{
				//c.first*=-1;
				c.second = 'j';
				return c;
			
			}
			else if (b.second == 'j')
			{
				c.first*=-1;
				c.second = 'i';
				return c;
				
			}
			else if (b.second == '1')
			{
				c.second = a.second;
				return c;
			}
			else 
			{
				c.first*=-1;
				c.second = '1';
				return c;
			}

			break;
		}


	}
	return c;
}

int main()
{

	int t;
	scanf("%d",&t);
	int teste = 0;
	char numero[10000 + 5];
	while(t--)
	{
		int ponto1, ponto2;
		ponto1 = ponto2 = -1;
		

		int l,x;
		pair<int,char>novo;
		pair<int,char>I = make_pair(1,'i');
		pair<int,char>J = make_pair(1,'j');
		pair<int,char>K = make_pair(1,'k');
	
		scanf("%d%d",&l,&x);
		scanf("%s",numero);
		pair< int,char> atual = make_pair(1,'1');
		for (int h = 1;h<=x;h++)
			for (int i = 0; i <l; i++)
				{
					//printf("\n",atual.first, atual.second);
					if (atual == I&&ponto1==-1)
					{
						ponto1 = i;
						atual = make_pair(1,'1');
					}
					if (atual == J&&ponto1!=-1&&ponto2==-1)
					{
						ponto2 = i;
						atual = make_pair(1,'1');
					}

					char b = numero[i];
					novo = make_pair(1,b);
					//printf("%d %c",atual.first, atual.second);
					atual = multiplica(atual,novo);
					//printf("%d %c\n",atual.first, atual.second);
					
				}
		teste++;
		printf("Case #%d: ",teste);
		if (atual == K&&ponto1!=-1&&ponto2!=-1)
			printf("YES\n");
		else printf("NO\n");
		
	}
	return 0;
}