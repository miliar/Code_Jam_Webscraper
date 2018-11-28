#include<stdio.h>
#include<list>

using namespace std;

void solve(int caseno)
{
	list<float> naomi;
	list<float> ken;
	naomi.clear();
	ken.clear();

	int N = 0;
	int i;
	float temp = 0;

	scanf("%d", &N);
	for(i = 0; i < N; i++)
	{
		scanf("%f", &temp);
		naomi.push_back(temp);
	}
	for(i = 0; i < N; i++)
	{
		scanf("%f", &temp);
		ken.push_back(temp);
	}
	naomi.sort();
	ken.sort();

	int c_naomi = 0, c_ken = 0;

	list<float>::iterator i_naomi = naomi.begin();
	list<float>::iterator i_ken = ken.begin();
	while(i_naomi != naomi.end() && i_ken != ken.end())
	{
		if(i_naomi._Mynode()->_Myval > i_ken._Mynode()->_Myval)
		{
			c_naomi++;
			i_ken++;
		}
		i_naomi++;
	}
	i_naomi = naomi.begin();
	i_ken = ken.begin();
	while(i_naomi != naomi.end() && i_ken != ken.end())
	{
		if(i_naomi._Mynode()->_Myval < i_ken._Mynode()->_Myval)
		{
			c_ken++;
			i_naomi++;
		}
		i_ken++;
	}
	printf("Case #%d: %d %d\n", caseno, c_naomi, N-c_ken);
}

int main()
{
	int t = 0;
	scanf("%d", &t);
	for(int i = 0; i<t; i++)
		solve(i+1);
	return 0;
}