#include<stdio.h>
#include<iostream>
#include<set>

using namespace::std;

int main()
{
	int T;scanf("%d", &T);
	int riadok;
	set<int>cisla;
	int x=0, cislo=0, vystup=1;
	bool bol=0, hladaj=0;


	for(int i=0;i<T;++i)
	{
		scanf("%d", &riadok);

		for(int a=0;a<4;++a)for(int b=0;b<4;++b)
		{
			if(a == (riadok-1))scanf("%d", &x), cisla.insert(x);
			else scanf("%d", &x);
		}

		scanf("%d", &riadok);

		for(int a=0;a<4;++a)for(int b=0;b<4;++b)
		{
			if(a == (riadok-1) )
			{
				scanf("%d", &x);
				hladaj=cisla.find(x) != cisla.end();
				if(hladaj && bol==false)cislo=x, bol=true;
				else if(hladaj && bol==true)vystup=2;
			}
			else scanf("%d", &x);
		}

		printf("Case #%d: ", i+1);
		if(vystup==1 && cislo != 0)printf("%d\n", cislo);
		else if(vystup==2)printf("Bad magician!\n");
		else if(vystup==1 && cislo == 0)printf("Volunteer cheated!\n");

		cisla.clear();
		x=0, cislo=0, vystup=1;
		bol=0, hladaj=0;
	}

	return 0;
}