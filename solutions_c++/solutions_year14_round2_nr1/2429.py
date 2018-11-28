#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

int t;
int n;
string slowa[107];
string nowe[107];
int ilek[107];
int m;
int wyn;
int ile;

bool pacz()
{
	for (int i=1; i<=n; i++)
	{
		for (int j=i+1; j<=n; j++)
		{
			if (nowe[i]!=nowe[j])
			return false;
		}
	}
	return true;
}

int licz(int v, int znak)
{
	int moc=0;
	for (int i=slowa[v].size()-1; i>=0; i--)
	{
		if (slowa[v][i]==nowe[1][znak])
		{
			moc++;
			slowa[v].erase(i, 1);
		}
		else
		break;
	}
	return moc;
}

int main()
{
	scanf("%d", &t);
	for (int h=1; h<=t; h++)
	{
		scanf("%d", &n);
		wyn=0;
		for (int i=1; i<=n; i++)
		{
			cin >> slowa[i];
			nowe[i]="";
			for (int j=0; j<slowa[i].size(); j++)
			{
				if (!j || slowa[i][j]!=slowa[i][j-1])
				nowe[i]+=slowa[i][j];
			}
		}
		printf("Case #%d: ", h);
		if (!pacz())
		{
			printf("Fegla Won\n");
			continue;
		}
		m=nowe[1].size();
		for (int i=m-1; i>=0; i--)
		{
			ile=0;
			for (int j=1; j<=n; j++)
			{
				ilek[j]=licz(j, i);
				ile+=ilek[j];
			}
			if ((ile%n)*2>n)
			ile=(ile/n)+1;
			else
			ile=ile/n;
			for (int j=1; j<=n; j++)
			{
				if (ilek[j]<ile)
				wyn+=(ile-ilek[j]);
				else
				wyn+=(ilek[j]-ile);
			}
		}
		printf("%d\n", wyn);
	}
	return 0;
}
