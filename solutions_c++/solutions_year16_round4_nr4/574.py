#include <bits/stdc++.h>
using namespace std;

int K[10][10];
int Wyp[10][10];
int N;
char input[10];


int Stan[10]; //stanowisko, na którym jest i
int Order[10]; // kolejność zasiadania

bool check()
{
	

	for(int i = 0; i < N; ++i)
		Stan[i] = i;
	bool istnieje = false;
	do
	{
		for(int i = 0; i < N; ++i)
		Order[i] = i;
		do
		{
			bool Zajete[10];
			for(int i = 0; i < N; ++i) Zajete[i] = false;
			bool Kupa = true;
			for(int i = 0; i < N && Kupa; ++i)
			{
				int c = Order[i];
				Zajete[Stan[c]] = true;
				if(Wyp[c][Stan[c]] == 0)
				{
					bool dupa = false;
					for(int i = 0; i < N && dupa == false; ++i)
						if(Zajete[i] == false && Wyp[c][i] == 1)
							dupa = true;
					if(dupa == false) return false;
					else
						Kupa = false;
				}
			}
			if(Kupa == true)
				istnieje = true;
					
		}while(next_permutation(Order, Order+N));
	}while(next_permutation(Stan, Stan+N));
	return istnieje;
}


void solver()
{
	scanf("%d", &N);
	for(int i = 0; i < N; ++i)
	{
		scanf("%s", input);
		for(int j = 0; j < N; ++j)
			K[i][j] = input[j]-'0';
	}
	int MAX = 1 << (N*N);
	int MNauk = 1000000;

	for(int i = 0; i < MAX; ++i)
	{
		bool Not = false;
		for(int j = 0; j < N; ++j)
			for(int k = 0; k < N; ++k)
			{
				if(i & (1 << (j*N+k)))
					Wyp[j][k] = 1;
				else
					Wyp[j][k] = 0;
			}
		for(int j = 0; j < N; ++j)
			for(int k = 0; k < N; ++k)
				if(K[j][k] == 1)
				{
					if(Wyp[j][k] == 1) Not = true;
					else Wyp[j][k] = 1;
				}
		if(Not == false)
		{
			if(check() == true)
				MNauk = min(MNauk, __builtin_popcount(i));
			
			
		}
		
	}
	printf("%d", MNauk);
	
	
}
int main()
{
	ios_base::sync_with_stdio(0);
	//solver();
	//return 0;
	int T;
	scanf("%d", &T);
	for(int i = 1; i <= T; ++i)
	{
		printf("Case #%d: ", i);
		solver();
		puts("");
	}
	
	
	return 0;
}
