/*
ID: yusup
PROG:
LANG: C++
*/

//#include <bits/stdc++.h>

#include <fstream>

#define INF  10000000000

using namespace std;

ifstream cin ("file.in");
ofstream cout ("file.out");
int smax[110];
int result[1010];
char arr[1010];

int main()
{
	int t,q=0,smax;
	cin>>t;
	result[-1]=0;
	for (int i=0;i<t;i++)
	{
		cin>>smax;
		for (int j=0;j<smax+1;j++)
		{
			cin>>arr[j];
			if (result[j-1]>=j)
			result[j]=result[j-1]+(int(arr[j])-48);
			else
			{
				q+=j-result[j-1];
				result[j]=result[j-1]+(int(arr[j])-48+(j-result[j-1]));
			}
		}
		cout<<"Case #"<<i+1<<": "<<q<<endl;
		q=0;
	}
}


