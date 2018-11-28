#include <iostream>
#include <iomanip.h>
#include <fstream.h>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <iomanip>
#include <cstdio>
#include <vector>
#include <queue>
using namespace std;


int main()
{
	int x[5][5];
	int vis[20];
	int t,a,b,num,num1,num2,k;
 	ifstream f1("d:\\A-small-attempt3.in");
 	ofstream f2("d:\\A-small-attempt0.out");
	f1>>t;
	for (int i=1;i<=t;i++)
	{
		f2<<"Case #"<<i<<": ";
		f1>>num1;
		for (a=1;a<=4;a++)
			for (b=1;b<=4;b++)
			f1>>x[a][b];
		memset(vis,0,sizeof(vis));
		for (a=1;a<=4;a++)
			vis[x[num1][a]]++;
			
		f1>>num2;
		for (a=1;a<=4;a++)
			for (b=1;b<=4;b++)
			f1>>x[a][b];
		for (a=1;a<=4;a++)
			vis[x[num2][a]]++;
		num=0;
		k=0;
		for (a=1;a<=16;a++)
		{
			if (vis[a]==2) 
			{
				num=a;
				k++;
			}
		} 
		if (k==0) f2<<"Volunteer cheated!\n";
		else if (k>1) f2<<"Bad magician!\n";
		else f2<<num<<endl;
	}
    return 0;
}
