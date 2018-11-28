#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
void wyjscie(int a)
{
	printf("Case #%d: ",a);
	return;
}
int main()
{
	int lol, n, ilo;
	string s;
	bool tak=0;
	char c, zap;
	scanf("%d", &lol);
	for(int h = 0 ; h < lol ; h++)
	{
		scanf("%d", &n);
		int tab[n+4][1010];
		for(int i = 0 ; i <= n ; i++)
			for(int j = 0 ; j <= 1000 ; j++)
				tab[i][j]=0;
		ilo=0;
		int wynik=0;
		zap='Z';
		string kupa;
		string a;
		string b;
		for(int i = 0 ; i < n ; i++)
		{
			cin>>a;
			b.resize(0);
			zap='Z';
			for(int j = 0 ; j < a.size() ; j++)
			{
				if(a[j]!=zap)
				{
					b.push_back(a[j]);
					//cout<<a[j];
					zap=a[j];
				}
				tab[i][b.size()]++;
			}
			if(i==0)
				kupa=b;
////////////////////////////////////
			//cout<<b<<endl;
////////////////////////////////////
			if(b!=kupa && i!= 0)
				tak=1;
		}
/////////////////////////////////////
// 		for(int i = 0 ; i < n ; i++)
// 		{
// 			for(int j = 0 ; j < 26 ; j++)
// 			{
// 				cout<<tab[i][j]<<" ";
// 			}
// 			cout<<endl;
// 		}
/////////////////////////////////////
		if(tak==1)
		{ 
			wyjscie(h+1);
			printf("Fegla Won\n");
			tak=0;
			continue;
		}
		int t[n+5];
		for(int i = 0 ; i < 200 ; i++)
		{
			for(int j = 0 ; j < n; j++)
			{
				t[j]=tab[j][i];
			}
			sort(t,t+n);
			int k = t[(n/2)];
			//cout<<"---> "<<k<<endl;
			for(int j = 0 ; j < n ; j++)
			{
				wynik += abs(t[j]-k);
			}
		}

		wyjscie(h+1);
		printf("%d\n",wynik);
	}
	
	return 0;
}