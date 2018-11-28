#include <fstream>
#include <math.h>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <limits.h>
#include <stdlib.h> 
#include <set>
#include <queue>
using namespace std;
#pragma comment(linker, "/STACK:999999999")
#define ll long long
const long long MAXN = 102;
const long double eps=0.00000000001;




int main()
{
	ifstream cin("input.txt");
	ofstream cout("output1.txt");
	int t,n,m;
	cin>>t;
	for (int q=0;q<t;q++)
	{
		cin>>n;
		int a[5][5],b[5][5];
		for (int i=1;i<=4;i++)
			for (int j=1;j<=4;j++)
				cin>>a[i][j];
		cin>>m;
		for (int i=1;i<=4;i++)
			for (int j=1;j<=4;j++)
				cin>>b[i][j];
		int r=0;
		int an=0;
		for (int i=1;i<=4;i++)
			for (int j=1;j<=4;j++)
			{
				if (a[n][i]==b[m][j])
				{
					r++;
					an=a[n][i];
				}
			}
			cout<<"Case #"<<q+1<<": ";
			if (r==0)
				cout<<"Volunteer cheated!";
			if (r==1)
				cout<<an;
			if (r>1)
				cout<<"Bad magician!";
			cout<<endl;
	}
					
	return 0;
}