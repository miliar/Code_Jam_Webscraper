#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <cstring>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <queue>
#include <stack>

using namespace std;
#define FOR(i, a, b) for( int i = (a); i < (b); i++ )
#define Fore(it, x) for(typeof (x.begin()) it = x.begin(); it != x.end (); it++)
#define Set(a, s) memset(a, s, sizeof (a))

char arr[5][5];

bool isWin(char c)
{
	bool sameh=1, samev=1,samed1=1,samed2=1,res=0;
	FOR(i,0,4)
	{
		sameh=1, samev=1,samed1=1,samed2=1;
		FOR(j,0,4)
		{
			sameh&=(arr[i][j]==c || arr[i][j]=='T');
			samev&=(arr[j][i]==c || arr[j][i]=='T');
			samed1&=(arr[j][j]==c || arr[j][j]=='T');
			samed2&=(arr[j][3-j]==c || arr[j][3-j]=='T');
		}
		res|=  (sameh | samev | samed1 | samed2);
		if(res)return true;
	}	
	return res;
}
bool hasEmpty()
{
	FOR(i,0,4)FOR(j,0,4)if(arr[i][j]=='.')return true;
	return false;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,kase=0;
	cin>>t;
	while(t--)
	{
		FOR(i,0,4)
			FOR(j,0,4)
			cin>>arr[i][j];
		cout<<"Case #"<<++kase<<": ";
		if(isWin('X'))
			cout<<"X won"<<endl;
		else if(isWin('O'))
			cout<<"O won"<<endl;
		else if (hasEmpty())
			cout<<"Game has not completed"<<endl;
		else
			cout<<"Draw"<<endl;
	}
	return 0;
}