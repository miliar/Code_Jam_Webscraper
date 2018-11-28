#include <iostream>
#include <stdio.h>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <cstring>
#include <queue>
using namespace std;
int t,i,j;
string k;
void poxel(int x)
{
	if(k[x] == '-') k[x] = '+';
	else k[x] = '-';
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin>>t;
	for(j=1;j<=t;j++)
	{
		cin>>k;
		int answ = 0;
		int p = 0;
		for(i = (int)(k.size()) - 1;i>=0;i--)
		{
			if(p%2 == 1) poxel(i);
			if(k[i] == '+') continue;
			answ++;
			p++;
		}
		cout<<"Case #"<<j<<": "<<answ<<endl;
	}
//	cin>>i;
	return 0;
}
