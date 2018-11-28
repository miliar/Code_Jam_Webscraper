#include <iostream>
#include <cstdio>
#include <algorithm>
#include <map>
#include <cstring>
using namespace std;
int t,f[10];
string input;
map <char,int> banyak;
int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		memset(f,0,sizeof(f));
		cin>>input;
		for(int j=0;j<input.length();j++)
		{
			banyak[input[j]]++;
		}
		while(banyak['Z']>0) //zero
		{
			f[0]++;
			banyak['Z']--;
			banyak['E']--;
			banyak['R']--;
			banyak['O']--;
		}
		while(banyak['X']>0) //six
		{
			f[6]++;
			banyak['S']--;
			banyak['I']--;
			banyak['X']--;
		}
		while(banyak['G']>0) //eight
		{
			f[8]++;
			banyak['E']--;
			banyak['I']--;
			banyak['G']--;
			banyak['H']--;
			banyak['T']--;
		}
		while(banyak['H']>0) //three
		{
			f[3]++;
			banyak['T']--;
			banyak['H']--;
			banyak['R']--;
			banyak['E']--;
			banyak['E']--;
		}
		while(banyak['W']>0) //two
		{
			f[2]++;
			banyak['T']--;
			banyak['W']--;
			banyak['O']--;
		}
		while(banyak['R']>0) //four
		{
			f[4]++;
			banyak['F']--;
			banyak['O']--;
			banyak['U']--;
			banyak['R']--;
		}
		while(banyak['O']>0) //one
		{
			f[1]++;
			banyak['O']--;
			banyak['N']--;
			banyak['E']--;
		}
		while(banyak['F']>0) //five
		{
			f[5]++;
			banyak['F']--;
			banyak['I']--;
			banyak['V']--;
			banyak['E']--;
		}
		while(banyak['V']>0) //seven
		{
			f[7]++;
			banyak['S']--;
			banyak['E']--;
			banyak['V']--;
			banyak['E']--;
			banyak['N']--;
		}
		while(banyak['I']>0) //nine
		{
			f[9]++;
			banyak['N']--;
			banyak['I']--;
			banyak['N']--;
			banyak['E']--;
		}
		printf("Case #%d: ",i);
		for(int j=0;j<10;j++)
		{
			while(f[j]--)
				printf("%d",j);
		}
		printf("\n");
	}	
}
